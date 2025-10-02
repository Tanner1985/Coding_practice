import scapy.all as scapy
import machine
import ipaddress
#Scanner that returns a list of objects with IP and MAC info from the scan using ARP
def netARPScan(network):
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
def scanICMP(network):
    clients = []
    for subnet in getSubnets(network):
        request = scapy.ICMP()
        request.pdst = subnet.network_address.exploded + '/16'
        broadcast = scapy.Ether()

        broadcast.dst = 'ff:ff:ff:ff:ff:ff'

        requestBroadcast = broadcast / request
        clients.append(scapy.srp(requestBroadcast, timeout = 1600)[0])
        for element in clients:
            print (element)
def scanTCP(network):
    clients = []
    for subnet in getSubnets(network):
        request = scapy.TCP(sport=666,flags="FPU")
        request.pdst = subnet.network_address.exploded + '/16'
        broadcast = scapy.Ether()

        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
        requestBroadcast = broadcast / request
        clients.append(scapy.srp(requestBroadcast, timeout = 1600)[0])
        for element in clients:
            print (element)
def pingARP(network):
    scapy.arping(network)

def UDPping(network):
        clients = []    
        request = scapy.UDP(dport=0)
        request.pdst = network
        broadcast = scapy.Ether()

        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
        requestBroadcast = broadcast / request
        clients.append(scapy.srp(requestBroadcast, timeout = 1600)[0])
        for element in clients:
            print (element)


def netARPCustomMac(network, switch):
    clients = []
    for subnet in getSubnets(network):
        request = scapy.ARP()
        request.pdst = subnet.network_address.exploded + '/16'
        broadcast = scapy.Ether()

        broadcast.dst = switch

        request_broadcast = broadcast / request
        clients.append(scapy.srp(request_broadcast, timeout = 1)[0])
        for element in clients:
            print (element)
            for item in element:
                print(item[1].psrc + "      " + item[1].hwsrc)
    return clients

def getSubnets(network):
    return list(ipaddress.ip_network(network).subnets(new_prefix=16))

