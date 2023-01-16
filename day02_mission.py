import random

small = random.choice([True, False])
green = random.choice([True, False])

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
