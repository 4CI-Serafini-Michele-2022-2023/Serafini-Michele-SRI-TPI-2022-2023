"""
mac.py
"""

import subprocess
import platform
import sys
from datetime import datetime
from icecream import ic

def change_mac_linux(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def change_mac_windows(interface, new_mac):
    subprocess.call(["reg", "add", "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E972-E325-11CE-BFC1-08002BE10318}\\%s" % interface, "/v", "NetworkAddress", "/d", new_mac, "/f"])
    subprocess.call(["netsh", "interface", "set", "interface", "name=%s" % interface, "admin=disable"])
    subprocess.call(["netsh", "interface", "set", "interface", "name=%s" % interface, "admin=enable"])

def main(interface, new_mac):
    operating_system = platform.system()
    if operating_system == "Linux":
        change_mac_linux(interface, new_mac)
    elif operating_system == "Windows":
        change_mac_windows(interface, new_mac)
    else:
        ic("Unsupported operating system.")

main("eth0", "00:11:22:33:44:55")

def trace():
    """
    creare file trace.log con data, piattaforma e nome della macchina
    """
    log.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")

if __name__ == '__main__':
    DATA = str(datetime.now())
    main()
    log = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    log.close()