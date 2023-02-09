# memo = list()  # 전역 변수로 한번 처리한 결과 값을 저장


def fibo_memo(n):
    """
    Memoization(DP)를 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global count_memoization
    count_memoization += 1
    memo = [0, 1]
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]


# def fibo_iter(n):
#
#     r = list()
#     p1, p2 = 1, 1
#     for _ in range(n):
#         r.append(p1)
#         p1, p2 = p2, p1 + p2
#     return r[-1]


def fibo_recu(n):
    global count_recursion
    count_recursion += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


count_recursion = 0
count_memoization = 0
print("피보나치 수 --> 0 1 ")
for i in range(2, 30):
    print(f"{i} : {fibo_memo(i)}")  # memoization
for i in range(2, 30):
    print(f"{i} : {fibo_recu(i)}")  # recursion

print(f"재귀: {count_recursion}, 메모: {count_memoization}")
