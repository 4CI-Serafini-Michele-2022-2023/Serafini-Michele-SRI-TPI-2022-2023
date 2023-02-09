"""
usbd.py
"""

import sys
from datetime import datetime
import platform 
import psutil


def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    fogg.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")
    
    
def monitor_proc():
    """
    creare file ps.csv che conterrà il timestamp, nome della macchina,
    nome processo, stato del processo e la sua data di creazione
    """
    for i in psutil.process_iter():
        fog.write(DATA + ";" + str(platform.node()) + ";" +
        str(i.name()) + ";" + str(i.status()) + ";" + str(i.create_time()) + "\n")


if __name__ == "__main__":
    DATA = str(datetime.now())
    fog = open("../flussi/ps.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    monitor_proc()
    fog.close()
    fogg.close()
