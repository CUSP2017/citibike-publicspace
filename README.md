# Understanding the value of Public Space with Citibike Riderships

## Getting Started

1. Download the data
To download the raw, external data, first run in the root directory of this project:

```
make download_data
```

This will create a collection of directories under `data/` that will store all
external and processed data. This may take a few minutes depending on the
speed of your internet.

2. Process the data
Next, run:

```
make process_data
```

This will generate the base CSV of Citibike stations.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py

## Project Notes

* The area of public space considered for this study was determined to be approximately a 185' radius around each Citibike Station
* The datasets used for this analysis were created in 2015 and 2016

## Attributions

- The directory structure of this project was inspired by the [Cookie Cutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) project.
