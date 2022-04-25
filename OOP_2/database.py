import mysql.connector
class database:
    def db(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='trafalgarlaw1910',
            port='3306',
            database='oop_2')
        return mydb

