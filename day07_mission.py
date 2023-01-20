# Prob 10.10 
class Laser:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class Smartphone:
    def does(self):
        return "ring"


class Laser_robot(Laser):
    def does(self):
        return f'Laser {super().does()}'


class Claw_robot(Claw):
    def does(self):
        return f'Claw {super().does()}'


class Smartphone_robot(Smartphone):
    def does(self):
        return f'Smartphone {super().does()}'

lr = Laser_robot()
print(lr.does())
cr = Claw_robot()
print(cr.does())
sr = Smartphone_robot()
print(sr.does())