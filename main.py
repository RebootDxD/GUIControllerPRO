#imports ---------------------------------------------------------------------------------------------------------------
import sys
from configparser import ConfigParser

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, FramelessDialog

from ui.MainWindow import Ui_Form  #imports .ui compiled to .py
from ui.AboutWindow import Ui_About
from ui.ComWindow import Ui_Com
import img.res # impor img
from python.script import Config


#-----------------------------------------------------------------------------------------------------------------------
class Window(FramelessWindow, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.AboutBtn.clicked.connect(WindowDialog)
        self.ComSetBtn.clicked.connect(WindowCom)


class WindowDialog(FramelessDialog, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.label_3.setText('<a href="https://github.com/RebootDxD"> <img src="img/git.png" width="32" height="32"> </a>')
        self.label_3.setOpenExternalLinks(True)

        self.exec_()

class WindowCom(FramelessDialog, Ui_Com):
    def __init__(self):
        super().__init__()
        i = Config()
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b;color:#fff;")
        self.ComSetComboBox.setCurrentText(i.Com)
        self.ComSetComboBox_2.setCurrentText(str(i.BaudRate))
        self.pushButton_2.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(lambda: save())

        def save():
            cfg = ConfigParser()
            cfg.add_section("Settings")
            Com = self.ComSetComboBox.currentText()
            Baud = self.ComSetComboBox_2.currentText()
            cfg.set("Settings", "COM", Com)
            cfg.set("Settings", "baudRate", str(Baud))
            with open("Settings.ini", "w") as configfile:
                cfg.write(configfile)
            self.close()



        self.exec_()

if __name__ == '__main__':
    Config()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

