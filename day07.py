class Duck:
    def __init__(self, input_name):
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


don = Duck('Donald')
print(don.name)

don.name = 'Donna'
print(don.name)

don._Duck_hidden_name = 'ww'
don.name = 'Kim inha'
print(don.name)
