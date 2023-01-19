# def div_calc(n1, n2):
#     """
#     나누기 함수
#     :param n1: 분자
#     :param n2: 분모
#     :return: 계산결과
#     """
#     return n1 / n2

try:
    raise Exception("쉬는 시간!")
    expr = input('분자와 분모 입력 : ').split()
    # print(div_calc(1, 0))
    print(int(expr[0]) / int(expr[1]))
    # print(expr[2])
except ZeroDivisionError as err1:
    print(err1)
    print("분모에 0이 올 수 없습니다.")
except ValueError as err2:
    print("숫자를 입력해 주세요")
except IndexError as err3:
    print(err3)
    print("2개의 숫자를 띄어쓰기로 구분해 입력해 주세요")
except Exception as other:
    print(other)
    print("예외 발생!")
else:  # 예외가 발생하지 않았을 때
    print('프로그램 정상', end=' ')
finally:  # 예외 발생 여부에 관계 없이 무조건 실행
    print('종료')