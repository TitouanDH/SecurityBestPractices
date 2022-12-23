"""
This file contains the common parameters use in the attacks.
The variables names should be straight forward on the purpose of them.

Steps:
    - enter the Commun settings
    - Look the list bellow, if your attack is one of those go to attack section in this file (Ctrl-F)

    DHCP related
    LLDP rogue
    Vlan hopping
    LAND
    OSPF route injection
    ICMP REDIRECT

    - Set up the attack variable (if needed = in the list above)
    - Go back to the .py file
    - lunch the attack

Refer to the first attacks of the document in order to understand and have detailled explainations.

"""

"Common settings"
"Settings below are used in many script, set them before any new attack !"
source_interface = "Ethernet"
destination_ip = "10.77.77.254"
source_ip = "10.77.77.55"
mac_source = "c8:5a:cf:09:be:a7"
mac_dest = "ff:ff:ff:ff:ff:ff"
router = "10.77.77.254"

"DHCP related settings"
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

"ICMP REDIRECT"
icmp_redir_distant = "192.168.80.1"