"""
getconfrete.py
"""


import platform
import ifcfg
from utilities.utility import first_line, log, save


def linux_nic():
    """
    funzione per ottenere e salvare
    le informazioni dal sistema operativo
    Linux
    """

    for name, interface in ifcfg.interfaces().items():
        out = name + ";"
        out += str(interface['ether']) + ";"
        out += str(platform.node()) + ";"
        for j in interface['inet4']:
            out += str(j)
        out += ";"
        for j in interface['inet6']:
            out += str(j)
        out += ";"
        save("../flussi/getconfrete.csv",log() + out)


def windows_nic():
    """
    funzione per ottenere e salvare le
    informazioni dal sistema operativo
    Windows
    """

    wim  = win32com.client.GetObject(r"winmgmts:\\.\root\cimv2")
    nic =  "SELECT * FROM  Win32_NetworkAdapterConfiguration where ipenabled = 'true'"
    coll_items = wim.ExecQuery(nic)
    for  item  in coll_items:
        out = item.caption + ";"
        out += str(item.macaddress) + ";"
        out += str(platform.node()) + ";"
        out += str(item.ipaddress[0]) + ";"
        out += str(item.ipaddress[1]) + ";\n"
        save("../flussi/getconfrete.csv", log() + out)


if __name__=="__main__":
    save("../log/trace.log",log() + "\n")
    F_LINE = "timestamp;timestamp-user-friendly;computername;sistemaoperativo;"
    F_LINE += "nomeschedarete;macaddress;hostname;inet4;inet6;\n"
    first_line("../flussi/getconfrete.csv", F_LINE)
    if platform.system() == "Windows":
        import win32com.client
        windows_nic()
    else:
        linux_nic()
