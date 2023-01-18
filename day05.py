# function
import random


def calc_fee(ages) -> dict:
    """
    놀이공원 요금 계산 프로그램
    어른 몇 명? 아이 몇 명
    :param ages: 나이
    :return: {어른, }
    """
    fee_detail = {'adult': 0,
                  'kids': 0,
                  'total': {
                      'counts': 0,
                      'fee': 0}
                  }
    for age in ages:
        if age > 18:
            fee_detail['adult'] += 1
        else:
            fee_detail['kids'] += 1
    fee_detail['total']['fee'] += 10_000 * fee_detail['adult'] + 3000 * fee_detail['kids']
    fee_detail['total']['counts'] += fee_detail['adult'] + fee_detail['kids']
    return fee_detail


n = int(input('몇 명이서 오셨나요? '))

age_list = [random.randint(1, 50) for i in range(n)]
print(age_list)
receipt = calc_fee(age_list)
print(receipt)
print(f'총 {receipt["total"]["counts"]}분, 성인 : {receipt["adult"]}명'
      f' 아이 : {receipt["kids"]}명\n총 금액 :{receipt["total"]["fee"]}원입니다.')
