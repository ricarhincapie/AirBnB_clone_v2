#!/usr/bin/python3
"""Transfers an Archive to server"""

from fabric.api import run, put, env
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['54.234.64.157', '34.75.248.42']

def do_deploy(archive_path):
    """Deploys an archive to servers
    with arg path/to/archive"""

    if exists(archive_path) is False:
        return False

    try:
        put('%s' % archive_path, '/tmp/')
        name_ex = archive_path.split("/")[1]
        name_noex = name.split(".")[0]
        run('sudo mkdir -p /data/web_static/releases/%s' % name_noex)
        run('sudo tar -xzf /tmp/%s -C data/web_static/releases/%s' % (name_ex, name_noex))
        # Uncompress the tar file to the releases directory
        run('sudo rm /tmp/%s' % name_ex)  # Delete Archive file
        run('mv /data/web_static/releases/%s/web_static/* /data/web_static/releases/%s' % (name_noex, name_noex))
        run('sudo rm -rf data/web_static/releases/%s/web_static' % name_noex)
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/%s /data/web_static/current' % name_noex)
        return True

    except Exception:
        return False
