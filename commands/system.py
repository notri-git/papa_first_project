import platform
import socket
import os
import datetime


def os_info():
    print(platform.system())


def hostname():
    print(socket.gethostname())


def pwd():
    print(os.getcwd())


def ls():
    files = os.listdir()

    for file in files:
        print(file)


def dt():
    now = datetime.datetime.now()

    print(now.strftime("%d.%m.%Y %H:%M:%S"))