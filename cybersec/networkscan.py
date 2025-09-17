import scapy.all as scapy
import machine
#Basic network scanner, returns info to the console
def netScan():
    network = input('Please Enter the Network to scan: ')
    request = scapy.ARP()

    request.pdst = network
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)
#Scanner that returns a list of objects with IP and MAC info from the scan
def netScanSave():
    machineList = []
    network = input('Please Enter the Network to scan: ')
    startPort = int(input('Please enter the start of the port range to scan for each machine: '))
    endPort = int(input('Please enter the end of the port range to scan for each machine: '))
    request = scapy.ARP()

    request.pdst = network
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients:
        machine = createNewMachine(element[1].psrc, element[1].hwsrc)
        machineList.append(machine)
        machine.scanSavePorts(startPort, endPort)
    return machineList
def createNewMachine(IP, MAC):
    return machine.Machine(IP, MAC)

