import os
import json
from app.validation.validation import validate, KWARGS, ARGS


__uid_file__ = "db/uid.json"
__db_user__ = "db/users"
__db_user_session__ = "db/session.json"


class User:

    def __init__(self):
        if os.path.isfile(__uid_file__):
            with open(__uid_file__, 'r') as f:
                self.uid = json.load(f)
        else:
            self.uid = 0

    @validate(2, ARGS)
    def registration(self, email, password):
        self.uid += 1
        user_list = os.listdir(__db_user__)
        if not user_list.__contains__(f"{email}.json"):
            with open(f"{__db_user__}/{email}.json", 'w') as f:
                data = {
                    'uid': self.uid,
                    'email': email,
                    'password': password
                }
                json.dump(data, f)
            with open(__uid_file__, 'w') as f:
                self.uid += 1
                json.dump(self.uid, f)
            print("User successfully registered!")
        else:
            print('User alredy exist.!')

    def __get_user(self, email):
        try:
            user_list = os.listdir(__db_user__)
            user = [x for x in user_list if x == f"{email}.json"][0]
            return user
        except Exception as e:
            print(e)

    @validate(2, ARGS)
    def login(self, email, password):
        if email != "":
            user_file = self.__get_user(email)
            if user_file != None:
                with open(f"{__db_user__}/{user_file}", 'r') as f:
                    data = json.load(f)
                    if data['password'] == password:
                        self.__write_current_session(
                            data['uid'], data['email'])
                        print("User successfully login.!")
                    else:
                        print("Error: password not matched")
            else:
                print("Error: email not found.!")
        else:
            print("Error: email can not be null")

    def __write_current_session(self, id, email):
        with open(__db_user_session__, 'w') as f:
            json.dump({
                'id': id,
                'email': email
            }, f)

    def view_session(self):
        with open(__db_user_session__,'r') as f:
            sess =  json.load(f)
            print(f"Current User ID: {sess['id']}\nCurrent User Email: {sess['email']}")
