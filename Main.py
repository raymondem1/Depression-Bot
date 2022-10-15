import subprocess as sp
import re
import time
import overpass
import sys
import geojson
from pandas import json_normalize
import requests
from dateTransfer import gettingName
from dateTransfer import cunty
from codecs import latin_1_decode
import math
from geopy.geocoders import Nominatim
import pyproj
from operator import truediv
from playsound import playsound
import time
import serial
import winsound
ser = serial.Serial('COM3', 9600, timeout=0.1)

loopadoop = 0

sadfact = 0




#ser.timeout = 1
time.sleep(1)

#playing sound
winsound.PlaySound("pain.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


#This is the correct method
wt = 0 # Wait time -- I purposefully make it wait before the shell command
accuracy = 3 #Starting desired accuracy is fine and builds at x1.5 per loop

# Getting the coordinates
pshellcomm = ['powershell']
pshellcomm.append('add-type -assemblyname system.device; '\
                      '$loc = new-object system.device.location.geocoordinatewatcher;'\
                      '$loc.start(); '\
                      'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) '\
                      '{start-sleep -milliseconds 100}; '\
                      '$acc = %d; '\
                      'while($loc.position.location.horizontalaccuracy -gt $acc) '\
                      '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; '\
                      '$loc.position.location.latitude; '\
                      '$loc.position.location.longitude; '\
                      '$loc.position.location.horizontalaccuracy; '\
                      '$loc.stop()' %(accuracy))

p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)
(out, err) = p.communicate()
out = re.split('\n', out)

lat = float(out[0])
long = float(out[1])
radius = int(out[2])
a = lat, long

print(a)

print("Coordinates done")

#Data placing (finding the nearset lake and puttin it into the txt doc)

print("finding lake")

#converting the things to floats

lat1 = float(lat)
long1 = float(long)

print("testingthese bitches")

print(lat1)
print(long1)

#addingto get the bounding box

#0.118
lat2 = lat1 + 0.118
long2 = long + 0.118
print(lat2)
print(long2)

long1 = str(long1)
long2 = str(long2)
lat1 = str(lat1)
lat2 = str(lat2)


#min lattitude, min longitude, max lattitude, max longitude
url = 'http://overpass-api.de/api/interpreter'  # Overpass API URL


query = f"""
    [out:json];
    way ["natural"="water"]
    ("""+lat1+""", """+long2+""", """+lat2+""", """+long2+""");
    out;
"""
r = requests.get(url, params={'data': query})
data = r.json()['elements']  # read response as JSON and get the data
df = json_normalize(data) 
f=open("data.txt", "w+", encoding="utf-8")
geojson.dump(data,f)
#f.write(str(data))
print("Finished placing the date in first txt doc")

time.sleep(5)
e= str(data)

subStr = re.search(r'name(.+?),',e)
a= str(subStr)
print(a.encode("utf-8"))
print("doing it man")

other = re.search(r'\'(.+?),',a)

print(other)
bitch = str(other)
with open('FinalName.txt', 'w') as foo:
    foo.write(bitch)

with open("FinalName.txt","r") as edd:
    cunt = edd.read()

finder = cunt.find('": "')
finder2 = cunt.find(""" ",' """)

print("Substring found at index:", finder, finder2)

print(finder)

finder+=4
finder2-=3

print(finder)
print(finder2)

cunty = cunt[finder:finder2]
print(cunty)

finder3 = cunty.find(": '")
length = len(cunty)
finderLast = length

finder3+=3

print(finder3)
print(finderLast)

cunty = cunty[finder3:finderLast]
#printing place
print(cunty)

#Now we get the coordinates of the lake

loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode("Brandy lake")
 
# printing address
print(getLoc.address)

#printing latitude and longitude
print("Latitude = ", getLoc.latitude)
print("Longitude = ", getLoc.longitude)

geodesic = pyproj.Geod(ellps='WGS84')
fwd_azimuth,back_azimuth,distance = geodesic.inv(long1, lat1, long2, lat2)

if(fwd_azimuth<0):
    angle = 360 + fwd_azimuth
if(fwd_azimuth>0):
    angle = 360 - fwd_azimuth

angle = math.floor(angle*100)/100

print(angle)

finalAngle = str(angle)

ser.write(finalAngle.encode('utf-8'))
winsound.PlaySound("finding.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

#ser.write(finalAngle.encode('utf-8'))

#testing = str(angle)

#print(testing)

#ser.write(testing.encode('utf-8'))
#ser.write(finalAngle.encode('utf-8'))

time.sleep(2)

while(loopadoop ==0):
    read= str(ser.readline(ser.inWaiting()))
    print(read)
    if("0" in read or "1" in read or "2" in read or "3" in read):
        sadfact = 42
        print("play end now")
        #playsound('C:/Users/raymo/Downloads/cood/end.wav')
        playsound('C:/Users/raymo/Downloads/cood/die.wav')
        #PlaySound("end.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        loopadoop=1
    if(sadfact%300 ==0 and sadfact >0):
        winsound.PlaySound("sad1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    sadfact+=1  
    time.sleep(.2)