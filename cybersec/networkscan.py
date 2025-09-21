import scapy.all as scapy
import machine
import ipaddress
#Basic network scanner, returns info to the console
def netScan(network):
    request = scapy.ARP()

    request.pdst = network
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)
    return clients
#Scanner that returns a list of objects with IP and MAC info from the scan

def getSubnet(ip, cidr):
    network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
    return str(network)

