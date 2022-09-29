# dedupe_training_example

Example data and scripts for investigating the training performance in dedupe.

## Contents

Two main scripts are in src/:
- make_extract.py: makes the sample data from a database. Not relevant for investigating dedupe.
- label.py: loads the data and asks user for labelling training data.

data/ contains the two data sets
- data set 1: bibliometric data from Microsoft Academic Graph. One version of the database is available [here](https://zenodo.org/record/6511057). 
- data set 2: grant data from NSF. [Source](https://www.nsf.gov/awardsearch/download.jsp).


## Installation
This works with a conda installation on Ubuntu 22:

```bash
# create environment
conda env create --prefix ./env --file environment.yml 
# to use the github version of dedupe instead:
# conda env create --prefix ./env --file environment_github.yml
conda activate ./env
# label records
python -m src.label
```

## Details
Some of the features in the data need further cleaning, but the sample illustrates the issue I have.


### What do the different fields mean, and how to decide whether the records are a match?
- `firstname`, `lastname`, `middlename` -> *Check how similar are the records*
- `year_range`: The tuple in the first record defines the start and end of the publication career of the person. The singleton in the second record is the year when the grant is awarded. -> *Check if the grant is awarded during the publication career of the person. You can add +/- 4 years around the start and end of the career of the person because of publication lag.*
- `main_us_institutions_year`: tuples of (x, y). In the first record, they mean that in year x, the person published most their papers at institution y. In the second record, they report the award year and institution of the grantee. -> *Check if there is a close overlap between the records. But it does not need to be perfect (people may not publish in every year, etc).*
- `all_us_institutions_year`: similar to the above. But for the first record, it reports the unique year-affiliation combinations under which the person has ever published anything. -> *The comparison should be made as in `main_us_institutions_year`. The idea is that this captures other affiliations of the person.*


## Trial log
Report the trials on labelling.
- 16/08/22. Field: physics.
    - dedupe 2.0.14: 1 positive, 23 negative
    - dedupe 2.0.13: 17 positive, 23 negative
- 29/09/22. Field: physics
    - dedupe@main from github: 1 positive, 72 negative


