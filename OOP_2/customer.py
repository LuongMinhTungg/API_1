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
                acc_data = {'id':i[0],'name': i[1], 'phone': i[2]}
                output.append(acc_data)
            if len(output) == 0:
                return 'None'
            else:
                return jsonify(output)
        except Exception as e:
            self.mydb.rollback()
            return 'None'


    def add_cus(self, name, phone):
        try:
            self.mycusor.execute('insert into oop_2.customer (name, phone) values(%s,%s)', (name, phone))
            self.mydb.commit()
            return 'add'
        except Exception as e:
            self.mydb.rollback()
            return 'none'

    def check_cus_id(self, cus_id):
        try:
            self.mycusor.execute('select * from oop_2.customer where id = %s ', (cus_id,))
            cus = self.mycusor.fetchall()
            if len(cus) == 0:
                return False
            else:
                return True
        except Exception as e:
            return 'None'
