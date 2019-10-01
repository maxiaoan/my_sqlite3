import sqlite3
import  time
import  datetime
import  random

conn = sqlite3.connect("tutorial.db")

cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword, value REAL)")

def data_entry():
    cursor.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2019-9-30 11:11:39','python',6)")
    conn.commit()
    cursor.close()
    conn.close()

def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Python"
    value = random.randrange(0, 10)
    cursor.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    cursor.execute("SELECT * FROM stuffToPlot")
    data = cursor.fetchall()
    #print(data)
    for row in data:
        print(row)


read_from_db()

cursor.close()
conn.close()