# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Py.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QLineEdit

class Ui_Form(object):
    Form = QtWidgets.QWidget()
    def __init__(self):
        super().__init__()
        self.initUI()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(692, 481)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 200, 651, 161))
        self.textEdit.setObjectName("textEdit")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(480, 70, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(480, 120, 75, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(80, 390, 75, 23))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(490, 390, 75, 23))
        self.pushButton4.setObjectName("pushButton4")
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(372, 70, 81, 20))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(232, 120, 221, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.radioButton1 = QtWidgets.QRadioButton(Form)
        self.radioButton1.setGeometry(QtCore.QRect(170, 390, 89, 16))
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton2 = QtWidgets.QRadioButton(Form)
        self.radioButton2.setGeometry(QtCore.QRect(570, 390, 89, 16))
        self.radioButton2.setObjectName("radioButton2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 80, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 54, 12))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        #self.pushButton1.clicked.connect(self,Form.pushButton1_clicked)
        #self.pushButton1.clicked.connect(Form.pushButton1_clicked)
        #btn1.clicked.connect(self.buttonClicked)
        #self.pushButton2.clicked.connect(Form.pushButton2_clicked)
        #self.pushButton3.clicked.connect(Form.pushButton3_clicked)
        #self.pushButton4.clicked.connect(Form.pushButton4_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def pushButton1_clicked(self,form):
        print('dd')
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "选择"))
        self.pushButton2.setText(_translate("Form", "查看解释"))
        self.pushButton3.setText(_translate("Form", "<--前一个"))
        self.pushButton4.setText(_translate("Form", "下一个-->"))
        self.radioButton1.setText(_translate("Form", "显示解释"))
        self.radioButton2.setText(_translate("Form", "显示解释"))
        self.label.setText(_translate("Form", "输入第几个单词"))
        self.label_2.setText(_translate("Form", "显示单词"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

