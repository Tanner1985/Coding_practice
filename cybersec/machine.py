import socket
import multiprocessing
class Machine:
    def __init__(self, IP, MAC):
        self.__IP = IP
        self.__MAC = MAC
        self.__openPorts = []
    def setIP(self, IP):
        self.__IP = IP
    def setMAC(self, MAC):
        self.__MAC = MAC
    def setOpenPorts(self, ports):
        self.__openPorts.append(ports)
    def getIP(self):
        return self.__IP
    def getMAC(self):
        return self.__MAC
    def getOpenPorts(self):
        return self.__openPorts
    def scanPorts(self, startPort, endPort):
        for port in range(startPort, endPort + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.__IP, port))
            if result == 0:
                self.setOpenPorts(port)
            sock.close()