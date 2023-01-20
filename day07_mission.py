# Prob 10.4
class Element:
    def __init__(self, name="", symbol="", number=""):
        self.name = name
        self.symbol = symbol
        self.number = number

    def get_item(self):  # instance method 이므로 self 필요
        return [self.name , self.symbol, self.number]

el_dict = {
    'name' : 'Hydrogen',
    'symbol' : 'H',
    'number' : 1
}

e2 = Element(**el_dict)
print(e2.get_item())