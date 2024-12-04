import pymysql
import hashlib

#执行sql语句
def my_sql(sql):
    #连接数据库
    conn=pymysql.connect(
        host='10.10.10.9',
        user='root',
        password='123456',
        db='mydb1',
        port=3306,
        charset='utf8',
        autocommit=True
    )#autocommit 自动提交sql

    cur=conn.cursor(pymysql.cursors.DictCursor)#建立游标,设置返回数据类型是字典
    cur.execute(sql)#执行sql
    res=cur.fetchone()#返回一条数据
    cur.close()#关闭游标
    conn.close()#关闭数据库
    return res

#加密
def my_md5(s,salt=''):#salt 加盐
    s = s + salt
    news=s.encode()#加密之前用 encode()变成二进制
    m=hashlib.md5(news) #加密
    return m.hexdigest() #返回密文

#注册
def reg():
    for i in range(3):
        print('欢迎注册'.center(50, '*'))
        user = input('账号：').strip().lower()  # 去除空格或换行符，输入的字母全部转为小写
        pd = input('密码：').strip()
        cpd = input('确认密码：').strip()
        sql='select username,passwd from app_myuser where username="%s";'%user
        # user_dic=my_sql(sql)
        if len(user) not in range(6, 11) or len(pd) not in range(6, 11):
            print('账号/密码长度必须在6-10之间')
        elif pd != cpd:
            print('两次输入的密码不一致')
        # elif user == user_dic['username']:
        elif my_sql(sql):#非空即真
            print('用户名重复！')
        else:  # 账号和密码合格则存入数据库，密码存入密文
            insert_sql='insert into app_myuser (username,passwd,is_admin) value ("%s","%s",1);'%(user,my_md5(pd))
            my_sql(insert_sql)
            print(user,my_md5(pd))
            print('注册成功'.center(50, '*'))
            break
    else:
        print('输入错误次数过多')

#登录
def login():
    for i in range(3):
        user = input('请输入登录账号：').strip().lower()
        pd = input('请输入密码：').strip()
        sql = 'select username,passwd from app_myuser where username="%s";'%user
        if user=="" or pd=="":
            print('账号/密码不能为空')
        else:
            user_dic = my_sql(sql)
            if user_dic:
                if my_md5(pd) == user_dic.get('passwd'):
                    print('登陆成功！')
                    break
                else:
                    print('密码错误！')
            else:
                print('用户不存在')
    else:
        print('错误次数较多，请稍后重新输入！')