# function
# input 2 numbers
def is_prime(n):
    """
    매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param n: integer number
    :return: bool value
    """
    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True


print(is_prime(19))
# print prime number between start and end
start, end = input('give 2 numbers : ').split()
if end < start:
    start, end = end, start

for divide in range(int(start), int(end)+1):
    if is_prime(divide):
        print(divide, end=" ")
