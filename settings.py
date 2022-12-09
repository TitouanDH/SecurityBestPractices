"""
This file contains the common parameters use in the attacks.
"""

"Common settings"
source_interface = "Ethernet"
destination_ip = "10.77.77.31"
source_ip = "10.77.77.31"
mac_source = "c8:5a:cf:09:be:a7"
mac_dest = "ff:ff:ff:ff:ff:ff"
router = "10.77.77.254"

"DHCP rogue settings"
rogue_serv = "10.10.10.1"
broadcast_address = "10.10.10.255"
subnet_mask = "255.255.255.0"

"LLDP rogue settings. Refer directly to the file for the other attack parameters"
chassis_id=b"38:f3:ab:59:2a:7e"
port_id=b"38:f3:ab:59:2a:7e"

"Vlan hopping"
vlans = [0, 80] # vlans in order : from us to the target vlan

"LAND"
destination_port = 8888