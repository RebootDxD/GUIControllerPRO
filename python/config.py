import os
from configparser import ConfigParser

patch = "C:/Users/potap/PycharmProjects/PythonProject/Settings.ini"


def check_cfg():
    if os.path.exists("Settings.ini"):
        print("cfg Exist!")
    else:
        cfg = ConfigParser()
        cfg.add_section("Settings")
        cfg.set('Settings', "COM", "COM1")
        cfg.set("Settings", "baudRate", "115200")
        cfg.Com = "COM1"
        cfg.BaudRate = "115200"
        with open("Settings.ini", "w+") as configfile:
            cfg.write(configfile)
        print("cfg create successfully")


def read_cfg():
    cfg = ConfigParser()
    cfg.read(patch)
    com = cfg.get("Settings", "COM")
    baud_rate_str = cfg.get("Settings", "baudRate")
    baud_rate = str(baud_rate_str)
    return com, baud_rate


def save_cfg(com, baud):
    cfg = ConfigParser()
    cfg.add_section("Settings")
    cfg.set("Settings", "COM", com)
    cfg.set("Settings", "baudRate", str(baud))
    with open("Settings.ini", "w+") as configfile:
        cfg.write(configfile)
