# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector as conn

# connecting to database and creating a database
try:
    dataBase = conn.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'rose'
    )
except conn.Error as error:
    print(f"An error occurred: {error}")
else:
    curserObejct = dataBase.cursor()
    create_database = curserObejct.execute('CREATE DATABASE IF NOT EXISTS spottech')
    if create_database:
        print("Database created!")
    else:
        print("Database you want to create already exists!")
        print("All done!")
