import networkscan
import portscan
import apirequester
import os
import sys
import subprocess
import targetIP
#This is the main module that elevates permissions and orginizes the flow of information
def main():
    if os.geteuid() !=0:
        print('Must be a sudo user, switching')
        runSudo()
    choice = 0
    print('Please pick an option')
    print('1: Network Scanner, scan an IP range for devices')
    print('2: Port Scanner, scan an IP and port range for open ports')
    print('3: API request, pull from an API and save JSON to text')
    print('4: Scan a Network and then each found machine for specific port ranges ')
    print('---------------------------')
    choice = int(input('Type your number of choice here: '))
    if choice == 1:
        networkscan.netScan()
    elif choice == 2:
        portscan.portScan()
    elif choice == 3:
        apirequester.apiRequest()
    elif choice == 4:
        networkList = networkscan.netScanSave()
        list = portscan.portScanAutomation(networkList)
        for targetIP in list:
            print(f'The IP {targetIP.getIP()} has the ports {targetIP.getOpenPorts()} open')
    else:
        print('Invalid option given')
#Function to escalate to sudo user, some things in this require permissions to function
def runSudo():
    args = ['sudo', 'python3'] + sys.argv
    os.execvp('sudo', args)

main()
