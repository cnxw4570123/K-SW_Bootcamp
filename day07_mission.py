# Prob 10.7
class Element:
    def __init__(self, name="", symbol="", number=0):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):  # instance method 이므로 self 필요
        return f'{self.name}, {self.symbol}, {self.number}'


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)
