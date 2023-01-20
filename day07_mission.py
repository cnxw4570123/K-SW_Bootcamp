# Prob 10.6 
class Element:
    def __init__(self, name="", symbol="", number=0):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):  # instance method 이므로 self 필요
        print(self.name , self.symbol, self.number)


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()
print(hydrogen)
