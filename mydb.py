import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user =  'root',
    passwd = '1234'
)

# prepare a cusror object
cusrorObject = dataBase.cursor()

# create a database
cusrorObject.execute("CREATE DATABASE crm")

print("all done....")
    
