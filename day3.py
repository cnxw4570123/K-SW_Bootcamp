# while
while True:
    dan = int(input('Dan(종료 원하면 \'0\' 입력): '))
    if dan == 0:
        break
    elif 1 < dan < 10:
        i = 1
        while i < 10:
            print('{0} x {1} = {2}'.format(dan, i, dan * i))
            i += 1
    else:
        print('2~9 사이의 값을 입력 하세요.')
print('종료')

