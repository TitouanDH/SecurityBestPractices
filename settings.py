"""
This file contains the common parameters use in the attacks.
"""

"Common settings"
source_interface = "Ethernet"
destination_ip = "10.130.7.1"
source_ip = "10.77.77.55"
mac_source = "c8:5a:cf:09:be:a7"
mac_dest = "ff:ff:ff:ff:ff:ff"
router = "10.77.77.254"

"DHCP rogue settings"
rogue_serv = "10.77.77.55"
broadcast_address = "10.77.77.255"
subnet_mask = "255.255.255.0"
start_ip = "10.77.77.80"

"LLDP rogue settings. Refer directly to the file for the other attack parameters"
chassis_id=b"38:f3:ab:59:2a:7e"
port_id=b"38:f3:ab:59:2a:7e"

"Vlan hopping"
vlans = [0, 80] # vlans in order : from us to the target vlan

"LAND"
destination_port = 8888

"OSPF route injection"
ospf_spoofed = "10.88.88.254"
ospf_network_adv = "10.99.99.0"
ospf_area = "0.0.0.0"