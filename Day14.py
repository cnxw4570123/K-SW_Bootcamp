# Pokemon v0.5
# getter setter -> property -> decorator
# classfield

class Pokemon:
    count = 0

    def __init__(self, owner, skills):  # 객체 생성 시 동작
        self.__hidden_owner = owner  # like private
        self.skills = skills.split('/')
        Pokemon.count += 1
        print(f'포켓몬 생성됨 :', end=" ")

    @property
    def owner(self):
        return self.__hidden_owner

    @owner.setter
    def owner(self, owner):
        self.__hidden_owner = owner

    def info(self):
        print(f"{self.hidden_owner}의 포켓몬이 사용가능한 스킬")
        for index, skill in enumerate(self.skills):
            print(f'{index + 1} : {skill}')
        print()

    def attack(self, idx):
        print(f'{self.skills[idx - 1]} 공격을 합니다')
    # owner = property(get_owner, set_owner)


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        self.name = '피카츄'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[피카~!]{self.owner}의 포켓몬 {self.name}가 {self.skills[idx - 1]} 공격(전기)을 시전!')

class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        self.name = '꼬부기'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[꼬북!]{self.owner}의 포켓몬 {self.name}가 {self.skills[idx - 1]} 공격(물)을 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다.')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        self.name = '꼬부기'
        super().__init__(owner, skills)
        print(f'{self.name}')

    def attack(self, idx):
        print(f'[파이]{self.owner}의 포켓몬 {self.name}가 {self.skills[idx - 1]} 공격(불)을 시전!')


while True:
    print(f'포켓몬 객체수 : {Pokemon.count}')
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    if menu == '2':
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 :')
        n = input('플레이어 이름: ')
        s = input('사용가능한 기술 입력("/"로 구분): ')
        if pokemon == '1':
            p = Pikachu(n, s)
            # p.owner = "한지우"  # setter 동작
            p.hidden_owner = '한지우'  # 허용되지 않는 접근
            pass
        elif pokemon == '2':
            p = Ggoboogi(n, s)
        elif pokemon == '3':
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라주세요.')
    info_atk = input('1) 공격: ')
    p.info()
    if info_atk == '1':
        atk_menu = input('스킬 번호 선택: ')
        p.attack(int(atk_menu) - 1)
    else:
        print('메뉴에서 골라 주세요')
