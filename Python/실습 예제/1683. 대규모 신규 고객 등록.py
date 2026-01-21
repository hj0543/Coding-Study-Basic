number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    pass

def create_user(name, age, address):

    # 유저 수 증가 함수 호출
    increase_user()

    # user-info dic 생성
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    pass

    # 환영 메세지 출력
    print(f'{name}님 환영합니다!')

    # dic 반환
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


array = list(map(create_user, name, age, address))

print(array)