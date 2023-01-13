import random

secret = random.randint(1, 10)
guess = int(input("1~10 사이의 정수 입력하세요 : "))

if secret > guess :
    print('too low')
elif secret < guess:
    print('too high')
else :
    print('just right')
print(f'secret was {secret} and guess was {guess}')