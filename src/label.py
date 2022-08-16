"""
This script uses dedupe for labelling links between two data set.
"""

import pandas as pd
import multiprocessing
import dedupe
import logging
import optparse

from src.helpers.utils import convert_to_tuple_of_tuples, convert_to_year_range
from src.helpers.setup_linking import fields

training_file = "data/training.json"
settings_file = "data/settings"

if __name__ == "__main__":

    # ## Logging
    optp = optparse.OptionParser()
    optp.add_option('-v', '--verbose', dest='verbose', action='count',
                    help='Increase verbosity (specify multiple times for more)'
                    )
    (opts, args) = optp.parse_args()
    log_level = logging.WARNING
    if opts.verbose:
        if opts.verbose == 1:
            log_level = logging.INFO
        elif opts.verbose >= 2:
            log_level = logging.DEBUG
    logging.getLogger().setLevel(log_level)

    # ## Prep data 
    print("Reading and preparing data", flush=True)

    d_mag = pd.read_csv("data/input_mag.csv", keep_default_na=False, na_values=["_"], dtype={"middlename": str})
    d_nsf = pd.read_csv("data/input_nsf.csv", keep_default_na=False, na_values=["_"], dtype={"middlename": str})

    n_cores = int(multiprocessing.cpu_count() / 2)

    for d in [d_nsf, d_mag]:
        for v in ["main_us_institutions_year", "all_us_institutions_year"]:
            d[v] = d.apply(lambda row: convert_to_tuple_of_tuples(row[v]), axis="columns")
        d["year_range"] = d.apply(lambda row: convert_to_year_range(row["year_range"]), axis="columns")

    # convert to dict for dedupe 
    nsfdata = d_nsf.set_index("grantid_personpos").T.to_dict(orient="dict") # not sure .T is necessary here but not below.. 
    magdata = d_mag.set_index("AuthorId").to_dict(orient="index")

    for data in [nsfdata, magdata]:
        for key in data.keys():
            middlename = data[key]["middlename"]
            if middlename == "":
                data[key]["middlename"] = None

    # ## Training
    linker = dedupe.RecordLink(fields, num_cores = n_cores) 
    linker.prepare_training(
        data_1=magdata, data_2=nsfdata, blocked_proportion=0.9, sample_size=100_000
        )

    print("Starting active labeling...", flush=True)
    dedupe.console_label(linker)

    linker.train()

    with open(training_file, "w") as tf: 
            linker.write_training(tf)
            
    with open(settings_file, "wb") as sf: 
        linker.write_settings(sf)


    linker.cleanup_training()

    print("Done.")

