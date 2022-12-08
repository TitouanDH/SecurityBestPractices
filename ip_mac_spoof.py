#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP
import settings
"""
Just sending a packet with different IP and MAC, in order to test spoofing protections.
"""


"IP SPOOF"
pck = Ether()/IP(src=settings.source_ip, dst=settings.destination_ip)/ICMP()
sendp(pck, iface=settings.source_interface)

"MAC SPOOF"
pck = Ether(src=settings.mac_source)/IP(dst=settings.destination_ip)/ICMP()
sendp(pck, iface=settings.source_interface)

"BOTH"
pck = Ether(src=settings.mac_source)/IP(src=settings.source_ip,dst=settings.destination_ip)/ICMP()
sendp(pck, iface=settings.source_interface)