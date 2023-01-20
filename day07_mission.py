# 10.9

class Bear:
    def eat(self):
        return 'Berries'


class Rabbit:
    def eat(self):
        return 'Clover'


class Octothorpe:
    def eat(self):
        return 'Campers'


b1 = Bear()
r1 = Rabbit()
o1 = Octothorpe()

print(b1.eat())
print(r1.eat())
print(o1.eat())