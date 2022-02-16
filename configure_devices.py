#!/usr/bin/env python3

from functions import generate_list_from_text_file, load_commands

# configure EOS device1
conf = ['enable', 'configure']
# BGP conf
basic = generate_list_from_text_file('device1.cfg')
conf = conf + basic
load_commands("10.100.164.113", "admin", "", conf)

# configure EOS device2
conf = ['enable', 'configure']
# BGP conf
basic = generate_list_from_text_file('device2.cfg')
# generate loopback configuration in a text file
with open('loopback.cfg', 'w') as file:
    for n in range (0, 8):
        for m in range(0, 254):
            file.write('interface loopback' + str(255*n + m) + '\n')
            file.write('ip address 1.1.' + str(n) + '.' + str(m) + '/32' + '\n')
# generate list from text file
loopback_conf_list = generate_list_from_text_file('loopback.cfg')
conf = conf + basic + loopback_conf_list
load_commands("10.100.164.114", "admin", "", conf)


