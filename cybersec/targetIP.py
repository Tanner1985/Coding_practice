class TargetIP:
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