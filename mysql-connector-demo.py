import mysql.connector
try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_demo"
    )
    mycusor=mydb.cusor()
    #mycusor.execute("CREATE DATABASE python_demo")
    mycusor.execute("SHOW DATABASES")

    for i in mycusor:
        print(i)
except e:
    print(e)