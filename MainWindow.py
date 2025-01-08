# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(35, 289, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"color: white;\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #511352;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#390d39;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.Prem_1 = QtWidgets.QPushButton(Form)
        self.Prem_1.setEnabled(False)
        self.Prem_1.setGeometry(QtCore.QRect(30, 330, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_1.setFont(font)
        self.Prem_1.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_1.setObjectName("Prem_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 3, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: transparent;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.25);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.AboutBtn = QtWidgets.QPushButton(Form)
        self.AboutBtn.setGeometry(QtCore.QRect(110, 3, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.AboutBtn.setFont(font)
        self.AboutBtn.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: transparent;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.25);\n"
"}")
        self.AboutBtn.setObjectName("AboutBtn")
        self.Prem_2 = QtWidgets.QPushButton(Form)
        self.Prem_2.setEnabled(False)
        self.Prem_2.setGeometry(QtCore.QRect(120, 330, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_2.setFont(font)
        self.Prem_2.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_2.setObjectName("Prem_2")
        self.Prem_3 = QtWidgets.QPushButton(Form)
        self.Prem_3.setEnabled(False)
        self.Prem_3.setGeometry(QtCore.QRect(210, 330, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_3.setFont(font)
        self.Prem_3.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_3.setObjectName("Prem_3")
        self.Prem_4 = QtWidgets.QPushButton(Form)
        self.Prem_4.setEnabled(False)
        self.Prem_4.setGeometry(QtCore.QRect(300, 330, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_4.setFont(font)
        self.Prem_4.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_4.setObjectName("Prem_4")
        self.Prem_5 = QtWidgets.QPushButton(Form)
        self.Prem_5.setEnabled(False)
        self.Prem_5.setGeometry(QtCore.QRect(390, 330, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_5.setFont(font)
        self.Prem_5.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_5.setObjectName("Prem_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 37, 800, 600))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/background.jpg"))
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(35, 389, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.Prem_6 = QtWidgets.QPushButton(Form)
        self.Prem_6.setEnabled(False)
        self.Prem_6.setGeometry(QtCore.QRect(120, 430, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_6.setFont(font)
        self.Prem_6.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_6.setObjectName("Prem_6")
        self.Prem_7 = QtWidgets.QPushButton(Form)
        self.Prem_7.setEnabled(False)
        self.Prem_7.setGeometry(QtCore.QRect(390, 430, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_7.setFont(font)
        self.Prem_7.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_7.setObjectName("Prem_7")
        self.Prem_8 = QtWidgets.QPushButton(Form)
        self.Prem_8.setEnabled(False)
        self.Prem_8.setGeometry(QtCore.QRect(300, 430, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_8.setFont(font)
        self.Prem_8.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_8.setObjectName("Prem_8")
        self.Prem_9 = QtWidgets.QPushButton(Form)
        self.Prem_9.setEnabled(False)
        self.Prem_9.setGeometry(QtCore.QRect(210, 430, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_9.setFont(font)
        self.Prem_9.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_9.setObjectName("Prem_9")
        self.Prem_10 = QtWidgets.QPushButton(Form)
        self.Prem_10.setEnabled(False)
        self.Prem_10.setGeometry(QtCore.QRect(30, 430, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.Prem_10.setFont(font)
        self.Prem_10.setStyleSheet("QPushButton{\n"
"        border : 0px;\n"
"        background: #642e60;\n"
"        color:white;\n"
"        border-radius: 8px;\n"
"        pading-down:2px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:rgba(186, 186, 186, 0.15);\n"
"}")
        self.Prem_10.setObjectName("Prem_10")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 564, 721, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: transparent;\n"
"color: white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(760, 580, 16, 16))
        self.label_5.setStyleSheet("background: transparent;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/wait.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(780, 580, 16, 16))
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/wait.png"))
        self.label_6.setObjectName("label_6")
        self.label_4.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.Prem_1.raise_()
        self.pushButton_2.raise_()
        self.AboutBtn.raise_()
        self.Prem_2.raise_()
        self.Prem_3.raise_()
        self.Prem_4.raise_()
        self.Prem_5.raise_()
        self.label_2.raise_()
        self.Prem_6.raise_()
        self.Prem_7.raise_()
        self.Prem_8.raise_()
        self.Prem_9.raise_()
        self.Prem_10.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GUIController PRO"))
        self.label.setText(_translate("Form", "Теплоком ПРЭМ"))
        self.pushButton.setText(_translate("Form", "Установить свзять "))
        self.Prem_1.setText(_translate("Form", "Ячейка 10"))
        self.pushButton_2.setText(_translate("Form", "Канал связи"))
        self.AboutBtn.setText(_translate("Form", "Help(H)"))
        self.Prem_2.setText(_translate("Form", "Ячейка 10"))
        self.Prem_3.setText(_translate("Form", "Ячейка 10"))
        self.Prem_4.setText(_translate("Form", "Ячейка 10"))
        self.Prem_5.setText(_translate("Form", "Ячейка 10"))
        self.label_2.setText(_translate("Form", "Теплоком ПРЭМ"))
        self.Prem_6.setText(_translate("Form", "Ячейка 10"))
        self.Prem_7.setText(_translate("Form", "Ячейка 10"))
        self.Prem_8.setText(_translate("Form", "Ячейка 10"))
        self.Prem_9.setText(_translate("Form", "Ячейка 10"))
        self.Prem_10.setText(_translate("Form", "Ячейка 10"))
        self.label_3.setText(_translate("Form", "Ожидание подключения"))
