from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPort

from python.config import read_cfg


serial = QSerialPort()


def on_open():
    list_serial = read_cfg()
    com, baud = list_serial[0], list_serial[1]
    serial.setPortName(com)
    serial.setBaudRate(int(baud))
    serial.open(QIODevice.ReadWrite)

