# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mqtt1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pub_py2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 311, 141))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 91, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 351, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setStyleSheet("color:red")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 210, 221, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 220, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.buttonClicked1)
        self.pushButton_3.clicked.connect(self.buttonClicked2)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Version1.0-张玮"))
        self.label_3.setText(_translate("Form", "发布到百度云"))
        self.label_4.setText(_translate("Form", "输入上传的值"))
        self.pushButton.setText(_translate("Form", "发布"))
        self.pushButton_2.setText(_translate("Form", "联接百度云"))
        self.label_6.setText(_translate("Form", "百度云发布与接收验序程Python版"))
        self.pushButton_3.setText(_translate("Form", "查询云上的值"))
    def buttonClicked(self):
        strr=self.lineEdit.text()
        pub_py2.publish(strr)

    def buttonClicked1(self):
        pub_py2.connect()
    def buttonClicked2(self):
        pub_py2.on_message()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
