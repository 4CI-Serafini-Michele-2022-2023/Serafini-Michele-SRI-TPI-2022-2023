"""
ping.py
"""
import csv
import platform
import subprocess
import threading
from icecream import ic

def ping_host(host):
    """
    Questa funzione esegue il ping dell'host in base al sistema operativo usato
    """
    if platform.system() == 'Windows':
        command = ['ping', '-n', '1', host]
    elif platform.system() == 'Linux':
        command = ['ping', '-c', '1', host]
    else:
        ic("Sistema operativo non supportato per l'host" + host)
        return

    result = subprocess.run(command, capture_output=True, check=True)
    output = result.stdout.decode('utf-8')
    if platform.system() == 'Windows' and "Risposta" in output:
        ic(host +"è raggiungibile")
    elif platform.system() == 'Linux' and "1 received" in output:
        ic(host + "è raggiungibile")
    else:
        ic(host + "non è raggiungibile")

def thread(hosts):
    """
    Questa funzione crea un thread per ogni host su cui eseguire il ping
    """
    threads = []
    for host in hosts:
        thread = threading.Thread(target=ping_host, args=(host,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    """
    Questa funzione legge tutte le righe della prima colonna del file di input
    """
    csv_file = 'input.csv'
    hosts = []

    with open(csv_file, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                hosts.append(row[0])

    thread(hosts)

if __name__ == '__main__':
    main()
