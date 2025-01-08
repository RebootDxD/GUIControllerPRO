#imports ---------------------------------------------------------------------------------------------------------------
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, FramelessDialog

from MainWindow import Ui_Form  #imports .ui compiled to .py
from AboutWindow import Ui_About
from ComWindow import Ui_Com
import img.res # impor img

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
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b")

        self.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
