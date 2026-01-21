title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.
# 딕셔너리 생성
data = {
    '과목': 'Python',
    '구분': '실습',
    '단계': 2,
    '문제번호': 3251,
    '이름': None,
    '일차': 22
}

# data 출력
print(data)

# 단계값을 2단계로 수정
data['단계'] = str(data['단계']) + '단계'

# 이름에 title 변수 할당
data['이름'] = title

# 일차 값을 원본에서 20을 뺀 값으로 할당
data['일차'] -= 20

# data 출력
print(data)
