import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="uriahby", passwd="55690122", database = "uriahby")

mycursor = mydb.cursor()
mycursor.execute("select * from student")

result = mycursor.fetchall()
for i in result:
    print(i)



mydb.close()