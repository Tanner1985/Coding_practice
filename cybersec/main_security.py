import networkscan
import trace
import portscan
import platform
import apirequester
import os
import sys
import subprocess
import machine
#This is the main module that elevates permissions and orginizes the flow of information
def main():
    if platform.system() == "Linux":
        if os.geteuid() != 0:
            print('Must be a sudo user, switching')
            runSudo()
    choice = getChoice()
    while choice !=0:
        if choice == 1:
            network = input('Please Enter the Network to scan: ')
            networklist = networkscan.netScan(network)
            choice = getChoice()
        elif choice == 2:
            portscan.portScan()
            choice = getChoice()
        elif choice == 3:
            apirequester.apiRequest()
            choice = getChoice()
        elif choice == 4:
            network = input('Please Enter the Network to scan: ')
            networkList = networkscan.netARPScan(network)
            print(networkList)
            for client in networkList:
                for item in client:
                    ip = item[1].psrc
                    mac = item[1].hwsrc
                    newMachine = createNewMachine(ip, mac)
                    print(f'Scanning {ip} for unsecure ports')
                    newMachine.scanUnsecurePorts()
                    print(f'Open ports for {ip} are: {newMachine.getOpenPorts()}')
            choice = getChoice()
        elif choice == 5:
            network = input('Please Enter the Network to scan: ')
            networkList = networkscan.scanICMP(network)
            choice = getChoice()
        elif choice == 6:
            network = input('Please Enter the Network to scan: ')
            networkList = networkscan.scanTCP(network)
            choice = getChoice()
        elif choice == 7:
            network = input('Please Enter the Network to scan: ')
            networkList = networkscan.pingARP(network)
            choice = getChoice()
        elif choice == 8:
            network = input('Please Enter the Network to scan: ')
            switch = input('Please enter MAC of target network device: ')
            networkList = networkscan.netARPCustomMac(network, switch)
            choice = getChoice()
        elif choice == 9:
            network = input('Please Enter the Network to scan: ')
            networkList = networkscan.UDPping(network)
            choice = getChoice()
        elif choice == 10:
            trace.multiTrace()
            choice = getChoice()
        else:
            print('Invalid option given')
            choice = getChoice()
    print('Exiting program')
#Function to escalate to sudo user, some things in this require permissions to function
def runSudo():
    args = ['sudo', 'python3'] + sys.argv
    os.execvp('sudo', args)

def getChoice():
    print('Please pick an option')
    print('---------------------------')
    print('0: Exit')
    print('1: Network Scanner, scan an IP range for devices using ARP')
    print('2: Port Scanner, scan an IP and port range for open ports')
    print('3: API request, pull from an API and save JSON to text')
    print('4: Scan a Network via ARP and then each found machines for specific port ranges ')
    print('5: Scan a network using ICMP')
    print('6: Scan a network using TCP')
    print('7: Scan a network using arping')
    print('8: ARP scan with specific MAC input')
    print('9: Scan using UDP')
    print('10: Trace route and print to graph')
    print('---------------------------')
    choice = int(input('Type your number of choice here: '))
    return choice

def createNewMachine(IP, MAC):
    thisMachine = machine.Machine()
    thisMachine.setIP = IP
    thisMachine.setMAC = MAC
    return thisMachine

main()
