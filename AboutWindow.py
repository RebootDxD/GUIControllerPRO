# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(669, 331)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        self.label_7 = QtWidgets.QLabel(About)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: transparent;\n"
"color:white;")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(20, 32, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"color:white;")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(About)
        self.label_6.setGeometry(QtCore.QRect(300, 32, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: transparent;\n"
"color:white;")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 461, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTabletTracking(False)
        self.label_2.setStyleSheet("background: transparent;\n"
"color:white;")
        self.label_2.setLineWidth(3)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(About)
        self.label_8.setGeometry(QtCore.QRect(1, 32, 711, 601))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("img/background.jpg"))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 32, 32))
        self.label_3.setStyleSheet("background: transparent;\n"
"")
        self.label_3.setPixmap(QtGui.QPixmap("img/github-mark-white.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(47, 296, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent;\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.label_8.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_7.raise_()

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Form"))
        self.label_7.setText(_translate("About", "GNU GPL v3.0"))
        self.label.setText(_translate("About", "GUIController PRO"))
        self.label_6.setText(_translate("About", "Release 1.0"))
        self.label_2.setText(_translate("About", "Узкоспециализированное ПО предназначенное для работы с модулем переключения каналов связи ЭМР (электромагнитных расходомеров) для ускорения калибровочного процесса."))
        self.label_4.setText(_translate("About", "RebootDxD"))
