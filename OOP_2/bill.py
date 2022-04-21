from flask import jsonify
from database import database as db
import datetime
from product import Product as P
class Bill:
    mydb = db().db()
    mycusor = mydb.cursor()
    list = []

    def add_bill(self,cus_id):
        try:
            if self.check_cus_id(cus_id) == False:
                return 'None'
            else:
                time = datetime.datetime.now()
                self.mycusor.execute('insert into oop_2.bill (cus_id,time) values(%s,%s)', (cus_id,time))
                self.mydb.commit()
                return 'add'
        except Exception as e:
            self.mydb.rollback()
            return 'None'

    def add_bill_info(self,bill_id,pro_id,price,count):
        self.mycusor.execute('insert into oop_2.bill_info (bill_id, pro_id, price, count) values (%s,%s,%s,%s)',(bill_id,pro_id,price,count))
        self.mydb.commit()
        return 'add'

    def show_bill(self, bill_id):
        try:
            self.mycusor.execute('select * from oop_2.bill where bill_id = %s',(bill_id, ) )
            acc = self.mycusor.fetchall()
            output = []
            for i in acc:
                acc_data = {'cus_id': i[1], 'time':[2]}
                output.append(acc_data)
            if len(output) == 0:
                return 'None'
            else:
                return jsonify(output)
        except Exception:
            self.mydb.rollback()
            return 'Error'

    def show_bill_info(self, bill_id):
        try:
            self.mycusor.execute('select * from oop_2.bill_info where bill_id = %s',(bill_id, ) )
            acc = self.mycusor.fetchall()
            output = []
            for i in acc:
                acc_data = {'bill_id': i[1], 'pro_id':i[2], 'price':i[3], 'count':i[4]}
                output.append(acc_data)
            if len(output) == 0:
                return 'None'
            else:
                return jsonify(output)
        except Exception as e:
            self.mydb.rollback()
            return 'None'

    def check_cus_id(self, cus_id):
        try:
            self.mycusor.execute('select * from oop_2.customer where id = %s ', (cus_id,))
            cus = self.mycusor.fetchall()
            if len(cus) == 1:
                return True
            else:
                return False
        except Exception as e:
            return 'None'

    def check_bill_id(self,bill_id):
        self.mycusor.execute('select * from oop_2.bill where bill_id = %s', (bill_id,))
        bill = self.mycusor.fetchall()
        if len(bill) == 1:
            return True
        else:
            return False

    def check_pro_id(self,bill_id,pro_id):
        self.mycusor.execute('select * from oop_2.bill_info where pro_id = %s and bill_id = %s',(pro_id,bill_id))
        pro = self.mycusor.fetchall()
        if len(pro) == 1:
            return True
        else:
            return False

    def sell(self,bill_id,pro_id,count):
        try:
            self.mycusor.execute('select price from oop_2.product where id = %s',(pro_id,))
            price = self.mycusor.fetchone()
            if self.check_bill_id(bill_id) == True:
                if self.check_pro_id(bill_id,pro_id) == True:
                    self.mycusor.execute('select count from oop_2.bill_info where bill_id = %s and pro_id = %s', (bill_id,pro_id))
                    c = self.mycusor.fetchone()
                    new_count = count + c[0]
                    self.mycusor.execute('update oop_2.bill_info set count = %s where bill_id = %s and pro_id = %s ',(new_count,bill_id,pro_id))
                    self.mydb.commit()
                    return 'add'
                else:
                    return self.add_bill_info(bill_id, pro_id, price[0], count)
            else:
                return 'None'
            #P.delete_pro(P, pro_id)
            #return jsonify({'bill':self.show_bill(bill_id), 'bill_info':self.show_bill_info(bill_id)})

        except Exception as e:
            self.mydb.rollback()
            return 'None'


    def discount(self,cus_id):
        sql = 'select count(bi.pro_id) from oop_2.bill as b, oop_2.bill_info as bi where b.cus_id = %s and b.bill_id = bi.bill_id '
        self.mycusor.execute(sql,(cus_id,))
        num_dis = self.mycusor.fetchone()
        if num_dis[0] <= 5:
            return 1
        else:
            return 0
