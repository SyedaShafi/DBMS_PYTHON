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
           insert into student(roll, name)
           values ('101', 'stdname')
           """

mycursor.execute(sqlquery)
mydbconnection.commit()
print("insert table successful")




