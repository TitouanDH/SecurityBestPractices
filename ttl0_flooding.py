#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, Dot1Q, IP, ICMP

source_interface = "Ethernet"
destination_ip = "192.168.80.81"

data_size = 500


pck = Ether()/IP(dst=destination_ip, ttl=0)/ICMP()/Raw(b"X" * data_size)
pck.show()
sendp(pck, iface=source_interface, loop=1)