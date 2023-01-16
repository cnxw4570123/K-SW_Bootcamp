# prime number

number = int(input("input number :"))
is_prime = True
# k = 1
# while k < number:
#     if number % k == 0:
#         counts += 1
#     k += 1

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime: # 비어있으면 False 따라서 0이 아니면 prime number 아님
    print(number, 'is a prime number')
else:
    print(number, 'is NOT a prime number')
