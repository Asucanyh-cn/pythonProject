'''
encoding:utf-8
author:yh
date:2023/2/15 10:25
'''

import mysql.connector as mysqlc
mydb=mysqlc.connect(
    # host="192.168.31.5",
	host="10.10.1.5",
    user="mysql",
    passwd="mypassw0000",
    # database=""
    # auth_plugin='mysql_native_password'
)
print(mydb)
mycursor = mydb.cursor()
def showDbs():
    # 列出数据库
    print('显示所有数据库：')
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
def showTbs():
    print('显示所有表：')
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
def showRcs(s):
    print('表'+s+'中的记录：')
    sql="SELECT * FROM "+s
    mycursor.execute(sql)
    for x in mycursor:
        print(x)
mycursor.execute("CREATE DATABASE IF NOT EXISTS managerSys")
mycursor.execute("USE managerSys")
mycursor.execute("CREATE TABLE IF NOT EXISTS users (username char(16) primary key,password char(32))")
# mycursor.execute("INSERT INTO users (username,password) VALUES ('usr','mypassword')")
mydb.commit() # 所有更新操作都要执行commit
showDbs()
showTbs()
showRcs('users')
