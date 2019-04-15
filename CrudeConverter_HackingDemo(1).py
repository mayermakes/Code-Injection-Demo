#!/usr/bin/python3
import os
import time

os.system("clear")
print(''' Crude .JPG to MP4 converter 0.1 / Code Injection Demo
_________________________________________________________________________
                           WARNING:
This piece of software is experimental and comes without any warranty.
DO NOT USE THIS ON ANY PRODUCTIVE OR CRITICAL SYSTEM. This is unsafe!
This tool can be used to demonstrate code injection!
Only for demonstrative purpose, any other use is strictly prohibited.
               DO NOT REMOVE THIS WARNING LABEL!
_________________________________________________________________________

              Published as Public Domain CC0 2019
_________________________________________________________________________
This file must be run in the same Folder the source .jpg files are located
_________________________________________________________________________
''')
print("Please enter: ")
fps = input("Framerate per second: ")
data = input("data format of input files(f.e.: image-%05d.jpg) : ")
file = input("output filename (f.e.: output.mp4 :")
try:
    os.system("ffmpeg -framerate " + str(fps)+ " -i "+ data + " -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p " + file)
except:
    print("invalid inputs")
time.sleep(3)
print("conversion finished")
