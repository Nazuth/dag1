print('Mysql')

import mysql

dbconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='pythondb'
)

mycursor = dbconnection.cursor()
mycursor.execute('SELECT * FROM persons')
regels = mycursor.fetchall()
print(regels)