# pip install jsonrpclib-pelix

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

# configure EOS devices
conf = ['enable', 'configure']
# BGP conf
basic = ['ip routing', 'interface ethernet 1', 'no shutdown','no switchport', 'ip address 10.10.10.1/24', 'router bgp 1', 'neighbor 10.10.10.2 remote-as 2', 'redistribute connected']
conf = conf + basic
load_commands("10.100.164.113", "admin", "", conf)

# generate loopback configuration in a text file
with open('loopback.conf', 'w') as file:
    for n in range (0, 8):
        for m in range(0, 254):
            file.write('interface loopback' + str(255*n + m) + '\n')
            file.write('ip address 1.1.' + str(n) + '.' + str(m) + '/32' + '\n')

# generate list from text file
loopback_conf_list = generate_list_from_text_file('loopback.conf')

conf = ['enable', 'configure']
# BGP conf
basic = ['ip routing', 'interface ethernet 1', 'no shutdown','no switchport', 'ip address 10.10.10.2/24', 'router bgp 2', 'neighbor 10.10.10.1 remote-as 1', 'redistribute connected']
conf = conf + basic + loopback_conf_list
load_commands("10.100.164.114", "admin", "", conf)

# Verify states on the device
time.sleep(5)
commands = ['show ip bgp summary']
output = load_commands( "10.100.164.113", "admin", "",commands)
print (output)

