from database import database as db
from flask import Flask, jsonify, request
from customer import Customer
from product import Product
from bill import Bill
from validate import Sche
from cerberus import schema_registry, Validator

app = Flask(__name__)
con = db().db()

mycusor = con.cursor()
Pro = Product()
Cus = Customer()
Bill = Bill()
Sche = Sche()

@app.route('/')
def index():
    return 'Hello'

@app.route('/show_cus')
def show_cus():
    return Cus.show_cus()

@app.route('/show_pro')
def show_pro():
    return Pro.show_pro()

@app.route('/add_cus', methods = ['POST'])
def add_cus():
    try:
        data = request.get_json()
        name = data['name']
        phone = data['phone']

        if Sche.vali_add_cus(data) == True:
            return Cus.add_cus(name,phone)
        else:
            return jsonify(Sche.vali_add_cus(data))
    except KeyError:
        return 'key error'


@app.route('/add_pro', methods = ['POST'])
def add_pro():
    try:
        data = request.get_json()
        name = data['name']
        brand_name = data['brand_name']
        category = data['category']
        price = data['price']
        if Sche.vali_add_pro(data) == True:
            return Pro.add_pro(name,brand_name,category,price)
        else:
            return jsonify(Sche.vali_add_pro(data))
    except KeyError:
        return 'key error'

@app.route('/add_bill', methods = ['POST'])
def add_bill():
    try:
        data = request.get_json()
        cus_id = data['cus_id']
        if Sche.vali_add_bill(data) == True:
            return Bill.add_bill(cus_id)
        else:
            return jsonify(Sche.vali_add_bill(data))
    except KeyError:
        return 'key error'

@app.route('/sell',methods = ['POST'])
def sell():
    try:
        data = request.get_json()
        pro_id = data['pro_id']
        bill_id = data['bill_id']
        count = data['count']
        if Sche.vali_sell(data):
            return Bill.sell(bill_id, pro_id, count)
        else:
            return jsonify(Sche.vali_sell(data))
    except KeyError:
        return 'key error'

@app.route('/show_bill')
def show_bill():
    return Bill.show_bill()

@app.route('/show_bill_info_by_bill_id',methods = ['POST'])
def show_bill_info_by_bill_id():
    try:
        data = request.get_json()
        bill_id = data['bill_id']
        if Sche.vali_show_bill_info_by_bill_id(data) == True:
            return Bill.show_bill_info_by_id(bill_id)
        else:
            return Sche.vali_show_bill_info_by_bill_id(data)
    except KeyError:
        return 'key error'

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
    app.run(host='0.0.0.0', port='1111')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
