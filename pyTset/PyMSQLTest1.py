import pymysql

#https://www.cnblogs.com/wancy/p/17515675.html


arg_kwargs={
    'host':"10.10.10.9",
    'port':3306,
    'user':'root',
    'password':"123456",
    'database':"mydb1",
    #'charset':'utf8'
}
#1.连接数据库，并得到Connection对象
db=pymysql.connections.Connection(**arg_kwargs)
#2.创建数据库的游标
cur=db.cursor()
#3.sql语句
sql = "INSERT INTO app_myuser (username, passwd) VALUES (%s,%s)"
val =[("yone1", "12sdf1"),('good','goodddps')]


#4.执行sql语句（其实是将sql语句提交给mysql数据库执行，执行后返回结果）
try:
    cur.executemany(sql,val)#是一个可迭代对象,返回一个int类型,为Number of affected rows.  注：execute单个，executemany多个
except Exception as e:
    print(e)
    db.rollback()
    #查询不需要rollback，因为select不需要commit
else:
    """
        分别获取一条记录数据、多条记录、所有记录
        one=cur.fetchone()
        many=cur.fetchmany(2)
        all=cur.fetchall()
    """

    print("sql执行成功")

    all=cur.fetchall()
    for row in all:
        print(row)
     
    db.commit()

  
finally:
    cur.close()#先关闭cur
    db.close()#再关闭db
