from app.validation.validation import validate, ARGS, KWARGS
import json
import os
import datetime

__db_user_session__ = "db/session.json"
__db_orders__ = "db/orders"
__db_oid__ = "db/oid.json"


class Order:
    oid = 1

    def __init__(self):
        with open(__db_user_session__, 'r') as f:
            data = json.load(f)
            self.email = data['email']
            self.id = data['id']
        self.__get_oid()

    def __get_oid(self):
        if os.path.exists(__db_oid__):
            with open(__db_oid__, 'r') as f:
                self.oid = json.load(f)
        else:
            self.oid = 1

    def __write_oid(self):
        with open(__db_oid__, 'w') as f:
            self.oid += 1
            json.dump(self.oid, f)

    def place(self, ):
        with open(f"{__db_orders__}/{self.email}.json", 'a') as f:
            json.dump({
                'id': self.oid,
                'user': self.id,
                'date': datetime.datetime.now(),
                'items': [

                ]
            }, f)

    def all(self):
        pass
