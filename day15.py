def print_poly(px, tx):
    """
    다항식 출력
    :param px: 계수
    :param tx: 차수
    :return:
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    polyStr = "P(x) = "
    for i in range(len(px)):
        coef = px[i]  # 계수
        term = tx[i]

        if coef > 0:
            polyStr += "+"
        if term > 0:
            polyStr += f"{coef}x^{term} "
        else:
            polyStr += f"{coef}"

    return polyStr


def calc_poly(x_val, px, tx):
    """
    다항식 계산
    :param x_val:
    :param px:
    :return:
    """
    ret_value = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        ret_value += coef * x_val**term
        term -= 1

    return ret_value


# px = [7, -4, 0, 5]
px = [3, -4, 5]
tx = [300, 20, 0]

if __name__ == "__main__":
    pStr = print_poly(px, tx)
    print(pStr)

    x_value = int(input("X 값-->"))

    px_value = calc_poly(x_value, px, tx)
    print(px_value)
