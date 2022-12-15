#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, ICMP, IPOption
import settings
import binascii


pck = Ether()/IP(dst=settings.destination_ip, options=IPOption(binascii.unhexlify('830310')))/ICMP()/Raw(b"X" * 500)
sendp(pck, iface=settings.source_interface)