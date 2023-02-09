"""
walk.py
"""

import os
import sys
from datetime import datetime
import platform
import wmi

def stampa():
    fo.write(str(properties.caption) + " " + str(properties.version) + "\n")

def att(root, file):
    stat1 = str(os.stat(os.path.join(root, file)).st_size)
    stat2 = str(os.stat(os.path.join(root, file)).st_mode)
    stat3 = str(os.stat(os.path.join(root, file)).st_atime)
    string = ("st_size" + stat1 + ";" + "st_mode" + stat2 + ";" + "st_atime" + stat3 + "\n")
    fog.write(string)
    
    
def trace():
    data = str(datetime.now())
    fogg.write(data + " " +  sys.platform + " " + str(platform.node()) + "\n")
    

if __name__ == "__main__":
    fo = open("../flussi/products.csv", "a", encoding = "latin-1")
    fog = open("../flussi/properties.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a")
    trace()
    cim = wmi.WMI()
    
    for properties in cim.Win32_Product():
        if(properties.InstallLocation == None):
            print("unknown path")
        else:
            print(properties.InstallLocation)
        print(str(properties.caption) + " " + str(properties.version) + "\n")
        stampa()
        est = str(properties.installLocation)
        if(est != (None)):
            for root, dirs, files in os.walk(str(properties.installLocation)):
                for file in files:
                    if(file.endswith(".exe")):
                        att(root, file)
    fo.close()
    fog.close()
    fogg.close()