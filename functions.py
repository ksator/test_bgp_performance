from jsonrpclib import Server
import ssl

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
