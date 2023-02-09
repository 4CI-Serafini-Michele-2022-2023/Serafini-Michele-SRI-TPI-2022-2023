"""
usbd.py
"""

import sqlite3
import sys
from datetime import datetime
import platform
import xml.etree.ElementTree as et
import time
import psutil
from tqdm import tqdm


def barra():
    for i in tqdm(range(100)):
        time.sleep(0.002)


def db():
    """
    salvare le info dei processi su un database
    """
    database = sqlite3.connect("../flussi/process.db")
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS processes (name, status, create_time)")
    for proc in psutil.process_iter():
        cursor.execute("INSERT INTO processes (name, status, create_time) VALUES (?, ?, ?)",
         (proc.name(), proc.status(), proc.create_time()))
        database.commit()
    database.close()


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
        str(i.name()) + ";" + str(i.status()) + ";" + str(i.create_time()) + "\n")


def xml(f):
    """
    salvare le info dei processi sul file XML
    """
    root = et.Element("ProcessList")
    for process in psutil.process_iter():
        name = str(process.name())
        status = str(process.status())
        date = str(process.create_time())

        nome_proc = et.Element("nome_proc")
        root.append(nome_proc)
        nome = et.SubElement(nome_proc, "name")
        nome.text = name

        status_proc = et.Element("status_proc")
        stato = et.SubElement(nome_proc, "status")
        stato.text = status

        create_time_proc = et.Element("create_time_proc")
        data = et.SubElement(nome_proc, "data_creazione")
        data.text = date

        tree = et.ElementTree(root)
        tree.write(f)

if __name__ == "__main__":
    DATA = str(datetime.now())
    fog = open("../flussi/process.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    f = '../flussi/process.xml'
    trace()
    choice = int(input("Scegli come salvare il tutto (1(xml)  2(database)  3(csv))  4(salvare su tutti e tre i formati): "))
    if choice == 1:
        xml(f)
        barra()
    elif choice == 2:
        db()
        barra()
    elif choice == 3:
        csv()
        barra()
    elif choice == 4:
        xml(f)
        db()
        csv()
        barra()
    else:
        print("Scelta non valida")
    fog.close()
    fogg.close()
