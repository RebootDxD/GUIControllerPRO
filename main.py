import sys

from PyQt5 import QtCore


from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow

from MainWindow import Ui_Form #import .ui compiled to .py


class Window(FramelessWindow, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color: #79215b")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())