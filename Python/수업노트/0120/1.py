# 1. 함수 정의
def get_sum(num1, num2):
    return num1 + num2

# 2. 서로 다른 입력값으로 함수 사용하기
result_1 = get_sum(5, 3)
result_2 = get_sum(10, 20)

# 3. 함수 호출
print(result_1) # 8
print(result_2) # 30

# def 함수 정의 -> result 함수 사용 -> print 함수 호출

def make_sum(pram1, pram2): # 1-parameter - 함수 입력값
    """ # 2-함수의 body 시작 - Docstring
    이것은 두 수를 받아 두 수의 합을 반환하는 함수입니다. # 3-Docstring
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2 # 4-함수 반환(핵심 로직)
result = make_sum(100, 30) # 5-함수 호출
print(result) # 130