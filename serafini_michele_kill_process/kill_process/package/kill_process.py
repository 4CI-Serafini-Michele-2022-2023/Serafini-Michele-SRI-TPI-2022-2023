"""
kill_process.py
"""

import sys
from datetime import datetime
import platform
import psutil
import os


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
    print(current_user)
    for i in psutil.process_iter():
        print(i)
        sium = i.username().split("\\")
        if sium[1] == current_user:
            
            fog.write(DATA + ";" + str(platform.node()) + ";" +
            str(i.pid) + ";" + str(i.status()) + "\n")
            
        else:
            fo.write(DATA + ";" + str(platform.node()) + ";" +
            str(i.pid) + ";" + str(i.status()) + "\n")


def find_process_by_pid(pid):
    """
    Cerca un processo utilizzando il suo PID.
    Restituisce l'oggetto `psutil.Process` corrispondente se trovato,
    altrimenti restituisce `None`.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
    except psutil.NoSuchProcess:
        return None

def find_processes_by_name(name):
    """
    Cerca i processi utilizzando il loro nome.
    Restituisce una lista di oggetti `psutil.Process` corrispondenti
    a tutti i processi con il nome specificato.
    """
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == name:
            process.terminate()  # Termina il processo
            print(f"Processo {name} ({process.info['pid']}) terminato.")
            return  # Esce dalla funzione dopo aver terminato il primo processo corrispondente
    print(f"Nessun processo trovato con il nome {name}.")



if __name__ == "__main__":
    DATA = str(datetime.now())
    fog = open("../flussi/kill_process_user.csv", "a", encoding = "latin-1")
    fo = open("../flussi/kill_process_system.csv", "a", encoding = "latin-1")
    fogg = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    csv()
    print("inserisci il pid del processo da killare")
    process = find_process_by_pid(int(input()))
    print("inserisci il nome del processo da killare")
    processes = find_processes_by_name(str(input()))
    fog.close()
    fogg.close()
