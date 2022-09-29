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
conda activate ./env
# label records
python -m src.label
```

To install instead the github version, I did 

```bash
conda env create --prefix ./env --file environment_github.yml

conda activate ./env
conda install git pip 
python -m pip install "dedupe @ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc"

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



## Does it install the correct version from github?

This was the output when installing dedupe from github:
```bash
Collecting dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Cloning https://github.com/dedupeio/dedupe (to revision 522e7b2147d61fa36d6dee6288df57aee95c4bcc) to /tmp/pip-install-yqbzj22v/dedupe_e97b15b0cac74885aebd898d39b36ce6
  Running command git clone --filter=blob:none --quiet https://github.com/dedupeio/dedupe /tmp/pip-install-yqbzj22v/dedupe_e97b15b0cac74885aebd898d39b36ce6
  Running command git rev-parse -q --verify 'sha^522e7b2147d61fa36d6dee6288df57aee95c4bcc'
  Running command git fetch -q https://github.com/dedupeio/dedupe 522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Running command git checkout -q 522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Resolved https://github.com/dedupeio/dedupe to commit 522e7b2147d61fa36d6dee6288df57aee95c4bcc
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting haversine>=0.4.1
  Using cached haversine-2.7.0-py2.py3-none-any.whl (6.9 kB)
Collecting categorical-distance>=1.9
  Using cached categorical_distance-1.9-py3-none-any.whl (3.3 kB)
Collecting highered>=0.2.0
  Using cached highered-0.2.1-py2.py3-none-any.whl (3.3 kB)
Collecting doublemetaphone
  Using cached DoubleMetaphone-1.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (149 kB)
Collecting Levenshtein-search==1.4.5
  Using cached Levenshtein_search-1.4.5-cp39-cp39-linux_x86_64.whl
Collecting scikit-learn
  Using cached scikit_learn-1.1.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30.8 MB)
Requirement already satisfied: numpy>=1.20 in ./env/lib/python3.9/site-packages (from dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.23.3)
Collecting simplecosine>=1.2
  Using cached simplecosine-1.2-py2.py3-none-any.whl (3.2 kB)
Collecting zope.index
  Using cached zope.index-5.2.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (105 kB)
Collecting affinegap>=1.3
  Using cached affinegap-1.12-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (56 kB)
Collecting BTrees>=4.1.4
  Using cached BTrees-4.10.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (3.8 MB)
Collecting dedupe-variable-datetime
  Using cached dedupe_variable_datetime-0.1.5-py3-none-any.whl (4.8 kB)
Collecting typing-extensions
  Using cached typing_extensions-4.3.0-py3-none-any.whl (25 kB)
Collecting zope.interface>=5.0.0
  Using cached zope.interface-5.4.0-cp39-cp39-manylinux2010_x86_64.whl (255 kB)
Collecting persistent>=4.1.0
  Using cached persistent-4.9.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (258 kB)
Collecting pyhacrf-datamade>=0.2.0
  Using cached pyhacrf_datamade-0.2.6-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)
Collecting datetime-distance
  Using cached datetime_distance-0.1.3-py3-none-any.whl (4.1 kB)
Collecting future
  Using cached future-0.18.2-py3-none-any.whl
Collecting threadpoolctl>=2.0.0
  Using cached threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Requirement already satisfied: scipy>=1.3.2 in ./env/lib/python3.9/site-packages (from scikit-learn->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.9.1)
Requirement already satisfied: joblib>=1.0.0 in ./env/lib/python3.9/site-packages (from scikit-learn->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.2.0)
Requirement already satisfied: six in ./env/lib/python3.9/site-packages (from zope.index->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (1.16.0)
Requirement already satisfied: setuptools in ./env/lib/python3.9/site-packages (from zope.index->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (65.4.0)
Collecting cffi
  Using cached cffi-1.15.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (441 kB)
Collecting PyLBFGS>=0.1.3
  Using cached PyLBFGS-0.2.0.14-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (273 kB)
Requirement already satisfied: python-dateutil>=2.6.0 in ./env/lib/python3.9/site-packages (from datetime-distance->dedupe-variable-datetime->dedupe@ git+https://github.com/dedupeio/dedupe@522e7b2147d61fa36d6dee6288df57aee95c4bcc) (2.8.2)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Building wheels for collected packages: dedupe
  Building wheel for dedupe (pyproject.toml) ... done
  Created wheel for dedupe: filename=dedupe-2.0.18-cp39-cp39-linux_x86_64.whl size=93036 sha256=c334d10776b663927019b9df8a3c8f85fd6f423d124cf1dce5720bbfa9e9867f
  Stored in directory: /home/flavio/.cache/pip/wheels/b7/2e/79/aa60287c4de830c8d5c3e889a8f46e1f91bad6c3eff70dbca0
Successfully built dedupe
Installing collected packages: Levenshtein-search, doublemetaphone, affinegap, zope.interface, typing-extensions, threadpoolctl, simplecosine, PyLBFGS, pycparser, haversine, future, categorical-distance, scikit-learn, pyhacrf-datamade, datetime-distance, cffi, persistent, highered, BTrees, zope.index, dedupe-variable-datetime, dedupe
Successfully installed BTrees-4.10.1 Levenshtein-search-1.4.5 PyLBFGS-0.2.0.14 affinegap-1.12 categorical-distance-1.9 cffi-1.15.1 datetime-distance-0.1.3 dedupe-2.0.18 dedupe-variable-datetime-0.1.5 doublemetaphone-1.1 future-0.18.2 haversine-2.7.0 highered-0.2.1 persistent-4.9.1 pycparser-2.21 pyhacrf-datamade-0.2.6 scikit-learn-1.1.2 simplecosine-1.2 threadpoolctl-3.1.0 typing-extensions-4.3.0 zope.index-5.2.1 zope.interface-5.4.0
```


But then, `conda list |grep dedupe` gives dedupe 2.0.18, from pypi...