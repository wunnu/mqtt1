# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import pymysql
import sys

from pymysql import Connection
###################
import py03

def mysql_read(n):
    conn = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
    cursor = pymysql.cursors.SSCursor(conn)
    n=1
    sql = 'select '+'3,'*+' from bb'
    #sql = 'select * from bb limit '+n+',1'
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)
    print('读出成功！')
    cursor.close()
    conn.close()
    return row
######################################

