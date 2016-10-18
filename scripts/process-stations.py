import json
import os

output_csv = os.getcwd() + '/data/processed/stations.csv'

with open(os.getcwd() + '/data/external/citibike-stations.json') as data_file:
    data_js = json.load(data_file)

if not os.path.isfile(output_csv):
    fh_cb = open(output_csv, 'w+')
    fh_cb.writelines('Station_id,Station_Name,Location,Latitude,Longitude')

    all_station_info = data_js['stationBeanList']
    for station in all_station_info:
        cb_station_id = station['id']
        cb_station_name = station['stationName']
        cb_location = station['stAddress1']
        lat = station['latitude']
        lon = station['longitude']

        fh_cb.writelines('\n{},{},{},{},{}'.format(cb_station_id, cb_station_name,cb_location,lat,lon))
