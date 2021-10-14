import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student_table")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)