# Author: charlie moffett, nyu cusp, 2017

import sys
import os


import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

key = sys.argv[1]
line = sys.argv[2]

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_cm4698.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Outputs the following to the console: bus name, # of vehicles, current position

# creates a variable that stores path to VehicleActivity in MTA JSON tree
veh_act = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# print the bus name
print("Bus Name: " + veh_act[0]['MonitoredVehicleJourney']['PublishedLineName'])

# print number of vehicles in the bus line
print("Number of Vehicles: " + str(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])))

# print the current position of each bus

buscount = len(veh_act)
for i in range(buscount):
    Long = veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Lat = veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']
    print("Bus " + str(i) + " is at latitude " + str(Lat) + " and longitude " + str(Long))


