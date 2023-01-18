# closures

def calculate():
    x = 1
    y = 2
    temp = 0

    def add_sub(n):  # temp가 계속해서 변경됨
        nonlocal temp
        # x = 11  # local variable
        temp = temp + x + n - y
        return temp

    print('once')
    return add_sub


c1 = calculate()  # calculate 함수는 한 번만 실행한다
print(type(c1))
print(c1)
for i in range(5):
    print(c1(i))  # add_sub만 5번 실행
