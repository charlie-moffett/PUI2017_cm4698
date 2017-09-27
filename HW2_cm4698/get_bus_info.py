# Author: charlie moffett, nyu cusp. 2017

# the following packages let me read line input arguments
import sys
import os


import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# sets the line input arguments to variables for string concatenation
key = sys.argv[1]
line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + line

# use the json.loads method to obtain a dictionary representation of the response string 
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# rejects any line input unless exactly 4 arguments are given
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: get_bus_info_cm4698.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

# allows me to write output to a CSV file
fout = open(sys.argv[3], "w")

# creates variable with core index that other variables will build off of
veh_act = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

buscount = len(veh_act)
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(buscount):
    Long = veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Lat = veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    stop_name = veh_act[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    stop_status = veh_act[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']
    # print(Lat, Long, stop_name, stop_status)
    fout.write("%s,%s,%s,%s\n" %(Lat, Long, stop_name, stop_status))
