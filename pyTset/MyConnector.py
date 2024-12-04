from sqlite3 import Cursor
import mysql.connector

conn = mysql.connector.connect(
    host='10.10.10.9',
    user='root',
    password='123456',
    database='mydb'
)


cursor = conn.cursor()


print("数据库连接成功")


sql = "SELECT * FROM users"

# 执行查询
cursor.execute(sql)

# 获取查询结果
results = cursor.fetchall()

for row in results:
    print(row)



"""
# 插入数据
sql = "INSERT INTO users (name, age,email) VALUES (%s, %s,%s)"
val = ("dfly", "30","dfly@alongdf.cn")
cursor.execute(sql,val)

conn.commit()


sql = "DELETE FROM users WHERE id=8"
cursor.execute(sql)
conn.commit()

"""

cursor.close()
conn.close()
