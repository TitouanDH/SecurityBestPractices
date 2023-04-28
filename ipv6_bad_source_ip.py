#!venv/bin/python

from scapy.all import *
from scapy.all import IPv6, ICMPv6EchoRequest
import settings
"""
Send an ipv6 packet with random source address
"""

"IPv6 bad source ip"


ip = IPv6(src=RandIP6(), dst="ff02::2", hlim=1)
icmpv6 = ICMPv6EchoRequest()

packet = ip/icmpv6
packet.show()

send(packet, iface=settings.source_interface)