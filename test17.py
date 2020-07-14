
import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pymysql import Connection

file = open("492.txt","r",errors='ignore',encoding="utf8")   #设置文件对象

try:
    while True:
        text_line = file.readline()
        if text_line:

            conn = Connection(host='localhost', user='root', password='1234abcd', port=3306, database='test')
            cursor = conn.cursor()

            a = text_line
            strr = "'" + a + "'"
            #print(strr)
            stri = 'insert into bb(na) values' + '(' + strr + ')'

            print(stri)
            cursor.execute(stri)
            conn.commit()
            print('插入成功！')
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())






        else:
            break
finally:
    file.close()
