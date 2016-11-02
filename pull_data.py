import os
import glob
import requests
import zipfile

# Hide InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

project_dir = os.path.dirname(__file__)
dl_path = os.path.join(project_dir, "data/external")

# Create data directories if needed
for d in ["data", "data/external", "data/interim", "data/processed"]:
    if not os.path.exists(d):
        os.makedirs(d)

files = [
    {
        "name": "citibike-stations.json",
        "url": "https://feeds.citibikenyc.com/stations/stations.json",
        "params": {},
        "zip": False
    },
    {
        "name": "tree-canopy.geojson",
        "url": "https://data.cityofnewyork.us/api/geospatial/pi5s-9p35",
        "params": {"method": "export", "format": "GeoJSON"},
        "zip": False
    },
    {
        "name": "street-assessment.zip",
        "url": "http://www.nyc.gov/html/dot/downloads/misc/street-assessment-rating.zip",
        "params": {},
        "zip": "street-assessment"
    },
    {
        "name": "subway-entrances.geojson",
        "url": "https://data.cityofnewyork.us/api/geospatial/drex-xx56",
        "params": {"method": "export", "format": "GeoJSON"},
        "zip": False
    },
    {
        "name": "bike-lanes.zip",
        "url": "http://www.nyc.gov/html/dot/downloads/misc/nyc-bike-routes.zip",
        "params": {},
        "zip": "bike-lanes"
    },
    {
        "name": "nyc-boroughs.zip",
        "url": "http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_16c.zip",
        "params": {},
        "zip": "nyc-boroughs"
    },
    {
        "name": "nyc-traffic.zip",
        "url": "https://www.dot.ny.gov/divisions/engineering/applications/traffic-data-viewer/traffic-data-viewer-repository/TDV_Shapefile_AADT_2015.zip",
        "params": {},
        "zip": "nyc-traffic"
    }
]

def download(arg):
    save_path = dl_path + "/" + arg["name"]
    if not os.path.isfile(save_path):
        print("Downloading " + arg["name"])
        r = requests.get(arg["url"], params=arg["params"], stream=True, verify=False)
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        if arg["zip"]:
            zip = zipfile.ZipFile(save_path)
            zip.extractall(dl_path + '/' + arg["zip"])

# Run the download for the files
for f in files:
    download(f)

# Download citibike ridership for 2015
citibike_months = ["201501", "201502", "201503", "201504", "201505", "201506",
                   "201507", "201508", "201509", "201510", "201511", "201512"]
citibike_data_files = [month + "-citibike-tripdata.zip" for month in citibike_months]

for citi in citibike_data_files:
    download({
        "name": citi,
        "url": "https://s3.amazonaws.com/tripdata/" + citi,
        "params": {},
        "zip": "ridership"
    })
