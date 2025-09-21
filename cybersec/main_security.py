import networkscan
import portscan
import apirequester
import os
import sys
import subprocess
import machine
#This is the main module that elevates permissions and orginizes the flow of information
def main():
    if os.geteuid() !=0:
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
            networkList = networkscan.netScan(network)
            print(networkList)
            for client in networkList:
                ip = client[1].psrc
                mac = client[1].hwsrc
                newMachine = createNewMachine(ip, mac)
                print(f'Scanning {ip} for unsecure ports')
                newMachine.scanUnsecurePorts()
                print(f'Open ports for {ip} are: {newMachine.getOpenPorts()}')
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
    print('1: Network Scanner, scan an IP range for devices')
    print('2: Port Scanner, scan an IP and port range for open ports')
    print('3: API request, pull from an API and save JSON to text')
    print('4: Scan a Network and then each found machines for specific port ranges ')
    print('---------------------------')
    choice = int(input('Type your number of choice here: '))
    return choice

def createNewMachine(IP, MAC):
    return machine.Machine(IP, MAC)

main()
