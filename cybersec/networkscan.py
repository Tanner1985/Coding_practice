import scapy.all as scapy

def main():
    network = input('Please Enter the Network to scan: ')
    request = scapy.ARP()

    request.pdst = network
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)

main()