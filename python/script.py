
import os
from PyQt5.QtSerialPort import QSerialPort
from configparser import ConfigParser


class Config(ConfigParser):

    def __init__(self):
        super().__init__()
        if os.path.exists("Settings.ini"):
            self.read("Settings.ini")
            self.Com = self.get("Settings", "COM")
            baudRateStr = self.get("Settings", "baudRate")
            self.BaudRate = str(baudRateStr)
            global Com_
            global Baud
            Com_ = self.Com
            Baud = self.BaudRate
        else:
            self.add_section("Settings")
            self.set("Settings", "COM", "COM1")
            self.set("Settings", "baudRate", "115200")
            self.Com = "COM1"
            self.BaudRate = "115200"
            with open("Settings.ini", "w+") as configfile:
                self.write(configfile)


class Connect(QSerialPort):
    def __init__(self):
        super().__init__()

        self.setPortName(COM)
        self.open(QIODevice.ReadWrite)








