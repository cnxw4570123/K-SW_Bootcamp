# class
class Pokemon:
    def __init__(self, name, owner, skills):  # 객체 생성 시 동작
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 객체 {name} 생성됨')

    def info(self):
        print(f"{self.owner}의 포켓몬은 {self.name}입니다.")
        for index, skill in enumerate(self.skills):
            print(f'{index+1} : {skill}')
        print()


class Pikachu(Pokemon):  # inheritance
    pass


pi1 = Pikachu('피카츄', '덴트', '몸통박치기')
pi1.info()
p1 = Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기', '오바람', '고속 스핀/거품/몸통 박치기/하이드로 펌프')
for i in [p1, p2]:
    i.info()

