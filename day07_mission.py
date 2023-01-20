# Prob 10.8
class Element:
    def __init__(self, name="", symbol="", number=0):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def get_name(self):
        return self.__name

    @property
    def get_symbol(self):
        return self.__symbol

    @property
    def get_number(self):
        return self.__number

    def __str__(self):  # instance method 이므로 self 필요
        return f'{self.get_name}, {self.get_symbol}, {self.get_number}'


hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen)
hydrogen.__name = 'acid'
# hydrogen._Element__name = 'acid' #이렇게 작성시에는 수정가능
print(hydrogen)
