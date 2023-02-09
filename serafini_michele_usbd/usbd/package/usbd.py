"""
usbd.py
"""

import os
import sys
from datetime import datetime
import platform


def trace():
    data = str(datetime.now())
    fogg.write(data + " " +  sys.platform + " " + str(platform.node()) + "\n")
    

if __name__ == "__main__":
    fog = open("../flussi/usbd2.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a")
    trace()
    with open("../flussi/usbd.csv", "r", encoding="latin-1") as filecsv:
        linea = filecsv.readlines()
        for line in linea:
            if "HID" not in line:
                fog.write(line)
    
    fog.close()
    fogg.close()
   