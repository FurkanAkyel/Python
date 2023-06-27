import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

#cursor.execute("""CREATE TABLE DATABASE(
#    name text,
#    lastname text,
#    age integer
#    )""")

def insert(name,lastname,age):
    addDatabase = """INSERT INTO DATABASE VALUES {}"""
    data = (name, lastname, age)
    cursor.execute(addDatabase.format(data))

nameadder,lnameadder,ageadder = input("Name = "),input("Last Name = "),input("age = ")
insert(nameadder,lnameadder,ageadder)

conn.commit()
conn.close()