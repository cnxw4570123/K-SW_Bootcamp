class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return '말!'


class Donkey(Animal):
    def says(self):
        return '당나귀!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass
    # def says(self):
    #     return 'hinny cries'

m1 = Mule()
h1 = Hinny()

print(m1.says())
print(Mule.mro())
print(h1.says())
