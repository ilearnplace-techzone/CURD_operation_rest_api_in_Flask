import json
from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)
mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="vicky1598",
         database="regester"
      )

mycursor = mydb.cursor()

@app.route('/')
def home():
    return ('welcome home')


@app.route('/signup', methods=['POST'])
def insert_record():
    record = json.loads(request.data)
    userid = record["id"]
    username=record["user"]
    emails=record["email"]
    mobile=record["mob"]
    password=record["pass"]
    rpassword=record["rpass"]

    sql="INSERT INTO reg (id,user,email,mob,pass,rpass) VALUES (%s,%s,%s,%s,%s,%s)"
    val=(userid,username,emails,mobile,password,rpassword)
    print(sql)
    mycursor.execute(sql,val)

    mydb.commit()
    return jsonify(record)


@app.route('/update',methods=['PUT'])
def update_records():
    record = json.loads(request.data)
    userid = record["id"]
    username = record["user"]
    emails = record["email"]
    mobile = record["mob"]
    password = record["pass"]
    rpassword = record["rpass"]

    sql = "UPDATE reg SET user='{}',email='{}',mob='{}',pass='{}',rpass='{}' WHERE id='{}'".format(username,emails,mobile,password,rpassword,userid,)
    mycursor.execute(sql)
    mydb.commit()
    return jsonify("update successfull")

@app.route('/delete',methods=['DELETE'])
def delete_records():
    record = json.loads(request.data)
    userid=record["id"]

    sql = "DELETE FROM reg WHERE id = %s"
    val = (userid,)
    mycursor.execute(sql,val)
    mydb.commit()
    return jsonify("delete successfull")

@app.route('/select',methods=['GET'])
def select_record():
    sql = "select * from reg"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    result=[]
    for row in myresult :
        row_dict={"user":row[0],"email":row[1],"mob":row[2],"pass":row[3],"rpass":row[4]}
        result.append(row_dict)
    return jsonify(result)



app.run(debug=True)
