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
        if ports not in self.__openPorts:
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
    def scanUnsecurePorts(self):
        unsecurePorts = [20,21,22,23,25,53,67,68,69,80,110,111,135,137,138,139,143,161,162,389,443,445,512,513,514,1099,2049,2121,3306,3389,5900,6000,6667,8080]
        for port in unsecurePorts:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.__IP, port))
            if result == 0:
                self.setOpenPorts(port)
            sock.close()