from flask import jsonify
from database import database as db


class Product:
    mydb = db().db()
    mycusor = mydb.cursor()

    def show_pro(self):
        try:
            self.mycusor.execute('select * from oop_2.product')
            acc = self.mycusor.fetchall()
            output = []
            for i in acc:
                acc_data = {'name': i[1], 'brand_name': i[2], 'category': i[3], 'price': i[4]}
                output.append(acc_data)
            if len(output) == 0:
                return 'None'
            else:
                return jsonify(output)

        except Exception as e:
            self.mydb.rollback()
            return jsonify({'error': e})

    def add_pro(self, name, brand_name, category, price):
        try:
            self.mycusor.execute('insert into oop_2.product (name, brand_name, category, price) values(%s,%s,%s,%s)', (name, brand_name, category, price))
            self.mydb.commit()
            return 'add'
        except Exception as e:
            self.mydb.rollback()
            return jsonify({'error': e})

    def delete_pro(self,id):
        try:
            self.mycusor.execute('DELETE FROM oop_2.product WHERE id = %s', (id,))
            self.mydb.commit()
            return 'delete'
        except Exception as e:
            self.mydb.rollback()
            return jsonify({'error': e})


