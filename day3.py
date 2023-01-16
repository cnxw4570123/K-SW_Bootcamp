# prime number

number = int(input("input number :"))
counts = 0

# k = 1
# while k < number:
#     if number % k == 0:
#         counts += 1
#     k += 1

for i in range(1, number+1):
    if number % i == 0:
        counts += 1

if counts == 2:
    print(number, 'is a prime number')
else:
    print(number, 'is NOT a prime number')