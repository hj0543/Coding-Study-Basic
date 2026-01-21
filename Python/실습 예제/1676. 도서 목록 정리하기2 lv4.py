information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],            
    ['홍길동전', '장생전', '도문대작'],     
    ['옥루몽', '옥련몽'],
]

# 인덱스를 사용하여 information 딕셔너리에 할당
information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

# 출력
print(authors[0], ':', information[authors[0]])
print(authors[1], ':', information[authors[1]])
print(authors[2], ':', information[authors[2]])
print(authors[3], ':', information[authors[3]])
print(authors[4], ':', information[authors[4]])
