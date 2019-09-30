import pymysql

db = pymysql.connect("localhost", "root","1231")

cursor = db.cursor()

#cursor.execute("create database mrsoft character set utf8;")

cursor.execute("use mrsoft")

#sql ="create table user(id int(10) primary key , name varchar(20))"
#cursor.execute(sql)

cursor.execute('insert into user (id, name) values ("1","MRSOFT")')
cursor.execute('insert into user (id, name) values ("2","Anday")')
cursor.execute('insert into user (id, name) values ("3","马小安")')


cursor.execute("select * from user")
users = cursor.fetchall()
print(users)

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database verson: %s" % data)

database = cursor.execute("SHOW DATABASES;")
print("existed databases %s " % database)

db.close()