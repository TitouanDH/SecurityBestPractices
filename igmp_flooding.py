#!venv/bin/python

from scapy.all import *
from scapy.contrib.igmp import IGMP

source_interface = "Ethernet"
destination_ip = "239.10.20.30"

pck = Ether()/IP(dst=destination_ip)/IGMP(type=22, gaddr=destination_ip)
pck.show()
sendp(pck, iface=source_interface, loop=1)