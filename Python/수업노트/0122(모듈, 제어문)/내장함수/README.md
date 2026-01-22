# 내장함수
## map 함수
**map(function, iterable)**
반복 가능한 데이토 구조의 모든 요소에 function을 적용하고, 그 결과 값들을 map object로 묶어서 반환
```python
# map 함수 사용 기본
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']


# map 함수 활용 1 - input과 함께 사용
# 터미널 창에서 1 2 3 입력 (공백 주의)
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

# for i numbers 1:
# numbers = int(i)

## 터미널 창에서 1 2 3 입력 (공백 주의)
numbers2 = list(map(int, input().split())) # list 형변환 안하면 덩어리로 나옴
print(numbers2)  # [1, 2, 3]


# map 함수 활용 2 - lambda와 함께 사용
numbers = [1, 2, 3, 4, 5]


def square(x): # 제곱을 하는 함수를 만들고
    return x**2


# lambda 미사용
squared1 = list(map(square, numbers)) # list 형변환 안하면 덩어리로 나옴
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용, 함수 미사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
```

# zip 함수(*iterables)
여러 개의 반복 가능한 데이터 구조를 묶어서, 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 그것들을 모아 zip object로 반환
```python
# zip 함수 사용 기본
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]


# zip 함수 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

# zip 함수 활용 (전치 행렬)
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]
# 출력
'''
(10, 40, 20)
(20, 50, 40)
(30, 39, 50)
'''
for score in zip(*scores):
    print(score)
```
* 반복 가능한 자료형의 길이가 다른 경우 가장 짧은 길이를 기준으로 묶어서 반환
* 