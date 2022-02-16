#!/usr/bin/env python3

from functions import generate_list_from_text_file, load_commands

# generate list from text file
commands = generate_list_from_text_file('show_commands_json.txt')

# Verify states on the device
output = load_commands( "10.100.164.113", "admin", "",commands, format = 'json')
for peer in output[0]['vrfs']['default']['peers']:
    print(peer)
    print("peerState " + output[0]['vrfs']['default']['peers'][peer]['peerState'])
    print("outMsgQueue " + str(output[0]['vrfs']['default']['peers'][peer]['outMsgQueue']))
    print("inMsgQueue " + str(output[0]['vrfs']['default']['peers'][peer]['inMsgQueue']))
    print("prefixReceived " + str(output[0]['vrfs']['default']['peers'][peer]['prefixReceived']))

print('\n')

# generate list from text file
commands = generate_list_from_text_file('show_commands_text.txt')
# Verify states on the device
output = load_commands( "10.100.164.113", "admin", "",commands, format = 'text')
print(output[0]['output'])
print(output[1]['output'])
