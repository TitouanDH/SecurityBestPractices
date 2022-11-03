#!venv/bin/python

''' NOT WORKING '''

from scapy.all import *
from scapy.contrib.igmp import IGMP

source_interface = "Ethernet"

pck = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src='0.0.0.0', dst='255.255.255.255')/UDP(dport=67, sport=68)/BOOTP(op=1)/DHCP(options=[('message-type', 'discover'), ('end')])
pck.show()
sendp(pck, iface=source_interface, loop=1)