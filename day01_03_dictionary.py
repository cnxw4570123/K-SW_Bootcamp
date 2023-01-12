# 교재 딕셔너리 예제
subjects = {
    '의사소통영어': 'A+',
    '오래된 미래' : 'B+',
    '양자역학' : ' A',
}
subject = '오래된 미래'
student = '정균민'
print(student, ' 학생의', subject,' 과목성적은 ', subjects[subject],'입니다')
print('%s 학생의 %s 과목성적은 %s입니다.' % (student, subject, subjects[subject])) # old style
print('{0} 학생의 {1} 과목 성적은 {2}입니다'.format(student, subject, subjects[subject])) # modern style 순서 변환 가능
print(f'{student}학생의 {subject} 과목 성적은 {subjects[subject]} 입니다') # modern style f-string
