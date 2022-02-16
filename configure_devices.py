from jsonrpclib import Server
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

def generate_list_from_text_file(text_file):
    """
    Generate a list from a text file
    Args:
        text_file (file): Text file
    Returns:
        list: A list
    """
    try:
        with open(text_file, 'r') as f:
            conf_list = f.readlines()
            for i,line in enumerate(conf_list):
                conf_list[i] = line.strip()
            return conf_list
    except:
        return None

def load_commands(hostname, username, password, commands):
    """
    Use EAPI to load commands on an EOS device
    Args:
        hostname (string): device hostname or IP
        username (string): device username
        password (string): device password
        commands (list): list of EOS commands
    """
    url = "https://" + username + ":" + password + "@" + hostname + "/command-api"
    switch = Server(url)
    result=switch.runCmds(version = 1,cmds = commands, autoComplete=True)
    return result

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
with open('loopback.conf', 'w') as file:
    for n in range (0, 8):
        for m in range(0, 254):
            file.write('interface loopback' + str(255*n + m) + '\n')
            file.write('ip address 1.1.' + str(n) + '.' + str(m) + '/32' + '\n')
# generate list from text file
loopback_conf_list = generate_list_from_text_file('loopback.conf')
conf = conf + basic + loopback_conf_list
load_commands("10.100.164.114", "admin", "", conf)

# Verify states on the device
time.sleep(5)
commands = ['show ip bgp summary']
output = load_commands( "10.100.164.113", "admin", "",commands)
print (output)

