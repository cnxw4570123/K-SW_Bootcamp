import time

def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer result
    """
    result = 1
    for k in range(1, n+1):
        result *= k
    return result


def factorial_recu(n):
    """
    재귀함수를 사용한 팩토리얼 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    """
    if n == 1:
        return 1
    return n * factorial_recu(n-1)


bef_iter = time.process_time()
print(factorial_iter(999))
aft_iter = time.process_time()
print(factorial_recu(999))
aft_rec = time.process_time()

print(f'반복문 : {aft_iter - bef_iter}, 재귀문 : {aft_rec - aft_iter}')