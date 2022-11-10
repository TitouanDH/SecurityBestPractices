#!venv/bin/python

from scapy.all import *
from scapy.contrib.lldp import *
from scapy.all import Ether
import binascii

"""
Advertising a fake AP via LLDP.
"""

source_interface = "Ethernet"
pck = Ether(dst="01:80:c2:00:00:0e")/LLDPDU()\
    /LLDPDUChassisID(subtype=4, id=b"38:f3:ab:59:2a:7e")\
    /LLDPDUPortID(subtype=3, id=b"38:f3:ab:59:2a:7e")\
    /LLDPDUTimeToLive(ttl=120)\
    /LLDPDUSystemCapabilities(mac_bridge_available=1, mac_bridge_enabled=1, wlan_access_point_available=1, wlan_access_point_enabled=1)\
    /LLDPDUGenericOrganisationSpecific(org_code=0x00120f, subtype=0x01, data=binascii.unhexlify("036c01001e"))\
    /LLDPDUEndOfLLDPDU(b"")

sendp(pck, iface=source_interface)

# Router
#/LLDPDUSystemCapabilities(mac_bridge_available=1,router_available=1, mac_bridge_enabled=1, router_enabled=1)\
# AP
#/LLDPDUSystemCapabilities(mac_bridge_available=1, mac_bridge_enabled=1, wlan_access_point_available=1, wlan_access_point_enabled=1)\
#IP PHONE
#/LLDPDUSystemCapabilities(telephone_available=1, telephone_enabled=1)\