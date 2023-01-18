# 9.2
def get_odds(first=0, end=10, step=0):
    number = first
    while number < end:
        if number % 2 == 1:
            yield number
        number += 1


count = 0
for i in get_odds():
    count += 1
    if count == 3:
        print(i)
        break
    

    