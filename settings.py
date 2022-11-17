"""
This file contains the commun parameters use in the attacks.
"""

"Commun settings"
source_interface = "ens192"
destination_ip = "239.10.20.30"
source_ip = "10.130.7.1"
mac_dest = "01:80:c2:00:00:0e"

"DHCP rogue settings"
rogue_serv = "10.10.10.1"
broadcast_address = "10.10.10.255"
subnet_mask = "255.255.255.0"
router = "10.10.10.254"

"LLDP rogue settings. Refer directly to the file for the other attack parameters"
chassis_id=b"38:f3:ab:59:2a:7e"
port_id=b"38:f3:ab:59:2a:7e"

"Vlan hopping"
vlans = [0, 80] # vlans in order : from us to the target vlan
