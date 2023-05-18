#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using do_deploy function
"""
import os
from fabric.api import env, put, run

# Set the SSH key and username
env.key_filename = "~/.ssh/school"
env.user = "ubuntu"

# Set the web server IPs
env.hosts = ['54.210.51.207', '54.90.53.12']


def do_deploy(archive_path):
    """creates uncompressed .tgz files and symbolic links remotely"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on web servers
        put(archive_path, "/tmp/")

        # Extract archive filename without extension
        archive_filename = os.path.basename(archive_path)
        folder_name = os.path.splitext(archive_filename)[0]

        # Uncompress the archive to /data/web_static/releases/
        run("sudo mkdir -p /data/web_static/releases/{}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(archive_filename, folder_name))

        # Delete the archive from the web servers
        run("sudo rm /tmp/{}".format(archive_filename))

        # rename
        run("sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}"
            .format(folder_name, folder_name))

        # Delete the existing symbolic link
        run("sudo rm -f /data/web_static/current")

        # Create a new symbolic link
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(folder_name))

        return True
    except Exception:
        return False
