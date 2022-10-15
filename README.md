# Depression-Bot
This is a robot that uses open street maps to find the nearest lake and try to go in it...He also gets frustrated when there's an obstacle in the way.

If this doesn't look all fancy and nice yet, I am busy atm working on another video for next week or posting this current video. If you come back later today it'll look real good and fancy. I give a super fast summary of the code now.

First get current gps coordinates from your local powershell

Then add and subtract to that to make a bounding box, send that to open street maps to find name of nearby lake

filter through some txt files twice because I suck

Get gps coorinates from name of lake

get angle between robot gps coordinates and lake coordinates

Send that to serial monitor 

(Add stupid thing for fun, every minute he will say a sad fact about the world...need to add more facts)

from there arduino code is in charge

There we just save that variable and keep the motors in range (there is an issue I will explain later but it works for the most part)

if uv sensor gets something in range (3 or less) then break the loop and send back to the python script by the seriall monitor to have it say the complaining voice line.

Will elaborate and make this nicer soon


