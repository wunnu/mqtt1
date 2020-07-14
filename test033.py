# _*_ coding:utf-8 _*_

# 导入模块
import pymysql
# 1.连接到mysql数据库
conn = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
cursor = pymysql.cursors.SSCursor(conn)


sql = "select * from bb limit 0,1"
cursor.execute(sql)
row = cursor.fetchone()
print(row)
print('读出成功！')
cursor.close()
conn.close()