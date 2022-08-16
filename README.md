# dedupe_training_example

Example data and scripts for investigating the training performance in dedupe.

### Contents

Two main scripts are in src/:
- make_extract.py: makes the sample data from a database. Not relevant for investigating dedupe.
- label.py: loads the data and asks user for labelling training data.

data/ contains the two data sets
- data set 1: bibliometric data from Microsoft Academic Graph. One version of the database is available [here](https://zenodo.org/record/6511057). 
- data set 2: grant data from NSF. [Source](https://www.nsf.gov/awardsearch/download.jsp).


### Installation
- With conda, run `conda env create --prefix ./env --file environment.yml`, then `conda activate ./env`
- Run `src/label.py`


