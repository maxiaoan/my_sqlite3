import sqlite3

conn = sqlite3.connect("tutorial.db")

cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword, value REAL)")

def data_entry():
    cursor.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2019-9-30 11:11:39','python',6)")
    conn.commit()
    cursor.close()
    conn.close()

create_table()
data_entry()