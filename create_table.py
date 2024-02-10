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
            create table student
            (
                roll varchar(4),
                name varchar(40)
            )
           """
mycursor.execute(sqlquery)
print("Create table successful")




