from cerberus import Validator
import validators
from urllib.parse import urlparse

from flask import Response


class Validate:
    def vali_add_acc(self,data):
        schema = {'acc_number': {'type': 'string', 'empty': False, 'regex': r'[0-9]{3}'},
                  'amount': {'type': 'float', 'empty': False, 'min': 1},
                  'category': {'type': 'string', 'empty': False,'allowed': ['tktk','tkvl'], 'minlength': 1, 'maxlength': 45},
                  'cus_id': {'type': 'integer', 'empty': False}}
        v = Validator(schema)
        if v.validate(data, schema):
            return True
        else:
            return v.errors

    def vali_add_cus(self,data):
        schema = {'name': {'type': 'string', 'empty': False, 'minlength': 1, 'maxlength': 45}}
        v = Validator(schema)

        if v.validate(data, schema) == True:
            return True
        else:
            return v.errors

    def vali_deposit(self,data):
        schema = {'acc_number': {'type': 'string', 'empty': False, 'regex': r'[0-9]{3}'},
                  'money': {'type': 'float', 'empty': False, 'min': 1}}
        v = Validator(schema)

        if v.validate(data, schema) == True:
            return True
        else:
            return v.errors

    def vali_set_link(self,data):
        schema = {'sa_acc_number': {'type': 'string', 'empty': False, 'regex': r'[0-9]{3}'},
                  'ca_acc_number': {'type': 'string', 'empty': False, 'regex': r'[0-9]{3}'}
                  }
        v = Validator(schema)

        if v.validate(data, schema) == True:
            return True
        else:
            return v.errors
