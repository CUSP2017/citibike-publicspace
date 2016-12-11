# Citbike Stations and Public Space
Final project for Applied Data Science, a Fall 2016 course at [NYU's Center for Urban Science + Progress](http://cusp.nyu.edu) taught by Dr. Stanislav Sobolevsky.

## Abstract

This project attempts to quantify the value of public space by investigating whether the quality of public space around a Citibike docking station increases ridership at that station controlling for other possible factors. The quality of public space is quantified this project using a combination of data, including the quality and traffic volumne on the street, the presence of bike lanes, the nearby presence of parks or subway entrances, and the number and quality of trees in the area. Controlling factors include median houshold income per census tract and population density. The project concludes that, though ridership at Citibike docking stations are not a good way to quantify people's preferences based on public space, the methodology used to develop the model, given a different dependent variable (such as urban sensing data) could prove to be useful for both public agencies and private companies.

## Reproducing Our Research

### 1. Set up your environment variables
Copy the .env example

```
cp .env-example .env
```

Edit `.env`, adding a Google Geocoding API Key that can be acquired [here](https://developers.google.com/maps/documentation/geocoding/intro).

### 2. Download the data
To download the raw, external data, first run in the root directory of this project:

```
make download_data
```

This will create a collection of directories under `data/` that will store all
external and processed data. This may take a few minutes depending on the
speed of your internet.

### 3. Process data

Run through all notebooks in the `notebooks` folder in the order of their prefix.
This will generate data in the `/data/processed` and `/data/map` folders to be used for analysis.

>Naming convention for all notebooks in the project: order number, the creator's initials, and a short `-` delimited description, e.g. `1.0-jp-initial-data-exploration`.

### 4. Analyze Data

Run through all notebooks in the `models` folder. These notebooks will run various regressions, outputting
our findings.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make download_data`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── map            <- Data to be used for mapping and visualizations.
    ├── notebooks          <- Data processing Jupyter notebooks.
    ├── models             <- Regression and analysis Jupyter notebooks.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    └── scripts            <- Source code for use in this project.

## Data Sources

| Citi Bike Docking Stations | [Citi Bike System Data](https://www.citibikenyc.com/system-data)                                                   |
| Street Assessment Ratings  | [NYC Dept of Transportation](http://www.nyc.gov/html/dot/html/about/datafeeds.shtml)                               |
| Parks                      | [NYC Open Data](https://data.cityofnewyork.us/City-Government/Parks-Properties/rjaj-zgq7)                          |
| Subway Entrances           | [NYC Open Data](https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56)                           |
| Bike Lanes                 | [NYC Dept of Transportation](http://www.nyc.gov/html/dot/html/about/datafeeds.shtml)                               |
| Tree Canopy                | [NYC Open Data](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh)             |
| Traffic Volume             | [NY State Dept of Transportation](https://www.dot.ny.gov/tdv)                                                      |
| Citi Bike Ridership        | [Citi Bike System Data](https://s3.amazonaws.com/tripdata/index.html)                                              |
| Median Household Income    | [United States Census](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t)            |
| Population Density         | [NYC Open Data](https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Census-Tracts/37cg-gxjd) |

## Attributions

- The directory structure of this project was inspired by the [Cookie Cutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) project.
