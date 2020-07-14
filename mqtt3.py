# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mqtt1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pub_py2
import paho.mqtt.client as mqtt
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 220, 231, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(73, 260, 251, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 311, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 30, 101, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 91, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 351, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.buttonClicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.groupBox.setTitle(_translate("Form", "Version1.0-张玮"))
        self.label_5.setText(_translate("Form", "输入strength值"))
        self.label_3.setText(_translate("Form", "发布到百度云"))
        self.label_4.setText(_translate("Form", "输入Light值"))
        self.pushButton.setText(_translate("Form", "发布"))
        self.label_6.setText(_translate("Form", "百度云发布与接收验序程Python版"))
    def buttonClicked(self):

        a=self.lineEdit.text()
        self.label.setText(a)
        b=self.lineEdit_2.text()
        self.label_2.setText(b)
####################################
        pub_py2.connect()






if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())