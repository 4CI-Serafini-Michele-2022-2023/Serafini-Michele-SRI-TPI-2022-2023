import csv
import os
import platform
import subprocess
import threading

def ping_host(host):
    if platform.system() == 'Windows':
        command = ['ping', '-n', '1', host]
    elif platform.system() == 'Linux':
        command = ['ping', '-c', '1', host]
    else:
        print(f"Sistema operativo non supportato per l'host {host}")
        return

    result = subprocess.run(command, capture_output=True)
    output = result.stdout.decode('utf-8')
    if platform.system() == 'Windows' and "Risposta" in output:
        print(f"{host} è raggiungibile.")
    elif platform.system() == 'Linux' and "1 received" in output:
        print(f"{host} è raggiungibile.")
    else:
        print(f"{host} non è raggiungibile.")

def ping_hosts(hosts):
    threads = []
    for host in hosts:
        thread = threading.Thread(target=ping_host, args=(host,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    csv_file = 'input.csv'
    hosts = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                hosts.append(row[0])

    ping_hosts(hosts)

if __name__ == '__main__':
    main()