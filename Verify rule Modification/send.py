#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP
import random


def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break
    if not iface:
        print ("Cannot find eth0 interface")
        exit(1)
    return iface

def main():

    if len(sys.argv)<2:
        print( 'pass 1 arguments: <destination>')
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()
    #srcport=[8008, 8009, 8000, 16119, 53, 21, 22, 23, 81, 554, 631, 943, 3910, 3911, 4070, 4071, 4520, 5001, 5002, 5080, 5555, 6668, 7888, 8008, 8009, 8554,9000, 9001, 8008, 8009, 8000, 16119, 53, 21, 22, 23, 81, 554, 631, 943, 3910, 3911, 4070, 4071, 4520, 5001, 5002, 5080, 5555, 6668, 7888, 8008, 8009, 8554,9000, 9001]
    #length=[54, 1000, 520, 64, 70, 80, 1420, 1148, 1268, 147, 157, 178, 200, 300, 54, 55, 56, 54, 54, 54, 1420, 240, 340, 370, 331, 444, 222, 666, 888, 224, 228, 229, 450, 250, 650, 850, 750, 252, 452, 852, 780, 54, 64, 74, 84, 94, 104, 204, 304, 404, 504, 704, 804, 904, 1004, 1104, 1204, 1304, 1404, 56, 76, 86, 96, 99, 100, 110, 125, 150]
    sno=0
    for i in range (0, 2500):
        srcport = random.randint(4000,5000)
        dstport = random.randint(4000,5000)
        n = random.randint(54,500)
        print "sending on interface %s to %s" % (iface, str(addr))
        pkt =  Ether(src=get_if_hwaddr(iface),dst = "00:00:0a:00:01:0a")
        pkt = pkt /IP(dst=addr, tos=1, flags=1, proto=6)
        pkt = pkt /UDP(sport = srcport, dport= dstport)
        myString = "z"*(n - 40)
        pkt = pkt/myString
        #pkt = pkt/"https://amazonecho.com/amazonecho"
        pkt.show2()
        sendp(pkt, iface=iface, verbose=False)
        time.sleep(0.1)
    
            #print "sending on interface %s to %s" % (iface, str(addr))
            #pkt =  Ether(src=get_if_hwaddr(iface),dst = "00:00:0a:00:01:05")
            #pkt = pkt /IP(dst=addr, tos=int(sys.argv[2]), flags=0, proto=6)
            #pkt = pkt /TCP(sport = srcport, dport= dstport, flags="A")
            #myString = "z"*(n - 40)
            #pkt = pkt/myString
            #pkt = pkt/"https://amazonecho.com/amazonecho"
            #pkt.show2()
            #sendp(pkt, iface=iface, verbose=False)



if __name__ == '__main__':
    main()