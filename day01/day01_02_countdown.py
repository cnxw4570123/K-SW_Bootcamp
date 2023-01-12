# for countdown in 5, 4, 3, 2, 1, 'count!':
#     print(countdown)

# 파이썬은 스네이크 표기법 사용 -> countdown_list
countdown_list = [5, 4, 3, 2, 1, 'hey']
for countdown in countdown_list:
    print(countdown)

print(countdown_list[3])
print('프로그램 종료')

# [] -> 인덱싱을 한다

quotes = {
    "Moe": "A wise guy, huh?", # key와 value로 나뉨
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!"
}
stooge = "Curly"
print(stooge, "says:", quotes[stooge])
