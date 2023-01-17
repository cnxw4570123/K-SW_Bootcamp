# dict
import random
# first = {'a': 'apple', 'b':'bear'}
# second = {'b':'bronze', 'c':'client'}
# print({**first, **second})

students = {'name': 'kim inha', 'age': 23, 'eyes': [1.1, 0.9]}
# for k in students.keys():
# for k in students:
# for k in students.values():
for k, v in students.items():
    # print(k)
    print(f'{k} : {v}')

print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end=' ')
print(f'시력은 좌 : {students["eyes"][0]} 우 : {students["eyes"][1]}')

# 술을 고르면 거기에 매칭되는 안주 추천해주는 프로그램
# q입력할 때까지 계속 loop
# 계산하고 종료

# alcohol_foods = {
#     '맥주': '치킨',
#     '소주': '골뱅이소면',
#     '와인': '치즈',
#     '고량주': '짬뽕'
# }

alcohol_foods = dict([['맥주', '치킨'],['소주','골뱅이소면'],['와인','치즈'],['고량주','짬뽕']])

alcohol_list = list(alcohol_foods)  # extract keys
while True:
    try:
        print()
        alcohol = int(input(f'술을 고르세요 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} '
                            f'5) 아무거나 6) 계산 : '))
        if alcohol == 6:
            print('다음에 또 뵙겠습니다')
            break
        elif 0 < alcohol < 5:
            menu = alcohol_list[alcohol-1]
            print(f'{menu}에 어울리는 안주는 {alcohol_foods[menu]}입니다')
        elif alcohol == 5:
            menu = random.choice(alcohol_list)
            foods = [food for food in alcohol_foods.values()]  #extract values and append list
            food = random.choice(foods)
            print(f'{menu}와 {food}를 드셔보세요')
        else:
            print('메뉴에서 골라주세요.')
    except:
        print('다시 골라주세요')