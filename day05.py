# Lambda func
#
# def edit_story(words, f):
#     for word in words:
#         print(f(word))
#
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
#
# edit_story(stairs, lambda word: word.capitalize() + '!')


import random


def process(no_list, f):
    for num in no_list:
        print(f(num))


numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x**2)  # 호출할 일이 많이 없으면 람다함수가 유리하다


# func as a parameter
# import random
#
#
# def process(no_list, f):
#     for num in no_list:
#         print(f(num))
#
#
# def squares(n):
#     """
#     정수를 받아서 제곱해서 반환하는 함수
#     :param n: 정수 값
#     :return:  정수를 제곱하여 반환
#     """
#     return n**2
#
#
# numbers = [random.randint(1, 100) for i in range(5)]
# print(numbers)
# process(numbers, squares)


def a():
    n = 2

    def b():
        return n**2

    return b


c = a()
