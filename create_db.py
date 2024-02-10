import mysql.connector

mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root3306"
)

print(mydbconnection)
db_name = "python_test_db"
mycursor = mydbconnection.cursor()
sqlquery = "create database " + db_name
mycursor.execute(sqlquery)

