# list

scores = ('B+', 'A+', 'C+')
print(scores[1])
# scores[1] = 'C+'  # immutable
# scores[2] = 'A+'  # immutable
temp = list(scores)  # convert to list
temp[1], temp[2] = temp[2], temp[1]
print(temp)
scores = tuple(temp)  # overwrite
print(scores[1])
print(scores[2])

big_bang = ['GD', 'TOP', '대성', '태양', '승리']
# big_bang.append('인하') 가장 마지막에 삽입
big_bang.insert(1, '인하')  # 특정 위치에 삽입
print(big_bang)
print(big_bang * 2)
exo = ['백현', '첸']
# exo.extend(big_bang)
# exo = exo + big_bang
exo.append(big_bang)
print(exo)
print(exo[2][4])  # 태양 출력
print(exo[-1][-2])

exo[1] = '시우민'
print(exo)
# print(exo.pop())  # 빅뱅 전체 삭제
print(exo[2].pop())  # 승리 삭제
print(exo[2].pop(-3))  # top 삭제
print(exo)

del exo[2][-2]  # 대성 삭제
print(exo)
exo[-1].remove('인하')
print(exo)
exo.clear()
print(exo)