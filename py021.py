import sys
from PyQt5 import QtWidgets
from py02 import Ui_Form

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def pushButton_clicked(self):




        #self.textEdit.setText("你点击了按钮")
    def pushButton2_clicked(self):
        print('2')
        #self.textEdit.setText("你点击了按钮")
    def pushButton3_clicked(self):
        print('3')
        #self.textEdit.setText("你点击了按钮")
    def pushButton4_clicked(self):
        print('4')
        #self.textEdit.setText("你点击了按钮")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())