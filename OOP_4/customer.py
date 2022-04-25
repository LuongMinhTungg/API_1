from flask import jsonify
from database import database as db

class Customer:
    mydb = db().db()
    mycusor = mydb.cursor()
    list = []

    def num_acc(self, name):
        self.mycusor.execute('select count(*) from oop_4.customer where name = %s', (name, ))
        amount = self.mycusor.fetchall()
        a = []
        for i in amount:
            a.append(i)
        return a[0][0]

    def add_cus(self,name):
        self.mycusor.execute('insert into oop_4.customer (name) values (%s)',(name, ))
        self.mydb.commit()
        return 'add'

    def show_cus(self):
        self.mycusor.execute('select * from oop_4.customer')
        cus = self.mycusor.fetchall()
        output = []
        for i in cus:
            cus_data = {'cus_id':i[0], 'name':i[1], 'count_acc':i[2]}
            output.append(cus_data)
        return jsonify(output)