"""inizio"""
import platform
from getprocess.getprocess import processi
from getprocess.utility import logs
from confrete.getconfrete import windows_nic, linux_nic


def start():
    """test"""
    try:
        processi()
        if platform.system() == "Windows":
            windows_nic()
        else:
            linux_nic()
    except:
        logs("Errore nell avvio dei due programmi")
        pass

if __name__ == "__main__":
    logs("Avvio dei programmi")
    start()
