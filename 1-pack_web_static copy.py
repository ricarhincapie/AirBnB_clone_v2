#!/usr/bin/python3
"""Module to compress web_static with Fabric"""

from fabric.api import local
import datetime


def do_pack():
    """Packs a local web_static folder to
    .tgz format for deployment"""
    local("mkdir -p versions")
    x = datetime.datetime.now()
    y = x.strftime("%Y%m%d%H%M%S")
    w = "web_static_" + (x.strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf versions/%s.tgz web_static/" % w, capture=True)
    if result.failed:
        return None
    return result
