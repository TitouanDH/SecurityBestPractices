#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP
import settings



pck = Ether(src=RandMAC())/IP(src=settings.source_ip, dst=settings.destination_ip)/ICMP()/Raw(b"X" * 500)
sendp(pck, iface=settings.source_interface, loop=1)