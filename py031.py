import sys
from PyQt5 import QtWidgets
from py03 import Ui_MainWindow
import py032

class MyPyQT_Form(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def pushbutton_clicked(self):
        print('d')
        b=self.lineEdit.text()
        a=py032.mysql_read(b)
        print(a)
        self.lineEdit_2.setText(str(a))

    def pushbutton2_clicked(self):
        print('2')
        #self.textEdit.setText("你点击了按钮")
    def pushbutton3_clicked(self):
        print('3')
        #self.textEdit.setText("你点击了按钮")
    def pushbutton4_clicked(self):
        print('4')
        #self.textEdit.setText("你点击了按钮")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())