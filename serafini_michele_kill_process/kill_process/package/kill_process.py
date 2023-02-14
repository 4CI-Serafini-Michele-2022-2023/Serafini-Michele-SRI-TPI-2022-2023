"""
usbd.py
"""

import sys
from datetime import datetime
import platform
import psutil
import os
import xml.etree.ElementTree as et


def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    fogg.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")
    
    
def csv():
    """
    creare file ps.csv che conterrà il timestamp, nome della macchina,
    nome processo, stato del processo e la sua data di creazione
    """
    current_user = os.getlogin()
    for i in psutil.process_iter(['username']):
        if i.info['username']=="SYSTEM":
            fo.write(DATA + ";" + str(platform.node()) + ";" +
            str(i.pid) + ";" + str(i.status()) + "\n")
            print(i.pid)
        elif i.info['username'] == current_user:
            fog.write(DATA + ";" + str(platform.node()) + ";" +
            str(i.pid) + ";" + str(i.status()) + "\n")


if __name__ == "__main__":
    DATA = str(datetime.now())
    fog = open("../flussi/kill_process_user.csv", "a", encoding = "latin-1")
    fo = open("../flussi/kill_process_system.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    csv()
    fog.close()
    fogg.close()
