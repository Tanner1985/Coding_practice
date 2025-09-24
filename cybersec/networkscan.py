import scapy.all as scapy
import machine
import ipaddress
#Basic network scanner, returns info to the console
def netScan(network):
    clients = []
    for subnet in getSubnets(network):
        request = scapy.ARP()
        request.pdst = subnet.network_address.exploded + '/16'
        broadcast = scapy.Ether()

        broadcast.dst = 'ff:ff:ff:ff:ff:ff'

        request_broadcast = broadcast / request
        clients.append(scapy.srp(request_broadcast, timeout = 1)[0])
        for element in clients:
            print (element)
            for item in element:
                print(item[1].psrc + "      " + item[1].hwsrc)
    return clients
#Scanner that returns a list of objects with IP and MAC info from the scan

def getSubnets(network):
    return list(ipaddress.ip_network(network).subnets(new_prefix=16))

