#!venv/bin/python

from scapy.all import *
from scapy.all import IP, UDP, DNS,DNSQR, DNSRR
import settings

dns_resp =  IP(src='10.130.7.9', dst='10.130.7.14') \
            / UDP(sport=53) \
            / DNS(id=2, qr=1, ra=1, qdcount=1, ancount=1, qd=DNSQR(qtype="A", qname="test.com"), an=DNSRR(rrname="test.com", rdata="10.10.10.1"))
send(dns_resp, iface=settings.source_interface, verbose=0)
