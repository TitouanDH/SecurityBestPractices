#!venv/bin/python

from scapy.all import *
from scapy.all import IP, Ether, Dot1Q
from scapy.contrib.ospf import *
import settings

'''
YOU CAN DIRECTLY MODIFY THE HEXA

import binascii
 ip_pkt = IP(src=settings.source_ip,dst=settings.destination_ip, ttl=1)/\
    OSPF_Hdr(type=4, src="10.88.88.254", area="0.0.0.0")/\
    OSPF_LSUpd(lsacount=1, lsalist=[\
    OSPF_BaseLSA(\
    binascii.unhexlify("000100050a6363000a5858fe8000000119300024ffffff00800000010000000000000000"))]) '''

# handmade
ip_pkt = IP(src=settings.source_ip,dst=settings.destination_ip, ttl=1)/\
    OSPF_Hdr(type=4, src="10.88.88.254", area="0.0.0.0")/\
    OSPF_LSUpd(lsacount=1, lsalist=[OSPF_External_LSA(id="10.99.99.0", adrouter="10.88.88.254", mask="255.255.255.0", ebit=1)])

ip_pkt.show()

dot1_tags = Ether()
for vlan_id in settings.vlans:
    dot1_tags = dot1_tags/Dot1Q(vlan=vlan_id)

sendp(dot1_tags/ip_pkt, iface=settings.source_interface)