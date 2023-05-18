#!/usr/bin/python3
"""
Fabric script that generates a tgz archive
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """generates .tgz archive"""
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static".format(path))
    if result.failed:
        return None
    return path
