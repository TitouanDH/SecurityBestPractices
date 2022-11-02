#!venv/bin/python

from scapy.all import *

source_interface = "ens192"

source_vlan = 0 # 0 or vlan number
destination_vlan = 80

destination_ip = "192.168.80.81"

pck = Ether()/Dot1Q(vlan=source_vlan)/Dot1Q(vlan=destination_vlan)/IP(dst=destination_ip)/ICMP()
pck.show()
sendp(pck, iface=source_interface)