#!venv/bin/python

from scapy.all import *

source_interface = "ens192"
destination_ip = "192.168.80.81"

data_size = 500


pck = Ether()/IP(dst=destination_ip, ttl=0)/ICMP()/Raw(b"X" * data_size)
pck.show()
sendp(pck, iface=source_interface, loop=1)