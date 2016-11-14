import json
import os
import googlemaps
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_GEOCODING_KEY"))
output_csv = os.getcwd() + '/data/processed/stations.csv'

with open(os.getcwd() + '/data/external/citibike-stations.json') as data_file:
    data_js = json.load(data_file)

if not os.path.isfile(output_csv):
    fh_cb = open(output_csv, 'w+')
    fh_cb.writelines('Station_id,Station_Name,Location,Latitude,Longitude,Zip')

    all_station_info = data_js['stationBeanList']
    for station in all_station_info:
        # Reverse geocode to get zip
        response = gmaps.reverse_geocode({'lat': station['latitude'], 'lng': station['longitude']})
        for address in response[0]['address_components']:
            if "postal_code" in address["types"]:
                zipcode = address["long_name"]

        fh_cb.writelines('\n{},{},{},{},{},{}'.format(station['id'],
                                                      station['stationName'],
                                                      station['stAddress1'],
                                                      station['latitude'],
                                                      station['longitude'],
                                                      zipcode))
