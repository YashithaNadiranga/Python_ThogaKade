from app.Order import Order
import sys
import os
from app.Item import Item
from app.User import User
from app.Order import Order
from app.validation.validation import get_inputs

user = User()
item = Item()
order = Order()


def init():
    if not os.path.exists('db/'):
        os.makedirs('db/items')
        os.makedirs('db/users')
        os.makedirs('db/orders')
    else:
        print('Already initialized the System')


@get_inputs(params=['email', 'password'])
def user_reg_inputs(email, password):
    user.registration(email, password)


@get_inputs(params=['email', 'password'])
def user_login_inputs(email, password):
    user.login(email, password)


def user_view_session():
    user.view_session()


def item_get_all():
    item.getAll()


@get_inputs(params=['id', 'name', 'price', 'qty'])
def item_add(id, name, price, qty):
    item.save(id, name, price, qty)


@get_inputs(params=['name'])
def item_find(name):
    item.find(name)


if __name__ == "__main__":
    print(banner)
    args = sys.argv[1:]

    if len(args) <= 0:
        print(
            user_help, "\nArguments Not Found! Please Provide arguments <section> <commend>")
    elif args[0] == "system" and args[1] == "init":
        init()
    elif not os.path.exists('db'):
        print('Please initialize the system before use.!\nuse main.py system init')
    elif args[0] == "help":
        print(user_help)
    else:
        section = args[0]
        commend = args[1]

        if section == "item":
            if commend == "add":
                item_add()
            elif commend == "all":
                item_get_all()
            elif commend == "find":
                item_find()
        if section == "user":
            if commend == "reg":
                user_reg_inputs()
            elif commend == "login":
                user_login_inputs()
            elif commend == "session":
                user_view_session()
