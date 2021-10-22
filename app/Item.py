from app.validation.validation import validate,ARGS,KWARGS

class Item:
    def __init__(self):
        pass

    @validate(3, ARGS)
    def save(self, name, price, qty):
        print(name, " ", price, " ", qty)