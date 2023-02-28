"""
usbd.py
"""

import sys
from datetime import datetime
import platform
import sqlite3
import win32com.client
import xml.etree.ElementTree as et


def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    fogg.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")


for item in wmi.ExecQuery("select * FROM Win32_Group"):
    print(item)




if __name__ == "__main__":
    DATA = str(datetime.now())
    f = '../flussi/evt.xml'
    fog = open("../flussi/evt.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    fog.close()
    fogg.close()
