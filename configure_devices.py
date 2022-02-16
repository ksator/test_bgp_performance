#!/usr/bin/env python3

from functions import generate_list_from_text_file, load_commands

conf = ['enable', 'configure']

# BGP conf for device 1
basic = generate_list_from_text_file('device1.cfg')

# configure EOS device1
device1 = conf + basic
load_commands("10.100.164.113", "admin", "", device1, format = 'text')

# BGP conf for device 2
basic = generate_list_from_text_file('device2.cfg')

# generate loopback interfaces configuration in a text file
with open('loopback.cfg', 'w') as file:
    for n in range (0, 8):
        for m in range(0, 254):
            file.write('interface loopback' + str(255*n + m) + '\n')
            file.write('ip address 2.2.' + str(n) + '.' + str(m) + '/32' + '\n')

# generate list from text file
loopback_int_list = generate_list_from_text_file('loopback.cfg')

# generate static routes configuration in a text file
with open('static_routes.cfg', 'w') as file:
    for n in range (0, 254):
        for m in range(0, 254):
            file.write('ip route 1.1.' + str(n) + '.' + str(m) + '/32 Null0' + '\n')

# generate list from text file
static_routes_list = generate_list_from_text_file('static_routes.cfg')

# configure EOS device2
device2 = conf + basic + loopback_int_list + static_routes_list
load_commands("10.100.164.114", "admin", "", device2, format = 'text')