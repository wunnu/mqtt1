import test20
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class MyWindow(QMainWindow, test20.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())