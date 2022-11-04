#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP

source_interface = "Ethernet"
destination_ip = "10.130.7.253"

pck = Ether(src=RandMAC())/IP(dst=destination_ip)/ICMP()
pck.show()
sendp(pck, iface=source_interface, loop=1)