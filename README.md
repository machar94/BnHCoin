# Installation instructions

Create a conda environment from the environment file:

``` bash
conda env create -f environment.yaml 
```

If you ever require a new package, add the package to the list of dependendencies and update the environment

``` bash
conda env update -f environment.yaml
```

## Create database

In the bnhcoin folder open a python interpreter and run the following:

``` python
>>> from app import db
>>> db.create_all()
```

You should notice that a site.db file has been created in the folder.
