class Duck:
    color = 'red'
    count = 0

    def __init__(self, input_name):
        Duck.count += 1
        self.__hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__hidden_name = input_name
    # name = property(get_name, set_name)

    @classmethod
    def kids(cls):
        print('class method')
        print(f"Duck has {cls.count} little kids")

    @staticmethod
    def test():
        print('static method')


don = Duck('Donald')
print(don.color, Duck.color)
don.color = 'blue'
print(don.color, Duck.color)
Duck.color = 'green'
print(don.color, Duck.color)
d2 = Duck('Induck')
print(d2.color, don.color, Duck.color)
Duck.kids()
Duck.test()
don.kids()
don.test()

# print(Duck.name)  # instance property이므로 class가 사용할 수 없다
print(don.name)


# don.name = 'Donna'
# print(don.name)
#
# don._Duck_hidden_name = 'ww'
# don.name = 'Kim inha'
# print(don.name)
