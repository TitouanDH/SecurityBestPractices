# SecurityBestPractices
This repository contains some scapy, packet crafting script demonstrating Security Issues.

## Installation
Download the repo from git and go in it then : 

Install virtualenv and configure python env
```bash
python -m pip install virtualenv
virtualenv venv
./venv/bin/activate
```

Once the virtualenv is enable
```bash
pip install -r requirement.txt
```

You are now set up !

## Configuration
The file settings.py contains the different attack parameters. Thoses are already set with default value however you will need to change in order to personnalise you attack.


## Execute attacks
Before launching any attack, you need to step up the settings.
Go to the *settings.py* fiel

Steps:  

    - Enter the Commun settings  
    - Look the list bellow, if your attack is one of those go to attack section in this file (Ctrl-F)
  
        DHCP rogue/exhaust
        LLDP rogue
        Vlan hopping
        LAND
        OSPF route injection
        ICMP REDIRECT

    - Set up the attack variable (if needed = in the list above)
    - Go back to the .py file
    - launch the attack

Refer back to the first attacks of the document in order to understand and have detailled explainations.