from app.validation.validation import validate, ARGS, KWARGS
import json
import os
import datetime
from app.Item import Item
from beautifultable import BeautifulTable

__db_user_session__ = "db/session.json"
__db_orders__ = "db/orders"
__db_oid__ = "db/oid.json"


class Order:
    oid = 1
    item = None

    def __init__(self):
        if os.path.isfile(__db_user_session__):
            with open(__db_user_session__, 'r') as f:
                data = json.load(f)
                self.email = data['email']
                self.id = data['id']
            self.__get_oid()
            self.item = Item()

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

    def place(self, item_list):
        try:
            items = []
            for item_name, qty in item_list:
                item_data = self.item.find(item_name)
                item_data['qty'] = qty
                items.append(item_data)
            with open(f"{__db_orders__}/{self.email}.json", "a") as f:
                j = {
                    'id': self.oid,
                    'user': self.id,
                    'date': str(datetime.datetime.now()),
                    'items': items,
                }
                json.dump(j, f)
                f.write("\n")
                self.__write_oid()
                return True
        except Exception as e:
            print("Error: Can't place order")
            return False

    def all(self):
        try:

            with open(f"{__db_orders__}/{self.email}.json", "r") as f:
                for i in f:
                    table = BeautifulTable()
                    table.columns.header = ["ID", "Name", "Price", "QTY"]
                    data = json.loads(str(i))
                    print(
                        f"Oid: {data['id']} User: {data['user']} Date: {data['date']}")
                    for x in data['items']:
                        table.rows.append(
                            [x['id'], x['name'], x['price'], x['qty']])
                    print(table, end="\n\n")

        except Exception as e:
            print("No Orders found", e)

