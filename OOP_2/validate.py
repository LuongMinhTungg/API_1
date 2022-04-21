from cerberus import schema_registry, Validator
class Sche:
    def vali_add_cus(self,data):
        schema = {'name': {'type': 'string', 'empty': False, 'minlength': 1, 'maxlength': 45},
                  'phone': {'type': 'string', 'empty': False, 'minlength': 10, 'maxlength': 11}}
        v = Validator(schema)

        if v.validate(data, schema):
            return True
        else:
            return v.errors

    def vali_sell(self,data):
        schema = {'pro_id': {'type': 'integer', 'empty': False, },
                  'pro_cus': {'type': 'integer', 'empty': False, },
                  'count': {'type':'integer', 'empty': False, 'min':1}}
        v = Validator(schema)

        if v.validate(data, schema):
            return True
        else:
            return v.errors

    def vali_add_pro(self,data):
        schema = {'name': {'type': 'string', 'empty': False, 'minlength': 1, 'maxlength': 45},
                  'brand_name': {'type': 'string', 'minlength': 1, 'maxlength': 45},
                  'category': {'type': 'string', 'empty': False, 'minlength': 1, 'maxlength': 45},
                   'price': {'type': 'float', 'empty': False}, 'min': 1}

        v = Validator(schema)
        if v.validate(data, schema):
            return True
        else:
            return v.errors

    def vali_add_bill(self,data):
        schema = {'cus_id': {'type': 'integer', 'empty': False, }}
        v = Validator(schema)
        if v.validate(data,schema):
            return True
        else:
            return v.errors