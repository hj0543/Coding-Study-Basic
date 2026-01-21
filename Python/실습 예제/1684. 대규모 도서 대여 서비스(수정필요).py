number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1
    pass

####################################################

def decrease_book(number):
    global number_of_book

    # 대여 권 수 만큼 차감
    number_of_book -= number
    
    # 남은 책 수 출력
    print(f'남은 책의 수 : {number_of_book}')

    pass

#################################################

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

#####################################################

def create_user(name, age):

    # 유저 수 증가 함수 호출
    increase_user()

    # 환영 메세지 출력
    print(f'{name}님 환영합니다!')

    return{'name':name, 'age':age}

many_user = list(map(create_user, name, age))

# user_info 리스트 생성
user_info = []
for user in many_user:
    new_dict = {}
    new_dict[user['name']] = user['age']

    user_info.append(new_dict)


###########################################################
# items로 풀어보기


def rental_book(info):

    name = info['name']
    age = info['age']
    
    rented = age // 10
    decrease_book(rented)

    print(f'{name}님이 {rented}권의 책을 대여하였습니다.')

    pass

for user in user_info.items():
    rental_book(user)

