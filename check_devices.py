from functions import generate_list_from_text_file, load_commands

# generate list from text file
commands = generate_list_from_text_file('show_commands.txt')

# Verify states on the device
output = load_commands( "10.100.164.113", "admin", "",commands)
for peer in output[0]['vrfs']['default']['peers']:
    print(peer)
    print("peerState " + output[0]['vrfs']['default']['peers'][peer]['peerState'])
    print("outMsgQueue " + str(output[0]['vrfs']['default']['peers'][peer]['outMsgQueue']))
    print("inMsgQueue " + str(output[0]['vrfs']['default']['peers'][peer]['inMsgQueue']))
    print("prefixReceived " + str(output[0]['vrfs']['default']['peers'][peer]['prefixReceived']))


