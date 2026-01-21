number_of_book = 100

def decrease_book(number):
    global number_of_book

    # 대여 권 수 만큼 차감
    number_of_book -= number

# 남은 책 수 출력
print(f'남은 책의 수 : {number_of_book}')

def rental_book(name, number):

    decrease_book(number)

    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)


