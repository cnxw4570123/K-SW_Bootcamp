univ = 'Inha University'

print(univ[5:])
print(univ[5:14]) # 14 - 1 까지 출력 1글자 잘림
print(univ[5:15])
print(univ[-10:]) # -1로 항상 끝을 가르킬 수 있다.
print(univ[::2])
print(univ[5:-6])
print(univ[-10:-6])

print(len(univ))
print(univ.split('i'))

pokemons_list = ['피카츄', '라이츄', '꼬부기', '이상해씨', '파이리']
pokemon_string = ", ".join(pokemons_list)
print(pokemon_string)

sentence = 'a duck goes into a bar'
print(sentence.replace('a ', 'a famous ', 100))
