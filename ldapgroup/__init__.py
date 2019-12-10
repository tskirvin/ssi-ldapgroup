# ldapgroup.py
# wrapper around ldap_groups == 2.5.2

#########################################################################
### Declarations ########################################################
#########################################################################

import ldap_groups
import sys
import yaml

#########################################################################
### Subroutines #########################################################
#########################################################################

def config_yaml(file):
    """
    Load a yaml configuration file to get required settings
    """
    global config

    try:
        config = yaml.load(open(file, 'r'))
    except IOError as exc:
        print("file error: %s" % (exc))
        sys.exit(2)
    except yaml.YAMLError as exc:
        print("YAML error: %s" % (exc))
        sys.exit(2)
    except Exception as exc:
        print("unknown error: %s" % (exc))
        sys.exit(2)

    return config

def connect(group_name, config):
    """
    Connect to the LDAP server.  Requires a specific group.
    """
    global ldap_connection

    group_dn = "CN=%s,%s" % (group_name, config['group_dn_suffix'])
    ldap_connection = ldap_groups.ADGroup(group_dn, config['server_uri'],
        config['user_dn_suffix'], None, None, config['bind']['dn'],
        config['bind']['password'])
    return ldap_connection

def is_empty(connection):
    """
    Check to see if there is a possible list of users.
    """
    if 'member' in connection.get_attributes(): return False
    return True

def users(connection):
    """
    Return array of users in the group.
    """
    if is_empty(connection): return []
    attr = connection.get_attributes()
    return attr['member']

def add_member(connection, user_name):
    """
    Add a user to the list.
    """
    connection.add_member(user_name)

def has_user(connection, user_name):
    """
    """
    if is_empty(connection): return False

    user_dn = "CN=%s,%s" % (user_name, config['user_dn_suffix'])
    if user_dn in connection.get_attributes()['member']: return True
    else: return False

def remove_user(connection, user_name):
    """
    """
    connection.remove_member(user_name)
