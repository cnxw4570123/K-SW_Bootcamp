def print_poly(px):
    """
    다항식 출력
    :param px:
    :return:
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수
        if i > 0 and coef > 0:
            polyStr += "+"
        elif coef == 0:
            term -= 1
            continue

        if term > 0:
            polyStr += f"{coef}x^{term} "
        else:
            polyStr += f"{coef}"
        term -= 1

    return polyStr


def calc_poly(x_val, p_x):
    """
    다항식 계산
    :param x_val:
    :param p_x:
    :return:
    """
    ret_value = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = p_x[i]  # 계수
        ret_value += coef * x_val**term
        term -= 1

    return ret_value


# px = [7, -4, 0, 5]
px = [-10, -2, 0, -1]

if __name__ == "__main__":
    pStr = print_poly(px)
    print(pStr)

    x_value = int(input("X 값-->"))

    px_value = calc_poly(x_value, px)
    print(px_value)
