from __future__ import print_function 
import json
import urllib2
import os
import sys
import csv

#'''file_name = sys.argv[0], apikey = sys.argv[1], Bus_line = sys.argv[2]'''
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: Python get_bus_info_yc3300.py <BUS_LINE><BUS_LINE>.csv")
    sys.exit()

Bus_Line = sys.argv[2]
file = sys.argv[3]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" +sys.argv[2]

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)



Bus_Count = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
Bus_Line = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']
print('Bus Line {}'.format(Bus_Line))


with open (file,'w') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(['Bus_Latitude','Bus_Longitude','Stop Name','Stop Status'])
    for i in range(Bus_Count):
        Bus_location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
        Bus_Longitude = Bus_location['Longitude']
        Bus_Latitude = Bus_location['Latitude']
        if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
            Stop_Name = 'N/A'
        else:
            Stop_Name=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
            Stop_Status = 'N/A'
        else:
            Stop_Status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            
        writer=csv.writer(csv_file)
        
        writer.writerow([Bus_Latitude,Bus_Longitude,Stop_Name,Stop_Status]) 