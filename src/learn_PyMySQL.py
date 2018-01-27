import pymysql
##################################################################
# 数据库连接
# 打开数据库连接
db = pymysql.connect('localhost', 'root', '', 'study')
# 创建一个游标对象
cursor = db.cursor()
# 执行sql查询
cursor.execute("SELECT VERSION()")
# 获取单挑数据
data = cursor.fetchone()
print("DataBase Version %s" % data)
# 关闭数据库
db.close()
##################################################################
# #创建数据库表
# # 打开数据库
# db = pymysql.connect('localhost','root','','study')
# # 创建一个游标对象
# cursor = db.cursor()
# # 执行sql，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME CHAR(20) NOT NULL,
#          LAST_NAME CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT)"""
# # 执行
# cursor.execute(sql)
# # 关闭数据库连接
# db.close()
##################################################################
# # SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
# sql = """INSERT INTO
#                  EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
#          VALUES
#                  ('MAC','Mohan',20,'M',2000)"""
# # 数据库插入操作
# 打开数据库
# db = pymysql.connect("localhost","root","","study")
# # 创建游标
# cursor = db.cursor()
# for index in range(50):
#
#     # sql插入语句
#     sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#            LAST_NAME, AGE, SEX, INCOME) \
#            VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#            ('Mac' + str(index), 'Mohan' + str(index), 20 + index, 'M', 2000 + index)
#     try:
#         # 执行sql
#         cursor.execute(sql)
#         # 提交到数据库
#         db.commit()
#     except:
#         # 报错回滚
#         db.rollback()
#
# # 关闭数据库连接
# db.close()
##################################################################
# 数据库查询操作
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# 打开数据库
# db = pymysql.connect("localhost","root","","study")
# # 创建游标
# cursor = db.cursor()
# sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % 2035
# try:
#     cursor.execute(sql)
#     listResult = cursor.fetchall()
#     for row in listResult:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname,lname,age,sex,income))
# except:
#     print("Error:Unable to fetch data")
# db.close()
##################################################################
# 数据库更新操作
# 打开数据库
# db = pymysql.connect("localhost","root","","study")
# # 创建游标
# cursor = db.cursor()
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % 'M'
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()
##################################################################
# 删除操作
# # 打开数据库
# db = pymysql.connect("localhost","root","","study")
# # 创建游标
# cursor = db.cursor()
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % 35
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()
##################################################################
# 执行事务
# 事务机制可以确保数据一致性。
# 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
# 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
# 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
# Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
# 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
# commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
