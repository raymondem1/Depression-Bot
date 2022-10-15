import subprocess as sp
import re
import time
import overpass
import sys

cunty = ""

def gettingName():
    global cunty
    #open text file in read mode
    text_file = open("C:/Users/raymo/Downloads/cood/data.txt", "r")

    #read whole file to a string
    data = text_file.read()

    #close file
    text_file.close()

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

    #printing place
    print(cunty)

    print("done now, you whore")
    return cunty
