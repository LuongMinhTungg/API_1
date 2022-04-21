from cerberus import Validator
class Validate:
    def vali_add_acc(self,data):
        schema = {'name': {'type': 'string', 'empty': False, 'minlength': 1, 'maxlength': 45},
                  'amount':{'type': 'float', 'empty': False, 'min': 1},
                  'number': {'type': 'string', 'empty': False, 'regex': r'[0-9]{3}'}}
        v = Validator(schema)
        if v.validate(data, schema):
            return True
        else:
            return v.errors

    def vali_deposit(self,data):
        schema = {
                  'money': {'type': 'float', 'empty': False, 'min': 1},
                  'number': {'type': 'string', 'empty': False, 'regex': r'[0-9]{3}'}}
        v = Validator(schema)
        if v.validate(data, schema):
            return True
        else:
            return v.errors