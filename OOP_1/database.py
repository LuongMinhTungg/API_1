import mysql.connector

class Database:
    def db(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='oop_1'
        )
        return mydb