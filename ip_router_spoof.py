#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP
import settings
"""
Just sending a packet spoofing router ip, in order to test spoofing protections.
"""


"IP SPOOF"
pck = Ether()/IP(src=settings.router, dst=settings.destination_ip)/ICMP()
sendp(pck, iface=settings.source_interface)