import sqlite3
conn = sqlite3.connect("Fugle_db.db")
c = conn.cursor()

t = input("Type: ")
att = input("Attribute: ")

sql = ("SELECT Fugl FROM Fugle WHERE "+str(t)+" LIKE '"+str(att)+"'")
print(sql)
Fugle_var = c.execute(sql)
print(Fugle_var)
Fugle_var = c.fetchall()
print(Fugle_var)
c.close()