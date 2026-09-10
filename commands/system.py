import platform
import socket
import os
import datetime


def os_info():
    return platform.system()


def hostname():
    return socket.gethostname()


def pwd():
    return os.getcwd()


def ls():
    files = os.listdir()

    return "\n".join(files)


def dt():
    now = datetime.datetime.now()

    return now.strftime("%d.%m.%Y %H:%M:%S")