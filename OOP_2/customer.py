from flask import jsonify
from database import database as db


class Customer:
    mydb = db().db()
    mycusor = mydb.cursor()

    def show_cus(self):
        try:
            self.mycusor.execute('select * from oop_2.customer')
            acc = self.mycusor.fetchall()
            output = []
            for i in acc:
                acc_data = {'name': i[1], 'phone': i[2]}
                output.append(acc_data)
            return jsonify({'list':output})
        except Exception as e:
            self.mydb.rollback()
            return jsonify({'error': e})


    def add_cus(self, name, phone):
        try:
            self.mycusor.execute('insert into oop_2.customer (name, phone) values(%s,%s)', (name, phone))
            self.mydb.commit()
            return 'add'
        except Exception as e:
            self.mydb.rollback()
            return jsonify({'error': e})