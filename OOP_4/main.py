from database import database as db
from flask import Flask, jsonify, request
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
    data = request.get_json()
    acc_number = data['acc_number']
    amount = data['amount']
    category = data['category']
    cus_id = data['cus_id']
    link = data['link']
    if V.vali_add_acc(data) == True:
        return A.add_acc(acc_number, amount, category, cus_id, link)
    else:
        return V.vali_add_acc(data)

@app.route('/show_saving_acc')
def show_sa():
    return A.show_saving_acc()

@app.route('/show_current_acc')
def show_ca():
    return A.show_current_acc()

@app.route('/deposit', methods = ['POST'])
def deposit():
    data = request.get_json()
    acc_number = data['acc_number']
    money = data['money']
    if V.vali_deposit(data) == True:
        return A.deposit(acc_number,money)
    else:
        return V.vali_deposit(data)

@app.route('/add_cus', methods = ['POST'])
def add_cus():
    try:
        data = request.get_json()
        name = data['name']
        if V.vali_add_cus(data) == True:
            return C.add_cus(name)
        else:
            return V.vali_add_cus(data)
    except Exception as e:
        return 'None'

@app.route('/withdrawal', methods = ['POST'])
def withdrawal():
    data = request.get_json()
    acc_number = data['acc_number']
    money = data['money']
    if V.vali_deposit(data) == True:
        return A.withdrawal(acc_number, money)
    else:
        return V.vali_deposit(data)

@app.route('/update_link', methods = ['POST'])
def update_link():
    data = request.get_json()
    sa_acc_number = data['sa_acc_number']
    ca_acc_number = data['ca_acc_number']
    link = data['link']
    if V.vali_up_link(data) == True:
        return A.update_link(link,sa_acc_number,ca_acc_number)
    else:
        return V.vali_deposit(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1010')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/