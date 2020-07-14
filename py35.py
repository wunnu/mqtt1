import pymysql
def conn1(n):
    conn = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
    cursor = pymysql.cursors.SSCursor(conn)
    #n='1'
    sql = 'select id from ff where name like '+'\''+n+'%'+'\''
    #sql = 'select * from dd limit '+n+',1'
    #sql='SELECT @rowNum:=@rowNum + 1 AS "temp",a.* FROM dd a,(SELECT @rowNum:=0) b LIMIT 1'
    #sql='select # from ff where name like '

    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)
    print('读行号成功！')
    cursor.close()
    conn.close()
    return row

def conn2(h):
    conn = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
    cursor = pymysql.cursors.SSCursor(conn)
    #n='1'
    sql = 'select name from ff where id like '+'\''+h+'%'+'\''
    #sql = 'select * from dd limit '+n+',1'
    #sql='SELECT @rowNum:=@rowNum + 1 AS "temp",a.* FROM dd a,(SELECT @rowNum:=0) b LIMIT 1'
    #sql='select # from ff where name like '

    cursor.execute(sql)
    row1 = cursor.fetchone()
    print(row1)
    print('读内容成功！')
    cursor.close()
    conn.close()
    return row1

def insert1(f,b):
    conn1 = pymysql.connect(host='localhost', user='root', password='1234abcd', db='test', charset='utf8')
    cursor = pymysql.cursors.SSCursor(conn1)
    #n='1'
    #sql = 'select na from bb where na like '+'\''+n+'%'+'\''
    #sql = 'select * from dd limit '+n+',1'
    #sql='SELECT @rowNum:=@rowNum + 1 AS "temp",a.* FROM dd a,(SELECT @rowNum:=0) b LIMIT 1'
    #sql='select # from ff where name like '

    sql='insert into dd(id,inter) values('+f+','+'\''+b+'\''+')'
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
    m2=m1.replace('(','')

    m3=m2.replace(',)','')
    print (m3)
    return m3

def str_handle1(m):
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
d=1
while d<7840:

    n=str(d)
    n1=str(int(n)+1)

    context_pre = conn1(n)
    c1=str_handle(context_pre)
    print(c1)

    context_lat=conn1(n1)
    c2=str_handle(context_lat)
    print(c2)
    c3=int(c2)-int(c1)
    print(c3)

    i=1
    while i<c3:
        n2=str(int(c1)+i)
        context=conn2(n2)
        insert1(n,str_handle1(context))
        i+=1
    d+=1