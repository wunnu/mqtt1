
import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pymysql import Connection

file = open("479.txt","r",errors='ignore',encoding="utf8")   #设置文件对象


text_line = file.readline().strip()

print(text_line)

conn = Connection(host='localhost', user='root', password='1234abcd', port=3306, database='test')
cursor = conn.cursor()
a = text_line
print(a)
strr = "'" + a + "'"
print(strr)
stri = 'insert into aa(name) values' + '(' + strr + ')'
print(stri)
cursor.execute(stri)
conn.commit()
print('插入成功！')
cursor.close()
conn.close()

file.close()
