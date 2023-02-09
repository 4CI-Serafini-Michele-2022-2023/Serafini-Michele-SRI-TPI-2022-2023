'''
getconfrete
'''

import sys
from datetime import datetime
import platform
import ifcfg
from icecream import ic


def trace():
    '''funzione per il trace.log'''
    fog.write(DATA + " " +  sys.platform + " " + str(platform.node()) + "\n")



if __name__ == "__main__":
    DATA = str(datetime.now())
    fo = open("../flussi/confrete.csv", "a", encoding = "latin-1")
    fog = open("../log/trace.log", "a", encoding = "latin-1")
    trace()
    for name, interface in ifcfg.interfaces().items():
        ic(interface)
        fo.write("nome:" + name + ";" + "ind_ipv4" + str(interface["inet4"])
        + ";" + "netmask" + str(interface["netmasks"])
        + ";" + "mac address" + str(interface["ether"])
        + ";" + "ind_ipv6" +  str(interface["inet6"]) + ";" + DATA + ";" +  sys.platform
        + ";" + str(platform.node()) + "\n")
    fo.close()
