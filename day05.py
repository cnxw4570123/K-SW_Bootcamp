# function
def calc_fee(*args):
    """
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: total entrance fee
    """
    total = 0
    for age in args:
        if age > 18:
            total += 10_000
        else:
            total += 3000
    return total


print(calc_fee(20, 20, 25))
print(calc_fee(45, 43, 10, 7))


# def do_nothing():
#     pass
#
#
# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)
#
#
# do_nothing()
# print(do_nothing())
#
# mamamoo = ['화사', '솔라', '휘인', '문별']
# print(mamamoo.pop())  # 리턴 후 삭제
# print(mamamoo.remove('휘인'))  # 삭제만 -> 리턴 값 없으므로 None 출력
#
# buggy('a')
# buggy('b')



