# class
class Pokemon:
    def __init__(self, owner, skills):  # 객체 생성 시 동작
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성됨 :', end=" ")

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용가능한 스킬")
        for index, skill in enumerate(self.skills):
            print(f'{index+1} : {skill}')
        print()

    def attack(self, idx):
        print(f'{self.skills[idx-1]} 공격을 합니다')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        self.name = '피카츄'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.owner}의 포켓몬 {self.name}가 {self.skills[idx-1]} 공격(전기)을 시전!')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        self.name = '꼬부기'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.owner}의 포켓몬 {self.name}가 {self.skills[idx-1]} 공격(물)을 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다.')


p0 = Pokemon('웅이', '공격1/공격2')
p0.info()
p0.attack(1)
# p0.swim()  # 꼬부기 객체만 사용한 메소드 attributeError
pi1 = Pikachu('한지우', '몸통박치기/백만볼트')
pi1.info()
pi1.attack(2)
ggo1 = Ggoboogi('오바람', '고속 스핀/거품/몸통 박치기')
ggo1.swim()
ggo1.attack(1)
# ggo1.info()

# p1 = Pokemon('한지우', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon('오바람', '고속 스핀/거품/몸통 박치기/하이드로 펌프')
# for i in [p1, p2]:
#     i.info()

