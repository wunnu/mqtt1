
import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pymysql import Connection

file = open("472.txt","r",errors='ignore',encoding="utf8")   #设置文件对象

try:
    while True:
        text_line = file.readlines()
        if text_line:
            print(text_line)



            b=0
            while b<200:
                print("dddd")
                b = b + 1
                conn = Connection(host='localhost', user='root', password='1234abcd', port=3306, database='test')
                cursor = conn.cursor()
                a = text_line[b]
                print(len(text_line))
                strr = "'" + a + "'"
                print(strr)
                stri = 'insert into aa(inerpret) values' + '(' + strr + ')'

                print(stri)
                cursor.execute(stri)
                conn.commit()
                print('插入成功！')
                cursor.close()
                conn.close()

        else:
            break
finally:
    file.close()
