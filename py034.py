import pymysql
def conn1(n):
    conn = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
    cursor = pymysql.cursors.SSCursor(conn)
    #n='1'
    sql = 'select na from bb where na like '+'\''+n+'%'+'\''
    #sql = 'select * from dd limit '+n+',1'
    #sql='SELECT @rowNum:=@rowNum + 1 AS "temp",a.* FROM dd a,(SELECT @rowNum:=0) b LIMIT 1'
    #sql='select # from ff where name like '

    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)
    print('读出成功！')
    cursor.close()
    conn.close()
    return row

def insert1(f,b):
    conn1 = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
    cursor = pymysql.cursors.SSCursor(conn1)
    #n='1'
    #sql = 'select na from bb where na like '+'\''+n+'%'+'\''
    #sql = 'select * from dd limit '+n+',1'
    #sql='SELECT @rowNum:=@rowNum + 1 AS "temp",a.* FROM dd a,(SELECT @rowNum:=0) b LIMIT 1'
    #sql='select # from ff where name like '

    sql='insert into gg(id,name) values('+f+','+'\''+b+'\''+')'
    #sql = 'insert into gg(name) values("ddd")'
    try:
        # 执行sql语句
        cursor.execute(sql)

        # 取一行结果
        result = cursor.fetchone()

        # 打印
        print(result)
        # 提交事务
        conn1.commit()

    except pymysql.Error as e:
        print(e)

        # 若出现错误，则回滚
        conn1.rollback()


    #cursor.execute(sql)
    #row = cursor.fetchone()
    #print(row)
    print('写入成功！')
    cursor.close()
    conn1.close()



def str_handle(m):
    m1=str(m)
    m2=m1.replace('(\'','')

    m3=m2.replace(',)','')
    print (m3)
    m4=m3.replace('\'','')
    print(m4)
    m5=m4.replace('r','')
    m6=m5.replace('\\','')
    print(m6)
    return m6
i=1

while i<20 :
    n=str(i)
    context = conn1(n)

    insert1(n,str_handle(context))
    i=i+1