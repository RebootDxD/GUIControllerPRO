# imports---------------------------------------------------------------------------------------------------------------
import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer, QIODevice
from PyQt5.QtGui import QIcon
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, FramelessDialog

from python.config import check_cfg, read_cfg, save_cfg
from ui.MainWindow import Ui_Form
from ui.AboutWindow import Ui_About
from ui.ComWindow import Ui_Com
from ui.ErrorDialog import Ui_Dialog
import img.res


# Main window-----------------------------------------------------------------------------------------------------------

class Window(FramelessWindow, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)

        # cfg-----------------------------------------------------------------------------------------------------------
        check_cfg()
        # ui------------------------------------------------------------------------------------------------------------
        self.setupUi(self)

        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.AboutBtn.clicked.connect(WindowDialog)
        self.ComSetBtn.clicked.connect(WindowCom)
        self.titleBar.maxBtn.hide()
        self.pushButton.clicked.connect(lambda: open())
        self.pushButton_2.clicked.connect(lambda: close())
        self.Prem_1.clicked.connect(lambda: radio(1))
        self.Prem_2.clicked.connect(lambda: radio(2))
        self.Prem_3.clicked.connect(lambda: radio(3))
        self.Prem_4.clicked.connect(lambda: radio(4))
        self.Prem_5.clicked.connect(lambda: radio(5))
        self.PC_1.clicked.connect(lambda: radio(6))
        self.PC_2.clicked.connect(lambda: radio(7))
        self.PC_3.clicked.connect(lambda: radio(8))
        self.PC_4.clicked.connect(lambda: radio(9))
        self.PC_5.clicked.connect(lambda: radio(10))

        def open():
            self.label_3.setText("Выполняеться подключение к " + list_serial[0])
            on_open()
            if check() == 0:
                self.pushButton.setEnabled(False)
                self.pushButton_2.setEnabled(True)
                self.Prem_2.setEnabled(True)
                self.Prem_3.setEnabled(True)
                self.Prem_4.setEnabled(True)
                self.Prem_5.setEnabled(True)
                self.PC_2.setEnabled(True)
                self.PC_3.setEnabled(True)
                self.PC_4.setEnabled(True)
                self.PC_5.setEnabled(True)

            else:
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
                ErrorDialog()
                serial.close()

        def radio(device):  # 1+ 1,2,3,4,5 = prem ; 2+ 1,2,3,4,5 = PC
            if device == 1:
                self.Prem_1.setEnabled(False)
                self.Prem_2.setEnabled(True)
                self.Prem_3.setEnabled(True)
                self.Prem_4.setEnabled(True)
                self.Prem_5.setEnabled(True)
                on_send("1")
            elif device == 2:
                self.Prem_1.setEnabled(True)
                self.Prem_2.setEnabled(False)
                self.Prem_3.setEnabled(True)
                self.Prem_4.setEnabled(True)
                self.Prem_5.setEnabled(True)
                on_send("2")
            elif device == 3:
                self.Prem_1.setEnabled(True)
                self.Prem_2.setEnabled(True)
                self.Prem_3.setEnabled(False)
                self.Prem_4.setEnabled(True)
                self.Prem_5.setEnabled(True)
                on_send("3")
            elif device == 4:
                self.Prem_1.setEnabled(True)
                self.Prem_2.setEnabled(True)
                self.Prem_3.setEnabled(True)
                self.Prem_4.setEnabled(False)
                self.Prem_5.setEnabled(True)
                on_send("4")
            elif device == 5:
                self.Prem_1.setEnabled(True)
                self.Prem_2.setEnabled(True)
                self.Prem_3.setEnabled(True)
                self.Prem_4.setEnabled(True)
                self.Prem_5.setEnabled(False)
                on_send("5")
            elif device == 6:
                self.PC_1.setEnabled(False)
                self.PC_2.setEnabled(True)
                self.PC_3.setEnabled(True)
                self.PC_4.setEnabled(True)
                self.PC_5.setEnabled(True)
                on_send("6")
            elif device == 7:
                self.PC_1.setEnabled(True)
                self.PC_2.setEnabled(False)
                self.PC_3.setEnabled(True)
                self.PC_4.setEnabled(True)
                self.PC_5.setEnabled(True)
                on_send("7")
            elif device == 8:
                self.PC_1.setEnabled(True)
                self.PC_2.setEnabled(True)
                self.PC_3.setEnabled(False)
                self.PC_4.setEnabled(True)
                self.PC_5.setEnabled(True)
                on_send("8")
            elif device == 9:
                self.PC_1.setEnabled(True)
                self.PC_2.setEnabled(True)
                self.PC_3.setEnabled(True)
                self.PC_4.setEnabled(False)
                self.PC_5.setEnabled(True)
                on_send("9")
            elif device == 10:
                self.PC_1.setEnabled(True)
                self.PC_2.setEnabled(True)
                self.PC_3.setEnabled(True)
                self.PC_4.setEnabled(True)
                self.PC_5.setEnabled(False)
                on_send("10")

        def close():
            on_close()
            self.pushButton_2.setEnabled(False)
            self.pushButton.setEnabled(True)
            self.Prem_1.setEnabled(False)
            self.Prem_2.setEnabled(False)
            self.Prem_3.setEnabled(False)
            self.Prem_4.setEnabled(False)
            self.Prem_5.setEnabled(False)
            self.PC_1.setEnabled(False)
            self.PC_2.setEnabled(False)
            self.PC_3.setEnabled(False)
            self.PC_4.setEnabled(False)
            self.PC_5.setEnabled(False)
            self.label_3.setText("Ожидание подключения")

        # serial--------------------------------------------------------------------------------------------------------
        serial = QSerialPort()
        list_serial = read_cfg()
        com, baud = list_serial[0], list_serial[1]

        def check():
            err = serial.error()
            return err

        def on_open():
            serial.setPortName(com)
            serial.setBaudRate(int(baud))
            serial.open(QIODevice.ReadWrite)
            if check() == 0:
                print("Serial port open successfully")
                QTimer.singleShot(1500, lambda: on_send("0"))
            else:
                print("Serial error")

        def on_send(message):
            if check() == 0:
                serial.write(message.encode())
            else:
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
                ErrorDialog()
                on_close()

        def on_read():
            if serial.canReadLine():
                rx = serial.readLine()
                data = str(rx, 'UTF-8').strip()
                if data[0] == "#":
                    ver = data[1:]
                    print("Software version " + ver)
                    self.label_3.setText("Подключено к " + list_serial[0] + " ПО v" + ver)
                else:
                    print(data)
            else:
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
                ErrorDialog()
                on_close()

        serial.readyRead.connect(on_read)

        def on_close():
            serial.close()
            print("Serial port close successfully")


# Com window------------------------------------------------------------------------------------------------------------

class WindowCom(FramelessDialog, Ui_Com):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Выбор COM порта")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setStyleSheet("background-color: #79215b;color:#fff;")
        list_serial = read_cfg()
        com, baud = list_serial[0], list_serial[1]
        self.ComSetComboBox.setCurrentText(com)
        self.ComSetComboBox_2.setCurrentText(baud)
        self.pushButton_2.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(lambda: save())

        def save():
            com_save = self.ComSetComboBox.currentText()
            baud_save = self.ComSetComboBox_2.currentText()
            save_cfg(com_save, baud_save)
            self.close()

        self.exec_()


# About window----------------------------------------------------------------------------------------------------------

class WindowDialog(FramelessDialog, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("О программе")
        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        if hasattr(sys, '_MEIPASS'):
            git_icon_path = os.path.join(sys._MEIPASS, 'img', 'git.png')
        else:
            git_icon_path = os.path.join('img', 'git.png')
        self.label_3.setText(f'<a href="https://github.com/RebootDxD"> <img src="{git_icon_path}" width="32" height="32"> </a>')
        self.label_3.setOpenExternalLinks(True)

        self.exec_()


# Error dialog----------------------------------------------------------------------------------------------------------
class ErrorDialog(FramelessDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ошибка")
        self.setStyleSheet("background-color: #79215b")
        self.setResizeEnabled(False)
        self.pushButton.clicked.connect(lambda: self.close())
        self.exec_()


# App setup-------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    if hasattr(sys, "_MEIPASS"):
        icon_path = os.path.join(sys._MEIPASS, "img/icon.ico")  # PyInstaller
    else:
        icon_path = "img/icon.ico"  # Обычный запуск

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(icon_path))
    win = Window()
    win.setWindowIcon(QtGui.QIcon(icon_path))
    win.show()
    sys.exit(app.exec_())
