# Author: charlie moffett, nyu cusp. 2017

import sys
import os


import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: get_bus_info_cm4698.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()



fout = open(sys.argv[1], "w")

veh_act = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

buscount = len(veh_act)
for i in range(buscount):
    Long = veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Lat = veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    stop_name = veh_act[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    stop_status = veh_act[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    veh_act[i]['MonitoredVehicleJourney']['VehicleLocation']
    # print(Lat, Long, stop_name, stop_status)
    fout.write("%s,%s,%s,%s\n" %(Lat, Long, stop_name, stop_status))
