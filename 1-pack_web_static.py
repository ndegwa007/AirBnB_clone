#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""


from datetime import datetime
from fabric.api import *


def do_pack():
    """generates .tgz archive"""
    date_format = "%Y%m%d%H%M%S"
    n = datetime.now().strftime(date_format)
    file_name = f"versions/web_static_{n}.tgz"
    local("mkdir -p versions")
    command = f"tar -cvzf {file_name} web_static"
    result = local(command)
    if result.failed:
        return None
    else:
        return file_name
