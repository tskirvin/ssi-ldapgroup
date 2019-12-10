#########################################################################
### Configuration #######################################################
#########################################################################

# domain = 'DC=services,DC=fnal,DC=gov'

########################################################################
### Declarations ########################################################
#########################################################################

# import ldap
# import ldap.filter
import ldap_groups
# import ldap.modlist as modlist
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

#             usercn=tmp[0].split('=')[1]
#             self.group.remove_member(usercn)
#
#     def add_member(self,user):


#
#     try:
#         result = lconn.search_s(config.base_dn, ldap.SCOPE_SUBTREE, "(&(objectClass=person)(cn=%s))" % username)
#         if len(result) == 1: return True
#         if len(result) > 1: raise Exception('multiple user match')
#         return False
#     except:
#         raise
#
# def group_exists(groupname, ldap_config):
#     c = configparser.RawConfigParser()
#     c.read(ldap_config)
#
#     # group_dn="CN=%s,OU=Harbor,OU=FermiGroups,DC=services,DC=fnal,DC=gov" % groupname
#     group_dn = "CN=%s,%s" % (groupname, c.get('main', 'group_dn_suffix'))
#     try:
#         ldap_groups.ADGroup(group_dn, config.server_uri, config.base_dn,
#             None, None, config.bind.dn, config.bind.password)
#         return True
#     except Exception:
#         return False
#
#
#             # self.group = ldap_groups.ADGroup(self.group_dn, self.server_uri, self.base_dn, None, None, self.bind_dn, self.bind_password)
#
# class ADGroupFlex(object):
#     def __init__(self, group_name, config_file):
#
#         # self.config=configparser.RawConfigParser()
#         # self.config.read(config_file)
#
#         # self.config_file=config_file
#         # self.group_name=group_name
#         # self.server_uri=self.config.get('main','server_uri')
#         # self.base_dn=self.config.get('main','base_dn')
#         # self.bind_dn=self.config.get('main','bind_dn')
#         # self.bind_password=self.config.get('main','bind_password')
#         # self.group_dn_suffix=self.config.get('main','group_dn_suffix')
#
#         if not self.group_exists(config_file):
#             self.__ldap_add_group()
#
#         try:
#             self.group = ldap_groups.ADGroup(self.group_dn, self.server_uri, self.base_dn, None, None, self.bind_dn, self.bind_password)
#         except Exception as e:
#             raise(e)
#
#
#     def get_attributes(self):
#         return self.group.get_attributes()
#
#     def is_empty(self):
#         attributes=self.group.get_attributes()
#         if 'member' in attributes:
#             return False
#         else:
#             return True
#
#     def group_exists(self, ldap_config):
#
#         try:
#             group=ldap_groups.ADGroup(self.group_dn, self.server_uri, self.base_dn, None, None, self.bind_dn, self.bind_password )
#             return True
#         except Exception as e:
#             return False
#
#
#     def get_users(self):
#         if not self.is_empty(): return self.group.get_attributes()['member']
#
#
#     def has_user(self,user):
#         userblob="CN=%s,OU=FermiUsers,%s" % (user, domain)
#         if self.is_empty(): return False
#
#         if userblob in self.group.get_attributes()['member']:
#             return True
#         else:
#             return False
#
#     # remove users from group
#     def empty_group(self):
#         if self.is_empty(): return True
#
#         for user in self.group.get_attributes()['member']:
#             tmp=user.split(',')
#             usercn=tmp[0].split('=')[1]
#             self.group.remove_member(usercn)
#
#     def add_member(self,user):
#         if not self.has_user(user):
#             try:
#                 self.group.add_member(user)
#             except:
#                 raise
#         else:
#             raise SSIUserExistsError
#
#     def remove_member(self,user):
#         if self.has_user(user):
#             self.group.remove_member(user)
#
#     def get_group_member_info(self):
#         return self.group.get_member_info()
#
#     def get_attributes(self):
#         return self.group.get_attributes()
#
#     def get_name(self):
#         return self.group.get_attribute('name')
#
#     def get_type(self):
#         return self.group.get_attribute('objectClass')
#
#     # This is sloppy, but it works
#     def __ldap_add_group(self):
#
#         try:
#             lconn = ldap.initialize(self.server_uri)
#         except Exception as e:
#             print("Initialize failed")
#             print(e)
#             raise
#         #except ldap.LDAPError, e:
#         #    raise
#
#         try:
#             lconn.simple_bind_s(self.bind_dn, self.bind_password)
#         except Exception as e:
#             print("bind failed")
#             print(e)
#             raise
#
#         #groupdn="cn=%s,OU=Harbor,OU=FermiGroups,%s" % (groupname, domain)
#
#         attrs = {}
#         attrs['objectclass'] = ['top', 'group']
#         attrs['cn'] = self.group_name
#         attrs['objectCategory'] = 'CN=Group,CN=Schema,CN=Configuration,%s' % (domain)
#         ldif = modlist.addModlist(attrs)
#         try:
#             lconn.add_s(self.group_dn, ldif)
#         except:
#             raise
#
#     # This is sloppy, but it works
#     def delete_group(self):
#         if not self.is_empty():
#             raise SSIGroupNotEmptyError
#
#         try:
#             lconn = ldap.initialize(self.server_uri)
#             lconn.simple_bind_s(self.bind_dn, self.bind_password)
#         except ldap.LDAPError as e:
#             print("Error binding to ldap:")
#             print(e)
#             sys.exit(1)
#
#         try:
#             lconn.delete_s(self.group_dn)
#         except Exception as e:
#             print("Error deleting group")
#             print(e)
#
#         return True
#
# #########################################################################
# ### main () #############################################################
# #########################################################################
