a = []
print(bool(a))
a.append(1)
print(bool(a))
print(bool(set()))
print(bool(dict()))
print(bool("a"))

vowel = 'aeiou'
letter = 'x'

if letter in vowel:
    print(letter, 'is a vowel')
else:
    print(letter, 'is not vowel')

# 문자열 *연산
limit = 20
words = "pass" * 6
diff = limit - len(words)
# if diff := limit - len(words) >= 0:
# 그냥 diff 하면 0이 아니므로 false 출력
if diff >= 0:
    print(words)
else:
    print(f"exceeds limit by {abs(diff)} characters")
