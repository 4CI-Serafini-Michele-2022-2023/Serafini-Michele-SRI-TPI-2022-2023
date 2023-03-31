"""
usbd.py
"""

import sys
from datetime import datetime
import platform
import csv 


def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    tracee.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")


def f_csv():
    with open("../flussi/input.csv", "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            column1 = row[0]
            column5 = row[5]
            csvv.write(column1 + ";" + column5 + "\n")

if __name__ == "__main__":
    DATA = str(datetime.now())
    f = '../flussi/proto.xml'
    csvv = open("../flussi/proto.csv", "a", encoding = "latin-1")
    tracee = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    f_csv()
    #choice = int(input("Scegli come salvare il tutto 1(xml)  2(database)  3(csv)  4(salvare su tutti e tre i formati): "))
    #if choice == 1:
    # xml(f)

    #elif choice == 2:
    #    db()
    #elif choice == 3:
    #    csv()
    #elif choice == 4:
    #    xml(f)
    #    db()
    #    csv()
    #else:
     #   print("Scelta non valida")

    csvv.close()
    tracee.close()
