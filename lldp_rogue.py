#!venv/bin/python

from scapy.all import *
from scapy.contrib.lldp import *
from scapy.all import Ether
import binascii
import settings
"""
Advertising a fake AP via LLDP.
"""

pck = Ether(dst=settings.mac_dest)/LLDPDU()\
    /LLDPDUChassisID(subtype=4, id=b"38:f3:ab:59:2a:7e")\
    /LLDPDUPortID(subtype=3, id=b"38:f3:ab:59:2a:7e")\
    /LLDPDUTimeToLive(ttl=120)\
    /LLDPDUSystemCapabilities(mac_bridge_available=1, mac_bridge_enabled=1, wlan_access_point_available=1, wlan_access_point_enabled=1)\
    /LLDPDUGenericOrganisationSpecific(org_code=0x00120f, subtype=0x01, data=binascii.unhexlify("036c01001e"))\
    /LLDPDUEndOfLLDPDU(b"")

sendp(pck, iface=settings.source_interface)

# Router
#/LLDPDUSystemCapabilities(mac_bridge_available=1,router_available=1, mac_bridge_enabled=1, router_enabled=1)\
# AP
#/LLDPDUSystemCapabilities(mac_bridge_available=1, mac_bridge_enabled=1, wlan_access_point_available=1, wlan_access_point_enabled=1)\
#IP PHONE
#/LLDPDUSystemCapabilities(telephone_available=1, telephone_enabled=1)\