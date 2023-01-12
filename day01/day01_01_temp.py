#(°C × 9/5) + 32 = °F

fahrenheit = float(input('화씨 온도 : '))


def temperature(fah):
    celsius = (fah - 32.0) * (5.0/9.0)
    return celsius


print(f'화씨 온도 {fahrenheit}도는 섭씨 온도 {temperature(fahrenheit):.1f}도 입니다')
