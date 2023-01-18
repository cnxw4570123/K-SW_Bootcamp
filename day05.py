# function
def inha():
    """
    단순 숫자 출력 함수
    """
    print(60)


def call_func(f):
    """
    매개변수로 함수를 받아 실행
    :param f: 함수명
    """
    f()  # 함수 실행


def subtract(num1, num2):
    print(num1 - num2)


def run_func(f, arg1, arg2):
    """
    함수를 매개 변수로 받아 arg1, arg2를 매개변수로 하는 함수 실행
    :param f: 함수명
    :param arg1: 정수 값
    :param arg2: 정수 값
    :return:
    """
    f(arg1, arg2)


call_func(inha)
print(type(call_func))

run_func(subtract, 99, 88)


def knights2(saying):  # 클로저
    def inner2():
        return f"We are the knights who say : {saying}"

    return inner2


a = knights2('duck')
print(a())


def outer(n2):
    """
    인수를 받아서 클로저에 인수를 매개변수로 할당한다
    :param n2: 정수 값
    :return:
    """
    n3 = 3
    print(f'외부함수 실행, n2=>{n2}, n3=>{n3}')

    def arg_changer():
        n3 = n2 ** 2
        print(f'클로저 실행, n2=>{n2}, n3=>{n3}')
        return n3

    return arg_changer


a = outer(10)
print(a())
