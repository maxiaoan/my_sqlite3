import mysqlite3

conn = mysqlite3.connect("mrsoft.db")

cursor = conn.cursor()

#sql ="create table user(id int(10) primary key , name varchar(20))"

#cursor.execute(sql)
cursor.execute('insert into user (id, name) values ("1","MRSOFT")')
cursor.execute('insert into user (id, name) values ("2","Anday")')
cursor.execute('insert into user (id, name) values ("3","马小安")')

cursor.execute("select * from user")


result3 = cursor.fetchall()

for i in result3:
    print(i[0],"\t",i[1])


cursor.close()

conn.close()