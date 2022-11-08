#!venv/bin/python

from scapy.all import *
from scapy.contrib.lldp import *
from scapy.all import Ether
import binascii

"""
Advertising a switch/router via LLDP. To other switchs.
"""

source_interface = "Ethernet"

pck = Ether(dst="01:80:c2:00:00:0e")/LLDPDU()\
    /LLDPDUChassisID(subtype=4, id=b"e8:e7:32:cc:f7:69")\
    /LLDPDUPortID(subtype=3, id=b"e8:e7:32:cc:f7:69")\
    /LLDPDUTimeToLive(ttl=120)\
    /LLDPDUSystemCapabilities(mac_bridge_available=1,router_available=1, mac_bridge_enabled=1, router_enabled=1)\
    /LLDPDUGenericOrganisationSpecific(org_code=0x00120f, subtype=0x01, data=binascii.unhexlify("036c01001e"))\
    /LLDPDUEndOfLLDPDU(b"")

sendp(pck, iface=source_interface, loop=1)