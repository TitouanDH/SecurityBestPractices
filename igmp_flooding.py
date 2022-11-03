#!venv/bin/python

from scapy.all import *
from scapy.contrib.igmp import IGMP

source_interface = "ens192"
destination_ip = "192.168.80.81"

data_size = 500


pck = Ether()/IP(dst=destination_ip)/IGMP()
pck.show()
sendp(pck, iface=source_interface)