import socket
def portScan():
    target = input('Please input target host: ')
    portStart = int(input('Please input the start of the port range: '))
    portEnd = int(input('Please enter the end of the port range: '))
    scan_ports(target, portStart, portEnd)
def scan_ports(target, startPort, endPort):
    for port in range(startPort, endPort + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f'Port{port}: Open')
            openport = True
        sock.close()
    if not openport:
        print('No open ports found')