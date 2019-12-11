# ssi-ldapgroup

ssi-ldapgroup provides a small library and set of scripts to add, remove,
and list users in a given group.  It is meant to be tied to a specific OU
with pre-existing password-based authentication.

This package is a thin wrapper around the `ldap_groups` PyPi module v2.5.2,
because other versions aren't currently working for some reason.

## </etc/ldapgroup/config.yaml>

Per-host configuration is provided in a central yaml file that looks like
this:

    domain: DC=services,DC=fnal,DC=gov
    group_dn_suffix: OU=CMS,OU=FermiGroups,DC=services,DC=fnal,DC=gov
    server_uri: ldaps://ldapdc2.services.fnal.gov:636
    user_dn_suffix: OU=FermiUsers,DC=services,DC=fnal,DC=gov

    bind:
        dn: CN=cd-srv-cmsadmin,OU=FermiServiceAccounts,DC=services,DC=fnal,DC=gov
        password: [insert-password-here]
