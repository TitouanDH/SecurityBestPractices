#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, ARP

source_interface = "Ethernet"
destination_ip = "10.130.7.253"
lan = "10.130.7.0/24"


pck = Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op=1,pdst=destination_ip ,psrc=RandIP(lan), hwdst="FF:FF:FF:FF:FF:FF")/Raw(b"X" * 20)
pck.show()
sendp(pck, iface=source_interface, loop=1)