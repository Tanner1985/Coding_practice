import scapy.all as scapy
import machine
import ipaddress
import multiprocessing
import time
MACHINELIST = []
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
    processes = []
    startTime = time.time()
    network = input('Please Enter the Network to scan: ')
    network = ipaddress.ip_network(network, strict=False)
    networkToScan = list(network.subnets(new_prefix=24))
    startPort = int(input('Please enter the start of the port range to scan for each machine: '))
    endPort = int(input('Please enter the end of the port range to scan for each machine: '))
    for element in networkToScan:
        numProcesses = 64
        with multiprocessing.Pool(processes=numProcesses) as pool:
            p = pool.map(autoNetScan, str(element),)
            processes.append(p)
    for process in processes:
        process.join()
    endTime = time.time()
    print(f'Scan completed in {endTime - startTime} seconds')
    for machine in MACHINELIST:
        machine.scanSavePorts(startPort, endPort)
    return MACHINELIST
            ##machine.scanSavePorts(startPort, endPort)
def autoNetScan(network):
    request = scapy.ARP()
    request.pdst = network
    broadcast = scapy.Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients:
            machine = createNewMachine(element[1].psrc, element[1].hwsrc)
            MACHINELIST.append(machine)

def createNewMachine(IP, MAC):
    return machine.Machine(IP, MAC)

def getSubnet(ip, cidr):
    network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
    return str(network)

