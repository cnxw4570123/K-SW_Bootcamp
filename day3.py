subject = ' $   python, data structure, database   $$$'
print(subject)
print(subject.strip())
print(subject.strip('$'))
print(subject.find('data'), subject.index('data'))
print(subject.find('inha'))
# print(subject.index('inha'))

#역순으로 검색
print(subject.rfind('data'))
print(subject.rindex('data'))

#개수 검색
print(subject.count('data'))

#대소문자 변환
print(subject.title())
