import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='atikmujawar',
    database='py1'
)

mycursor = mydb.cursor()


# mycursor.execute("create database py1")
# mycursor.execute("use py1")
# mycursor.execute("create table py (name varchar(10), class varchar(10), rollno int(5))")

# sql = "INSERT INTO py (name, class, rollno) VALUES (%s, %s, %s)
# val = ("Mike", "SE-5", "1")
# # mycursor.execute(sql, val)
# sql2 = "INSERT INTO py (name, class, rollno) VALUES (%s, %s, %s)"
# val2 = ("Jack", "SE-5", "2")
# mycursor.execute(sql2, val2)
# sql3 = "INSERT INTO py (name, class, rollno) VALUES (%s, %s, %s)"
# val3 = ("Billy", "SE-5", "3")
# mycursor.execute(sql3, val3)
# mydb.commit()
mycursor.execute("select * from py")
print("Table Contents")
res=mycursor.fetchall()
for x in res:
    print(x)
print(mycursor.rowcount, "record inserted.")

# sql4 = "update py set class='SE-6' where name='Billy'"
# mycursor.execute(sql4)

# sql5 = "update py set rollno='1' where name='Mike'"
# mycursor.execute(sql5)
print("")
mycursor.execute("select * from py")
print("Table Contents")
res=mycursor.fetchall()
for x in res:
    print(x)
print(mycursor.rowcount, "Updated Table")