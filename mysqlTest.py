import mysql.connector as mysqlc
mydb = mysqlc.connect(
  host="172.16.3.190",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="mypassw0000"   # 数据库密码
)
print(mydb)
mycursor = mydb.cursor()
# 创建数据库
# mycursor.execute("CREATE DATABASE test_db")
# 查看数据库
mycursor.execute("SHOW DATABASES")
## 输出游标内容
for x in mycursor:
  print(x)
# 关闭数据库连接
mydb.close()