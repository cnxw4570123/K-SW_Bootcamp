import random

value = [True, False]
small = value[random.randint(0, 1)]
green = value[random.randint(0, 1)]

print(f"small = {small} and green = {green}")
if small:
    if green:
        print('It is pea')
    else:
        print('It is cherry')
else:
    if green:
        print("It is watermelon")
    else:
        print("It is pumpkin")
