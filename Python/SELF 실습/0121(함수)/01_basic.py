# 함수 정의
def make_sum(x, y):
    """
    이것은 두 수를 파라미터로 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3

    :param x: Description 
    :param y: Description
    """
    result = x + y
    return result

# 함수 호출 및 반환 값 할당
result = make_sum(100, 200) # print(make_sum(100, 200)) 으로도 가능
print(result)   # 300

# [번외] print() 함수는 반환값이 없다.
result2 = print(100) # 100은 출력되지만, 반환값은 None
print(result2)  # None

def my_func():
    """
    Docstring for my_func
    이 함수는 호출되면 터미널에 hello를 출력하는 함수입니다.
    """
    print("hello")

result3 = my_func()  # hello 출력
print(result3)  # None 출력