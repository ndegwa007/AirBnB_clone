from datetime import datetime
from fabric.api import *

def do_pack():

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
