from flask import jsonify
from database import database as db



class Account:
    mydb = db().db()
    mycusor = mydb.cursor()
    list = []

    def add_saving_acc(self, acc_number, profits):
        self.mycusor.execute('insert into oop_4.saving_acc (acc_number, profits) values(%s,%s)', (acc_number, profits))
        self.mydb.commit()
        return 'add'

    def add_current_acc(self, acc_number):
        self.mycusor.execute('insert into oop_4.current_acc (acc_number) values(%s)', (acc_number,))
        self.mydb.commit()
        return 'add'

    def show_saving_acc(self):
        self.mycusor.execute('select * from oop_4.saving_acc ')
        saving_acc = self.mycusor.fetchall()
        output = []
        for i in saving_acc:
            data_sa = {'acc_number':i[1],'profits':i[2], 'link':i[3]}
            output.append(data_sa)
        if len(output) == 0:
            return 'None'
        else:
            return jsonify({'saving acc': output})

    def show_acc(self):
        self.mycusor.execute('select * from oop_4.account')
        acc = self.mycusor.fetchall()
        output = []
        for i in acc:
            data_acc = {'acc_number':i[1],'amount':i[2],'cus_id':i[3]}
            output.append(data_acc)
        if len(output) == 0:
            return 'None'
        else:
            return jsonify({'account': output})

    def show_current_acc(self):
        self.mycusor.execute('select * from oop_4.current_acc ')
        saving_acc = self.mycusor.fetchall()
        output = []
        for i in saving_acc:
            data_ca = {'acc_number': i[1], 'link': i[2]}
            output.append(data_ca)
        if len(output) == 0:
            return 'None'
        else:
            return jsonify({'current acc': output})

    def count_account(self, cus_id):
        try:
            self.mycusor.execute('select count_acc from oop_4.customer where cus_id = %s', (cus_id,))
            count_acc = self.mycusor.fetchone()
            new_count_acc = count_acc[0] + 1
            self.mycusor.execute('update oop_4.customer set count_acc = %s where cus_id = %s', (new_count_acc, cus_id))
            self.mydb.commit()
            return 'update'
        except Exception as e:
            self.mydb.rollback()
            return 'None'

    def add_link(self,link):
        if link == 1:
            self.mycusor.execute('insert into ')

    def add_acc(self,acc_number, amount, category, cus_id):
        try:
            if self.checking_acc(acc_number) == True:
                return 'existed'
            else:
                self.mycusor.execute('insert into oop_4.account (acc_number, amount, cus_id) values(%s,%s,%s)', (acc_number, amount, cus_id))
                self.mydb.commit()
                self.count_account(cus_id)
                if category.upper() == "tktk".upper():
                    return self.add_saving_acc(acc_number, amount*8/100)
                elif category.upper() == "tkvl".upper():
                    return self.add_current_acc(acc_number)
        except Exception as e:
            self.mydb.rollback()
            return 'none'


    def checking_saving_acc(self, acc_number):
        self.mycusor.execute('select * from oop_4.saving_acc as sa, oop_4.account as a where sa.acc_number = a.acc_number and a.acc_number = %s', (acc_number, ))
        acc = self.mycusor.fetchall()
        if len(acc) == 1:
            return True
        else:
            return False

    def checking_current_acc(self, acc_number):
        self.mycusor.execute('select * from oop_4.current_acc as ca, oop_4.account as a where ca.acc_number = a.acc_number and a.acc_number = %s', (acc_number,))
        acc = self.mycusor.fetchall()
        if len(acc) == 1:
            return True
        else:
            return False

    def checking_acc(self, acc_number):
        self.mycusor.execute('select * from oop_4.account as a where acc_number = %s',
            (acc_number,))
        acc = self.mycusor.fetchall()
        if len(acc) == 1:
            return True
        else:
            return False

    def deposit(self, acc_number, money):
        try:
            if self.checking_acc(acc_number):
                self.mycusor.execute('Select amount from oop_4.account where acc_number = %s', (acc_number, ))
                amount = self.mycusor.fetchone()
                new_amount = amount[0] + float(money)
                self.update_amount(new_amount,acc_number)
                if self.checking_saving_acc(acc_number):
                    self.mycusor.execute('update oop_4.saving_acc set profits = %s where acc_number = %s', (new_amount*8/100,acc_number))
                    self.mydb.commit()
                return 'deposit'
            else:
                return 'not exist'
        except Exception as e:
            self.mydb.rollback()
            return 'None'

    def select_amount(self,str,acc_number):
        sql = ('select amount from '+str+' where acc_number = %s')
        self.mycusor.execute(sql,(acc_number,))
        amount = self.mycusor.fetchall()
        a = []
        for i in amount:
            a.append(i)
        amount = a[0][0]
        return amount

    def check_link(self, ca_acc_number):
        self.mycusor.execute('select * from oop_4.saving_acc as sa, oop_4.current_acc as ca where sa.link = ca.link and ca.acc_number = %s', (ca_acc_number,))
        acc = self.mycusor.fetchall()
        if len(acc) == 0:
            return False
        else:
            return True

    def update_amount(self,new_amount,acc_number):
        self.mycusor.execute('update oop_4.account set amount = %s where acc_number = %s', (new_amount, acc_number))
        self.mydb.commit()
        return 'update'

    def update_profits(self,profits,acc_number):
        self.mycusor.execute('update oop_4.saving_acc set profits = %s where acc_number = %s',(profits,acc_number))
        self.mydb.commit()
        return 'update'

    def withdrawal(self, acc_number, money):
        try:
            if self.checking_saving_acc(acc_number):
                amount = self.select_amount('oop_4.account', acc_number)
                if amount >= money:
                    new_amount = amount - float(money)
                    self.update_amount(new_amount,acc_number)
                    self.update_profits(new_amount*8/100,acc_number)
                    return 'withdrawal'
                else:
                    return 'money > amount'
            elif self.checking_current_acc(acc_number):
                ca_amount = self.select_amount('oop_4.account', acc_number)
                if money <= ca_amount:
                    new_amount = ca_amount - float(money)
                    self.update_amount(new_amount,acc_number)
                    return 'withdrawal'
                else:
                    if self.check_link(acc_number):
                        self.mycusor.execute('select sa.acc_number from oop_4.saving_acc as sa, oop_4.current_acc as ca where ca.acc_number = %s and ca.link = sa.link', (acc_number,))
                        acc = self.mycusor.fetchone()
                        sa_acc_number = acc[0]
                        sa_amount = self.select_amount('oop_4.account', sa_acc_number)
                        if sa_amount + ca_amount >= money:
                            self.update_amount(0,acc_number)
                            new_amount_1 = money - ca_amount
                            self.update_amount(sa_amount - new_amount_1,sa_acc_number)
                            self.update_profits((sa_amount - new_amount_1)*8/100,sa_acc_number)
                            return 'withdrawal'
                        else:
                            return 'money > sa_amount + ca_amount'
                    else:
                        return 'not link'
            else:
                return 'not exist'
        except Exception as e:
            self.mydb.rollback()
            return 'none'

    def check_cus_id(self,sa_acc_number,ca_acc_number):
        self.mycusor.execute('select a.cus_id from oop_4.account as a, oop_4.saving_acc as sa, oop_4.current_acc as ca where a.acc_number = %s and sa.acc_number = %s and ca.acc_number = %s',(sa_acc_number,sa_acc_number,ca_acc_number))
        acc = self.mycusor.fetchall()
        if len(acc) == 0:
            return False
        else:
            return True

    def update_link(self, link, sa_acc_number, ca_acc_number):
        self.mycusor.execute('update oop_4.saving_acc set link = %s where acc_number = %s ', (link, sa_acc_number))
        self.mydb.commit()
        self.mycusor.execute('update oop_4.current_acc set link = %s where acc_number = %s ', (link, ca_acc_number))
        self.mydb.commit()
        return 'update'


    def set_link(self, sa_acc_number, ca_acc_number):
        try:
            if self.checking_acc(sa_acc_number) == True and self.checking_acc(ca_acc_number) == True:
                if self.check_cus_id(sa_acc_number,ca_acc_number) == True:
                    if self.check_link(ca_acc_number) == False:
                        self.mycusor.execute('select cus_id from oop_4.account where acc_number = %s ',(sa_acc_number,))
                        cus_id = self.mycusor.fetchone()
                        return self.update_link(cus_id[0],sa_acc_number,ca_acc_number)
                    else:
                        return 'link existed'
                else:
                    return 'none'
            else:
                return 'None'
        except Exception as e:
            self.mydb.rollback()
            return 'error'
