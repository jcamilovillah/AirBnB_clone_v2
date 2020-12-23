#!/usr/bin/python3
""" Pack web static """
from fabric.api import *
from os import path

env.hosts = ["35.185.12.242", "35.229.37.224"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False
    try:
        dire = "data/web_static/releases"
        file_name = archive_path.split('/')[-1]
        wext = file_name.split('.')[0]
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p mkdir -p /{}/{}".format(dire, wext))
        run("tar -xzf /tmp/{} -C /{}/{}/".format(file_name, dire, wext))
        run("rm /tmp/{}".format(file_name))
        run("mv /{}/{}/web_static/* /{}/{}/".format(dire, wext, dire, wext))
        run("rm -rf /{}/{}/web_static".format(dire, wext))
        run("rm -rf /data/web_static/current")
        run("ln -s /{}/{}/ /data/web_static/current".format(dire, wext))
        return True

    except Exception:
        return False
