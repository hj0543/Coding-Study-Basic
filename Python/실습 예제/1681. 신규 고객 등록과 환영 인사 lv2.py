number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    # 유저 수 증가 함수 호출
    increase_user()

    # user-info dic 생성
    user_info = {
        'name': '홍길동',
        'age': 30,
        'address': '서울'
    }

    # 환영 메세지 출력
    print(f'{name}님 환영합니다!')

    # dic 반환
    return user_info

print(f'현재 가입 된 유저 수 : {number_of_people}')

result = create_user('홍길동', 30, '서울')
print(result)

print(f'현재 가입 된 유저 수 : {number_of_people}')