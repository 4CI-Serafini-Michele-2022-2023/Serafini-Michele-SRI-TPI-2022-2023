"""
usbd.py
"""

import sys
from datetime import datetime
import platform
import psutil
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
    for i in psutil.process_iter():
        fog.write(DATA + ";" + str(platform.node()) + ";" +
        str(i.pid) + ";" + str(i.status()) + "\n")


if __name__ == "__main__":
    DATA = str(datetime.now())
    fog = open("../flussi/kill_process.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    csv()
    fog.close()
    fogg.close()
