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
        print('System initialized Successfully')
    else:
        print('Already initialized')


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

def order_all():
    order.all()

def order_place():
    item_list = []
    item_get_all()
    while True:
        item_name = input('\nPlease Enter Your Item Name: ')
        qty = input('\nPlace Enter Qty: ')
        if item.is_item_exist(item_name):
            item_list.append([item_name, qty])
        else:
            print("Sorry Item can not found. please check again.", end="\n")
        is_continue = input("Do you want to add more items (Yes/No): ")
        if is_continue.lower() == "no":
            break
        else:
            continue
    result = order.place(item_list)
    if result == True:
        print("\nYour order has been placed.")
    else:
        print("\nPlease Try again.!")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) <= 0:
        print(
            user_help, "\nArguments Not Found! Please Provide arguments <section> <commend>")
    elif args[0] == "system" and args[1] == "init":
        init()
    elif not os.path.exists('db'):
        print('Please initialize the system before use.!\nuse python main.py system init')
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
        if section == "order":
            if commend == "place":
                order_place()
            if commend == "all":
                order_all()
