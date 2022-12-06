#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, ARP
import settings

pck = Ether(src=RandMAC(), dst="FF:FF:FF:FF:FF:FF")/ARP(op=2, psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF")/Raw(b"X" * 20)
pck.show()
sendp(pck, iface=settings.source_interface)