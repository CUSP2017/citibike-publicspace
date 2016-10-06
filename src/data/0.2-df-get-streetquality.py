# Download street quality dataset from http://www.nyc.gov/html/dot/html/about/datafeeds.shtml#vision

import os

os.chdir("..")
os.chdir("..")
if not os.path.exists("data/external"):
    os.makedirs("data/external")

os.chdir("data/external")

if not os.path.isfile('street-assessment-rating.geojson'):
    os.system("curl -O http://www.nyc.gov/html/dot/downloads/misc/street-assessment-rating.zip")
    os.system("unzip street-assessment-rating.zip")
    os.system("rm street-assessment-rating.zip")
