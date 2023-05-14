#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''
from datetime import datetime
from fabric.api import *


def do_pack():
    '''generates .tgz archive from contents of the web_static folder'''
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
