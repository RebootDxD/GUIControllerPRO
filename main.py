# imports ---------------------------------------------------------------------------------------------------------------
import sys

from PyQt5 import QtCore
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, FramelessDialog

from python.config import check_cfg, read_cfg, save_cfg
from python.serial import on_open
from ui.MainWindow import Ui_Form  # imports .ui compiled to .py
from ui.AboutWindow import Ui_About
from ui.ComWindow import Ui_Com
import img.res  # import img
import python.config


# -----------------------------------------------------------------------------------------------------------------------
class Window(FramelessWindow, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.AboutBtn.clicked.connect(WindowDialog)
        self.ComSetBtn.clicked.connect(WindowCom)
        self.pushButton.clicked.connect(lambda: on_open())
        check_cfg()



class WindowCom(FramelessDialog, Ui_Com):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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


class WindowDialog(FramelessDialog, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.label_3.setText(
            '<a href="https://github.com/RebootDxD"> <img src="img/git.png" width="32" height="32"> </a>')
        self.label_3.setOpenExternalLinks(True)

        self.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
