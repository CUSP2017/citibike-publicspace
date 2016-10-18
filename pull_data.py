import os
import glob
import requests
import zipfile

project_dir = os.path.dirname(__file__)
dl_path = os.path.join(project_dir, "data/external")

# Create data directories if needed
for d in ["data", "data/external", "data/interim", "data/processed"]:
    if not os.path.exists(d):
        os.makedirs(d)

# Citibike stations
citibike_file = dl_path + "/citibike-stations.json"
if not os.path.isfile(citibike_file):
    print("Downloading Citibike stations")
    r = requests.get('https://feeds.citibikenyc.com/stations/stations.json',
                     stream=True)

    with open(citibike_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# Tree Canopy
trees_file = dl_path + "/tree-canopy.geojson"
if not os.path.isfile(trees_file):
    print("Downloading Tree Canopy")
    r = requests.get('https://data.cityofnewyork.us/api/geospatial/pi5s-9p35',
                     params={"method": "export", "format": "GeoJSON"},
                     stream=True)

    with open(trees_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# Street Assessment
street_assessment_zip = dl_path + "/street-assessment.zip"
if not os.path.isfile(street_assessment_zip):
    print("Downloading ")
    r = requests.get('http://www.nyc.gov/html/dot/downloads/misc/street-assessment-rating.zip',
                     stream=True)

    with open(street_assessment_zip, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    zip = zipfile.ZipFile(street_assessment_zip)
    zip.extractall(dl_path + '/street-assessment')

# Subway Entrances
subway_file = dl_path + "/subway-entrances.geojson"
if not os.path.isfile(subway_file):
    print("Downloading Subway Entrances")
    r = requests.get('https://data.cityofnewyork.us/api/geospatial/drex-xx56',
                     params={"method": "export", "format": "GeoJSON"},
                     stream=True)

    with open(subway_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# Bike Routes
bike_zip = dl_path + "/bike-lanes.zip"
if not os.path.isfile(bike_zip):
    print("Downloading Bike Lanes")
    r = requests.get('http://www.nyc.gov/html/dot/downloads/misc/nyc-bike-routes.zip',
                     stream=True)

    with open(bike_zip, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    zip = zipfile.ZipFile(bike_zip)
    zip.extractall(dl_path + '/bike-lanes')

# Traffic Short Counts
traffic_short_zip = dl_path + "/traffic-short-counts.zip"
if not os.path.isfile(traffic_short_zip):
    print("Downloading Traffic Short Counts")
    r = requests.get('https://www.dot.ny.gov/divisions/engineering/applications/traffic-data-viewer/traffic-data-viewer-repository/TDV_Shapefile_Short_Counts_2014.zip',
                     params={"accessType": "DOWNLOAD"},
                     stream=True)

    with open(traffic_short_zip, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    zip = zipfile.ZipFile(traffic_short_zip)
    zip.extractall(dl_path + '/traffic-short-counts')

# Traffic Continuous Counts
traffic_continuous_zip = dl_path + "/traffic-continuous-counts.zip"
if not os.path.isfile(traffic_continuous_zip):
    print("Downloading Traffic Continuous Counts")
    r = requests.get('https://www.dot.ny.gov/divisions/engineering/applications/traffic-data-viewer/traffic-data-viewer-repository/TDV_Shapefile_Continuous_Counts_2014.zip',
                     params={"accessType": "DOWNLOAD"},
                     stream=True)

    with open(traffic_continuous_zip, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    zip = zipfile.ZipFile(traffic_continuous_zip)
    zip.extractall(dl_path + '/traffic-continuous-counts')
