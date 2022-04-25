
from database import database as db
from flask import Flask, jsonify, request, Response
from acount import Account
from customer import Customer
from validate import Validate
V = Validate()
C = Customer()
A = Account()
app = Flask(__name__)
con = db().db()


@app.route('/')
def index():
    return 'Hello'



@app.route('/add_acc', methods = ['POST'])
def add_acc():
    try:
        data = request.get_json()
        acc_number = data['acc_number']
        amount = data['amount']
        category = data['category']
        cus_id = data['cus_id']
        if V.vali_add_acc(data) == True:
            return A.add_acc(acc_number, amount, category, cus_id)
        else:
            return V.vali_add_acc(data)
    except KeyError:
        return 'wrong key'

@app.route('/show_cus')
def show_cus():
    return C.show_cus()

@app.route('/show_saving_acc')
def show_sa():
    return A.show_saving_acc()

@app.route('/show_current_acc')
def show_ca():
    return A.show_current_acc()

@app.route('/show_acc')
def show_acc():
    return A.show_acc()

@app.route('/deposit', methods = ['POST'])
def deposit():
    try:
        data = request.get_json()
        acc_number = data['acc_number']
        money = data['money']
        if V.vali_deposit(data) == True:
            return A.deposit(acc_number,money)
        else:
            return V.vali_deposit(data)
    except KeyError:
        return 'wrong key'


@app.route('/add_cus', methods = ['POST'])
def add_cus():
    try:
        data = request.get_json()
        name = data['name']
        if V.vali_add_cus(data) == True:
            return C.add_cus(name)
        else:
            return V.vali_add_cus(data)
    except KeyError as e:
        return 'wrong key'

@app.route('/withdrawal', methods = ['POST'])
def withdrawal():

    try:
        data = request.get_json()
        acc_number = data['acc_number']
        money = data['money']
        if V.vali_deposit(data) == True:
            return A.withdrawal(acc_number, money)
        else:
            return V.vali_deposit(data)
    except KeyError:
        return 'wrong key'

@app.route('/set_link', methods = ['POST'])
def set_link():
    try:
        data = request.get_json()
        sa_acc_number = data['sa_acc_number']
        ca_acc_number = data['ca_acc_number']
        if V.vali_set_link(data) == True:
            return A.set_link(sa_acc_number, ca_acc_number)
        else:
            return V.vali_deposit(data)
    except KeyError:
        return 'wrong key'

@app.errorhandler(404)
def page_not_found(error):
    return 'wrong url'

@app.errorhandler(400)
def page_not_found(error):
    return 'bad request'

@app.errorhandler(405)
def page_not_found(error):
    return 'wrong methods'

@app.errorhandler(500)
def page_not_found(error):
    return 'sever error'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1010')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/