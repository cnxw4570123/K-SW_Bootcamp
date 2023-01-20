# Prob 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def get_item(self):
        return [self.name , self.symbol, self.number]


e1 = Element('Hydrogen', 'H', 1)
print(e1.get_item())

