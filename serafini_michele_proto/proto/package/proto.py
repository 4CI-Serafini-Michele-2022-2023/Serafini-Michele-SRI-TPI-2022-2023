"""
usbd.py
"""

import sys
from datetime import datetime
import platform
import sqlite3
from lxml import etree as et


def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    fogg.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")


def xml(f):
    """
    salvare le info dei processi sul file XML
    """
   


def db():
    """
    salvare le info dei processi su un database
    """
  


def csv():
    KeyError


if __name__ == "__main__":
    DATA = str(datetime.now())
    f = '../flussi/evt.xml'
    fog = open("../flussi/evt.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    choice = int(input("Scegli come salvare il tutto 1(xml)  2(database)  3(csv)  4(salvare su tutti e tre i formati): "))
    if choice == 1:
     xml(f)

    elif choice == 2:
        db()
    elif choice == 3:
        csv()
    elif choice == 4:
        xml(f)
        db()
        csv()
    else:
        print("Scelta non valida")

    fog.close()
    fogg.close()
