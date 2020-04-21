import sqlite3
conn = sqlite3.connect("Fugle_db.db")
c = conn.cursor()
t = input("Type: ")
att = input("Attribute: ")
sql = "SELECT * FROM Fugl WHERE "+str(t)+"="+str(att)
print(sql)
Fugle_var = c.execute(sql)
print(Fugle_var)