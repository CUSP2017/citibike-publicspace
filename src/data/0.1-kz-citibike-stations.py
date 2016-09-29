
#Get Citibike station location data

#url format:  https://feeds.citibikenyc.com/stations/stations.json


import json
import urllib
import codecs
import pandas as pd
import numpy as np

citibike_serviceurl =  "https://feeds.citibikenyc.com/stations/stations.json"

while True:

    url = citibike_serviceurl
    print 'Retrieving', url

    data = urllib.urlopen(url).read()
    try:
        data_js = json.loads(str(data))
    except:
        data_js = None
        print '==Failure to Retrieve=='
        continue

    #fhand = codecs.open('citibike_loc_json.js', 'w', "utf-8")   #create a json file to inspect the format and content
    #fhand.writelines(json.dumps(data_js, indent=4))

    fname = 'citibike_station_info.csv'
    fh_cb = open(fname, 'w+')
    fh_cb.writelines('Station_id,Station_Name,Location,Latitude,Longitude,Total_Docks,Available_Docks,Available_Bikes,lastCommunicationTime,Status,Test_Station,Status_Key')

    all_station_info = data_js['stationBeanList']
    for station in all_station_info:
        cb_station_id = station['id']
        cb_station_name = station['stationName']
        cb_location = station['stAddress1']
        lat = station['latitude']
        lon = station['longitude']

        tot_docks = station["totalDocks"]
        avb_docks = station['availableDocks']
        avb_bikes = station['availableBikes']
        last_commu_time = station['lastCommunicationTime']
        status = station['statusValue']    # "In Service"
        is_test_station = station['testStation']
        status_key = station['statusKey']

        print '{},{},{},{},{},{},{},{},{},{},{},{}'.format(cb_station_id, cb_station_name,cb_location,lat,lon,tot_docks,avb_docks,avb_bikes,last_commu_time,status,is_test_station,status_key)
        fh_cb.writelines('\n{},{},{},{},{},{},{},{},{},{},{},{}'.format(cb_station_id, cb_station_name,cb_location,lat,lon,tot_docks,avb_docks,avb_bikes,last_commu_time,status,is_test_station,status_key))

    station_count = len(all_station_info)
    print '\nNumber of Citi Bike stations ', station_count

    break


# create DataFrame using Pandas
#fh_cb = open(fname, 'r')
#df_cb = pd.read_csv(fname)
#df_cb.head(20)





