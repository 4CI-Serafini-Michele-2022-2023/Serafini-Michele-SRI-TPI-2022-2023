"""
getprocess
"""
import time
import psutil
from utility.virustotal import virustotal
from utility.utility import logs, save


def processi():
    """
    salva le informazioni dei processi
    """
    process_list = []
    logs("Avvio processi")

    for proc in psutil.process_iter():
        try:
            if proc.name().endswith('.exe'):
                stringa = str(proc.exe() + "; " + proc.name() + "; "
                + str(proc.pid) + virustotal(proc.exe()))
                save("../../flussi/processi.csv", stringa)
                time.sleep(5)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            logs("Errore durante l'esecuzione della funzione processi()")
    for process in process_list:
        print(process)


if __name__ == "__main__":
    logs("Avvio programma")
    processi()
