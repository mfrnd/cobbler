"""
Migration from V2.x.x to V2.8.5
"""
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: 2021 Dominik Gedon <dgedon@suse.de>
# SPDX-FileCopyrightText: 2021 Enno Gotthold <egotthold@suse.de>
# SPDX-FileCopyrightText: Copyright SUSE LLC


from schema import Schema, SchemaError

schema = Schema({
    "allow_duplicate_hostnames": bool,
    "allow_duplicate_ips": bool,
    "allow_duplicate_macs": bool,
    "allow_dynamic_settings": bool,
    "always_write_dhcp_entries": bool,
    "anamon_enabled": bool,
    "auth_token_expiration": int,
    "bind_chroot_path": str,
    "bind_master": str,
    "buildisodir": str,
    "build_reporting_enabled": bool,
    "build_reporting_ignorelist": str,
    "build_reporting_sender": str,
    "build_reporting_smtp_server": str,
    "build_reporting_subject": str,
    "build_reporting_to_address": str,
    "cheetah_import_whitelist": list,
    "client_use_localhost": str,
    "cobbler_master": str,
    "consoles": str,
    "createrepo_flags": str,
    "default_deployment_method": str,
    "default_kickstart": str,
    "default_name_servers": list,
    "default_name_servers_search": list,
    "default_ownership": list,
    "default_password_crypted": str,
    "default_template_type": str,
    "default_virt_bridge": str,
    "default_virt_disk_driver": str,
    "default_virt_file_size": int,
    "default_virt_ram": int,
    "default_virt_type": str,
    "enable_gpxe": bool,
    "enable_menu": bool,
    "func_auto_setup": bool,
    "func_master": str,
    "http_port": int,
    "isc_set_host_name": bool,
    "iso_template_dir": str,
    "kerberos_realm": str,
    "kernel_options": dict,
    "kernel_options_s390x": dict,
    "ldap_anonymous_bind": bool,
    "ldap_base_dn": str,
    "ldap_management_default_type": str,
    "ldap_port": int,
    "ldap_search_bind_dn": str,
    "ldap_search_passwd": str,
    "ldap_search_prefix": str,
    "ldap_server": str,
    "ldap_tls": str,
    "ldap_tls_cacertfile": str,
    "ldap_tls_certfile": str,
    "ldap_tls_keyfile": str,
    "manage_dhcp": bool,
    "manage_dns": bool,
    "manage_forward_zones": list,
    "manage_reverse_zones": list,
    "manage_genders": bool,
    "manage_rsync": bool,
    "manage_tftp": bool,
    "manage_tftpd": bool,
    "mgmt_classes": list,
    "mgmt_parameters": dict,
    "next_server": str,
    "power_management_default_type": str,
    "power_template_dir": str,
    "proxy_url_ext": str,
    "proxy_url_int": str,
    "puppet_auto_setup": bool,
    "puppet_parameterized_classes": bool,
    "puppet_server": str,
    "puppet_version": int,
    "pxe_just_once": bool,
    "pxe_template_dir": str,
    "redhat_management_permissive": bool,
    "redhat_management_server": str,
    "redhat_management_key": str,
    "redhat_management_type": str,
    "register_new_installs": bool,
    "remove_old_puppet_certs_automatically": bool,
    "replicate_repo_rsync_options": str,
    "replicate_rsync_options": str,
    "reposync_flags": str,
    "reposync_rsync_flags": str,
    "restart_dhcp": bool,
    "restart_dns": bool,
    "run_install_triggers": bool,
    "scm_track_enabled": bool,
    "scm_track_mode": str,
    "serializer_pretty_json": bool,
    "server": str,
    "signature_path": str,
    "signature_url": str,
    "sign_puppet_certs_automatically": bool,
    "snippetsdir": str,
    "template_remote_kickstarts": bool,
    "virt_auto_boot": bool,
    "webdir": str,
    "xmlrpc_port": int,
    "yum_distro_priority": int,
    "yum_post_install_mirror": bool,
    "yumdownloader_flags": str,
}, ignore_extra_keys=False)


def validate(settings: dict) -> bool:
    """
    Checks that a given settings dict is valid according to the reference schema ``schema``.

    :param settings: The settings dict to validate.
    :return: True if valid settings dict otherwise False.
    """
    try:
        schema.validate(settings)
    except SchemaError:
        return False
    return True


def normalize(settings: dict) -> dict:
    """
    If data in ``settings`` is valid the validated data is returned.

    :param settings: The settings dict to validate.
    :return: The validated dict.
    """
    return schema.validate(settings)


def migrate(settings: dict) -> dict:
    """
    Migration of the settings ``settings`` to the V3.2.1 settings

    :param settings: The settings dict to migrate
    :return: The migrated dict
    """
    # Use the functions from helper.py to achieve this!
    pass
