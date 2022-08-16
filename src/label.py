
import pandas as pd
import multiprocessing
import dedupe

from src.helpers.utils import convert_to_tuple_of_tuples, convert_to_year_range
from src.helpers.setup_linking import fields

training_file = "data/training.json"
settings_file = "data/settings"


# TODO
    # add logging from dedupe?
    # is the year_range confusing: eg those that continue the career outside the us?
    # fix the numpy warning??


if __name__ == "__main__":

    print("Reading and preparing data", flush=True)

    d_mag = pd.read_csv("data/input_mag.csv", keep_default_na=False, na_values=["_"], dtype={"middlename": str})
    d_nsf = pd.read_csv("data/input_nsf.csv", keep_default_na=False, na_values=["_"], dtype={"middlename": str})

    n_cores = int(multiprocessing.cpu_count() / 2)

    for d in [d_nsf, d_mag]:
        for v in ["main_us_institutions_year", "all_us_institutions_year"]:
            d[v] = d.apply(lambda row: convert_to_tuple_of_tuples(row[v]), axis="columns")
        d["year_range"] = d.apply(lambda row: convert_to_year_range(row["year_range"]), axis="columns")

    # convert to dict for dedupe 
    nsfdata = d_nsf.set_index("grantid_personpos").T.to_dict(orient="dict") # TODO: why is the .T necessary here but not below??
    magdata = d_mag.set_index("AuthorId").to_dict(orient="index")

    for data in [nsfdata, magdata]:
        for key in data.keys():
            middlename = data[key]["middlename"]
            if middlename == "":
                data[key]["middlename"] = None

    linker = dedupe.RecordLink(fields, num_cores = n_cores) 
    linker.prepare_training(data_1=magdata, data_2=nsfdata)

    print("Starting active labeling...", flush=True)
    dedupe.console_label(linker)

    linker.train()

    with open(training_file, "w") as tf: 
            linker.write_training(tf)
            
    with open(settings_file, "wb") as sf: 
        linker.write_settings(sf)


    linker.cleanup_training()

    print("Done.")

