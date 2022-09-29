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
    - dedupe@main from github: 1 positive, 50 negative


## Installing from github

Installed dedupe from within the conda environment as follows:

```bash
python -m pip install "dedupe @ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc"
```

This was the output: 
```bash
Collecting dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Cloning https://github.com/dedupeio/dedupe (to revision 522e7b2147d61fa36d6dee6288df57aee95c4bcc) to /tmp/pip-install-s9gwll_e/dedupe_5b76234a1cc64a758529db20a7bfdd2e
  Running command git clone --filter=blob:none --quiet https://github.com/dedupeio/dedupe /tmp/pip-install-s9gwll_e/dedupe_5b76234a1cc64a758529db20a7bfdd2e
  Running command git rev-parse -q --verify 'sha^522e7b2147d61fa36d6dee6288df57aee95c4bcc'
  Running command git fetch -q https://github.com/dedupeio/dedupe 522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Running command git checkout -q 522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Resolved https://github.com/dedupeio/dedupe to commit 522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: haversine>=0.4.1 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (2.7.0)
Requirement already satisfied: highered>=0.2.0 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (0.2.1)
Requirement already satisfied: doublemetaphone in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.1)
Requirement already satisfied: numpy>=1.20 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.23.3)
Requirement already satisfied: categorical-distance>=1.9 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.9)
Requirement already satisfied: simplecosine>=1.2 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.2)
Requirement already satisfied: typing-extensions in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (4.3.0)
Requirement already satisfied: zope.index in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (5.2.1)
Requirement already satisfied: Levenshtein-search==1.4.5 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.4.5)
Requirement already satisfied: scikit-learn in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.1.2)
Requirement already satisfied: BTrees>=4.1.4 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (4.10.1)
Requirement already satisfied: dedupe-variable-datetime in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (0.1.5)
Requirement already satisfied: affinegap>=1.3 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.12)
Requirement already satisfied: zope.interface>=5.0.0 in ./env/lib/python3.9/site-packages (from BTrees>=4.1.4->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (5.4.0)
Requirement already satisfied: persistent>=4.1.0 in ./env/lib/python3.9/site-packages (from BTrees>=4.1.4->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (4.9.1)
Requirement already satisfied: pyhacrf-datamade>=0.2.0 in ./env/lib/python3.9/site-packages (from highered>=0.2.0->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (0.2.6)
Requirement already satisfied: future in ./env/lib/python3.9/site-packages (from dedupe-variable-datetime->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (0.18.2)
Requirement already satisfied: datetime-distance in ./env/lib/python3.9/site-packages (from dedupe-variable-datetime->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (0.1.3)
Requirement already satisfied: threadpoolctl>=2.0.0 in ./env/lib/python3.9/site-packages (from scikit-learn->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (3.1.0)
Requirement already satisfied: joblib>=1.0.0 in ./env/lib/python3.9/site-packages (from scikit-learn->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.2.0)
Requirement already satisfied: scipy>=1.3.2 in ./env/lib/python3.9/site-packages (from scikit-learn->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.9.1)
Requirement already satisfied: six in ./env/lib/python3.9/site-packages (from zope.index->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.16.0)
Requirement already satisfied: setuptools in ./env/lib/python3.9/site-packages (from zope.index->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (65.4.0)
Requirement already satisfied: cffi in ./env/lib/python3.9/site-packages (from persistent>=4.1.0->BTrees>=4.1.4->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.15.1)
Requirement already satisfied: PyLBFGS>=0.1.3 in ./env/lib/python3.9/site-packages (from pyhacrf-datamade>=0.2.0->highered>=0.2.0->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (0.2.0.14)
Requirement already satisfied: python-dateutil>=2.6.0 in ./env/lib/python3.9/site-packages (from datetime-distance->dedupe-variable-datetime->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (2.8.2)
Requirement already satisfied: pycparser in ./env/lib/python3.9/site-packages (from cffi->persistent>=4.1.0->BTrees>=4.1.4->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (2.21)
```


But then, `conda list |grep dedupe` gives dedupe 2.0.18, from pypi...