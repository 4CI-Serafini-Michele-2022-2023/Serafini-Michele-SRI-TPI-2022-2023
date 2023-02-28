"""
usbd.py
"""

import sys
from datetime import datetime
import platform
import sqlite3
import win32evtlog
import xml.etree.ElementTree as et

#win32_NTLogEvent

def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    fogg.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")


def xml(f):
    """
    salvare le info dei processi sul file XML
    """
    style = xml.ProcessingInstruction("stile.css", 
    text = 'type="text/css" href="../stile.css"')
    root.addprevious(style)
    server = None
    logtype = "Security" 
    open = win32evtlog.OpenEventLog(server, logtype)
    contrario = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(open, contrario, 0)
    total = win32evtlog.GetNumberOfEventLogRecords(open)
    root = et.Element("events")
    for x in range(total):
        for event in events:
            event_xml = et.SubElement(root, "event")
            et.SubElement(event_xml, "event_category").text = str(event.EventCategory)
            et.SubElement(event_xml, "time").text = str(event.TimeGenerated)
            et.SubElement(event_xml, "name").text = str(event.ComputerName)
            tree = et.ElementTree(root)
        tree.write(f)


def db():
    """
    salvare le info dei processi su un database
    """
    server = None
    logtype = "Security" 
    open = win32evtlog.OpenEventLog(server, logtype)
    contrario = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(open, contrario,0)
    total = win32evtlog.GetNumberOfEventLogRecords(open)

    database = sqlite3.connect("../flussi/evt.db")
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS evt (name, Last_access, Category_event)")
    for x in range(total):
        for event in events:
            cursor.execute("INSERT INTO evt (name, Last_access, Category_event) VALUES (?, ?, ?)",
            (event.ComputerName, str(event.TimeGenerated), event.EventCategory))
            database.commit()
        database.close()


def csv():
    server = None
    logtype = "Security"

    open = win32evtlog.OpenEventLog(server, logtype)
    contrario = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(open, contrario, 0)
    total = win32evtlog.GetNumberOfEventLogRecords(open)

    for x in range(total):
        for event in events:
            fog.write("Nome: " + str(event.ComputerName) + ";  " + "Ultimo accesso: " + str(event.TimeGenerated) + ";  " +
            "Event category: " + str(event.EventCategory) + "\n")


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
