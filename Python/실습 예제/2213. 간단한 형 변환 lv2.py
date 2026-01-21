book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
book = int(book) # book값 정수형으로 형 변환
print(guide)
print(book * total)

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
rental = int(rental) # rental값 정수형으로 형 변환
print(changes)
print(total - rental)
