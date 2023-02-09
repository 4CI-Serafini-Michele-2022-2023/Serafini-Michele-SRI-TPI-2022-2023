"""
walk.py
"""

import os
import sys
from datetime import datetime
import platform
import wmi
import win32com.client    


def trace():
    data = str(datetime.now())
    fogg.write(data + " " +  sys.platform + " " + str(platform.node()) + "\n")

if __name__ == "__main__":

    fo = open("../flussi/win32.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a")
    wmi = win32com.client.GetObject("winmgmts://./root/cimv2")
    col_items = wmi.ExecQuery("SELECT * FROM Win32_Product")
    for item in col_items:
        fo.write(str(str(item.Caption)) + ";" + str(item.InstallDate) + ";" + str(item.Version) + "\n")      
    trace()
    fo.close()
    fogg.close()