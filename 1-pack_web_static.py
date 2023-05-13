#!/usr/bin/python3
"""module has a function that creates zip files from static files"""
from datetime import datetime
from fabric.api import *


def do_pack():

    """
    do_pack: function creates a zip file of static files
    into a folder called versions

    Args:
        no args

    Returns:
        a zip file with compressed with static files
    """

    date_format = "%Y%m%d%H%M%S"
    now = datetime.utcnow().strftime(date_format)
    file_name = f"versions/web_static_{now}.tgz"
    local("mkdir -p versions")
    command = f"tar -cvzf {file_name} web_static"
    result = local(command)
    if result.failed:
        return None
    else:
        return file_name
