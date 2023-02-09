"""
usbd.py
"""


import os
import platform
from datetime import datetime

def first_line(file, stringa):
    """
    funzione per controllare se
    un file esiste, così da
    sapere quando è necessaria
    la riga introduttiva
    """

    if not os.path.isfile(file):
        save(file, stringa)


def save(path, stringa):
    """
    funzione per salvare all'interno di
    un file una stringa e scrivere nel csv i Processi,Pid
    """

    if not os.path.isfile(path):
        with open(path, "w",  encoding = "utf-8") as f_o:
            f_o.write("Percorso" ";" + "Processo" + ";" + "Pid" + "\n")
            f_o.close()
    with open(path, "a", encoding = "utf-8") as f_o:
        f_o.write(stringa + "\n")
        f_o.close()


def logs(stringa):
    """
    funzione per prendere le
    informazioni rigurdanti ogni
    esecuzione del programma
    """

    data = (datetime.now())
    unix_data = str(datetime.timestamp(data))
    data = str(data)
    node = str(platform.node())
    platf = str(platform.system())
    out = unix_data + ";" + data + ";" + node + ";" + platf + ";" + stringa
    return out

if __name__=="__main__":
    save("../../log/utility_trace.log", logs("test"))
