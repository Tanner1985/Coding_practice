#This is a complex trace route using scapy and saving to a graph
import scapy.all as scapy
import graphviz

def multiTrace():
    traceList = []
    moreTrace = 'Y'
    while moreTrace != 'N':
        target = input('Please enter the site or IP to trace to: ')
        traceList.append(target)
        moreTrace = input('Would you like to add more sites to trace? Y or N: ')
        moreTrace.upper()
    res, unans = scapy.traceroute(traceList, dport=[80,443],maxttl=20,retry=-2)
    res.graph(target = 'Graph')