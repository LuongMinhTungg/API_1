from database import Database as db
from flask import Flask, jsonify, request
from validate import Validate

V = Validate()
app = Flask(__name__)

mydb = db().db()
mycusor = mydb.cursor()


@app.route('/')
def index():
    return 'Hello'


@app.route('/account')
def list_account():
    mycusor.execute('select * from oop_1.account')
    acc = mycusor.fetchall()
    output = []
    for i in acc:
        acc_data = {'name': i[1], 'number': i[2], 'amount': i[3]}
        output.append(acc_data)
    if len(output) == 0:
        return 'None'
    else:
        return jsonify(output)


def checking_acc(number):
    mycusor.execute('select * from oop_1.account where number = %s', (number,))
    acc = mycusor.fetchall()
    if len(acc) == 1:
        return True
    else:
        return False

@app.route('/add_acc', methods=['POST'])
def add_acc():
    try:
        data = request.get_json()
        amount = data['amount']
        name = data['name']
        number = data['number']
        if checking_acc(number) == True:
            if V.vali_add_acc(data) == True:
                mycusor.execute("insert into oop_1.account(name, number, amount) values (%s, %s, %s)", (name, number, float(amount)))
                # commit the transaction
                mydb.commit()
                return 'add'
            else:
                return V.vali_add_acc(data)
        else:
            return 'None'
    except Exception as e:
        return 'None'


def search_acc(number):
    mycusor.execute('select * from oop_1.account where number = %s', (number,))
    acc = mycusor.fetchall()
    output = []
    for i in acc:
        acc_data = {'name': i[1], 'number': i[2], 'amount': i[3]}
        output.append(acc_data)
    return jsonify(output)


@app.route("/deposit", methods=['POST'])
def deposit():
    try:
        data = request.get_json()
        number = data['number']
        money = data['money']
        if V.vali_deposit(data) == True:
            if checking_acc(number) == False:
                return 'None'
            else:
                mycusor.execute('select amount from oop_1.account where number = %s', (number,))
                amount = mycusor.fetchone()
                new_amount = amount[0] + float(money)
                mycusor.execute('update oop_1.account set amount = %s where number = %s', (new_amount, number))
                mydb.commit()
                return search_acc(number)
        else:
            return V.vali_deposit(data)
    except Exception as e:
        return 'None'


@app.route("/withdrawal", methods=['POST'])
def withdrawal():
    try:
        data = request.get_json()
        number = data['number']
        money = data['money']
        if V.vali_deposit(data) == True:
            if checking_acc(number) == False:
                return 'none'
            else:
                mycusor.execute('select amount from oop_1.account where number = %s', (number,))
                amount = mycusor.fetchone()
                if (money) > amount[0]:
                    return 'None'
                else:
                    new_amount = amount[0] - (money)
                    mycusor.execute('update oop_1.account set amount = %s where number = %s', (new_amount, number))
                    mydb.commit()
                    return search_acc(number)
        else:
            return V.vali_deposit(data)
    except Exception as e:
        return 'None'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8686')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
