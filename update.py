import mysql.connector

db_name = "python_test_db"
mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root3306",
    database = db_name
)

mycursor = mydbconnection.cursor()
sqlquery = """
          update student 
          set name = "My name is shafi"
          where name = "stdname"
           """

mycursor.execute(sqlquery)
mydbconnection.commit()
print("update table successful")




