from __future__ import print_function 
import json
import urllib2
import os
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: Python show_bus_location_yc330.py <BUS_LINE>")
    sys.exit()

Bus_Line = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" +sys.argv[2]

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


Bus_Count = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
Bus_Line = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']

print('Bus Line {}'.format(Bus_Line))
for i in range(Bus_Count):
    Bus_location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    Bus_Longitude = Bus_location['Longitude']
    Bus_Latitude = Bus_location['Latitude']
    print('Bus {} is at latitude {} and longitude {}'.format( i+1, Bus_Longitude, Bus_Latitude))
                                
