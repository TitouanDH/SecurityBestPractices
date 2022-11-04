#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP

source_interface = "Ethernet"
destination_ip = "192.168.80.81"

pck = Ether()/IP(dst=destination_ip, ttl=0)/ICMP()/Raw(b"X" * 500)
pck.show()
sendp(pck, iface=source_interface, loop=1)