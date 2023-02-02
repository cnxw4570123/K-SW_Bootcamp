# class
class Pokemon:
    def __init__(self, owner, skills):  # 객체 생성 시 동작
        self.hidden_owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성됨 :', end=" ")

    def get_owner(self):
        return self.hidden_owner

    def set_owner(self, owner):
        self.hidden_owner = owner

    def info(self):
        print(f"{self.hidden_owner}의 포켓몬이 사용가능한 스킬")
        for index, skill in enumerate(self.skills):
            print(f'{index + 1} : {skill}')
        print()

    def attack(self, idx):
        print(f'{self.skills[idx - 1]} 공격을 합니다')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        self.name = '피카츄'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.get_owner()}의 포켓몬 {self.name}가 {self.skills[idx - 1]} 공격(전기)을 시전!')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        self.name = '꼬부기'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.get_owner()}의 포켓몬 {self.name}가 {self.skills[idx - 1]} 공격(물)을 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다.')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        self.name = '꼬부기'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.get_owner()}의 포켓몬 {self.name}가 {self.skills[idx - 1]} 공격(불)을 시전!')


while True:
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    n = input('플레이어 이름: ')
    s = input('사용가능한 기술 입력("/"로 구분): ')
    if menu == '2':
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 :')
        if pokemon == '1':
            p = Pikachu(n, s)
            pass
        elif pokemon == '2':
            p = Ggoboogi(n, s)
        elif pokemon == '3':
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라주세요.')
    info_atk = input('1) 공격: ')
    if info_atk == '1':
        p.info()
        atk_menu = input('스킬 번호 선택: ')
        p.attack(int(atk_menu) - 1)
    else:
        print('메뉴에서 골라 주세요')

# p0 = Pokemon('웅이', '공격1/공격2')
# p0.info()
# p0.attack(1)
# pi1 = Pikachu('한지우', '몸통박치기/백만볼트')
# pi1.info()
# pi1.attack(2)
# ggo1 = Ggoboogi('오바람', '고속 스핀/거품/몸통 박치기')
# ggo1.swim()
# ggo1.attack(1)