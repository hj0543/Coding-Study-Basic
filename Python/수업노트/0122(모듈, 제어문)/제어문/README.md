# 제어문
코드의 실행 흐름을 제어하는 데 사용되는 구문
조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행
#### 조건문 - if, elif, else
```python
if score >= 90:
    message = "축하합니다! 최고입니다!"
elif score >= 70:
    print("멋져요! 잘하셨어요!")
else:
    print("조금 더 노력해보세요!")
```
#### 반복문 - for, while, break, continue
```python
for i in range(N):
    twinkle(message)
```
> **N = 3**이라고 가정 (3번 반복)
> **message**는 앞서 95점을 받아 **"축하합니다! 최고입니다!"**가 저장되었다고 가정
> twinkle() 함수는 메시지 앞뒤에 별(★)을 붙여서 출력하는 기능이라고 가정
> 실행 결과: range(3)이므로 i가 0, 1, 2로 변하면서 총 3번 실행됩니다.
> 
> Plaintext
> 
> ★ 축하합니다! 최고입니다! ★
> ★ 축하합니다! 최고입니다! ★
> ★ 축하합니다! 최고입니다! ★

```python
while True:
    print("계속할까요? (y/n)")
    answer = input()
    if answer == 'y':
        play()
    else:
        print("게임을 종료합니다.")
        break
```
> 계속할까요? (y/n)
> y
> (play() 함수가 실행되어 게임이 진행됨...)
> 
> 계속할까요? (y/n)
> n
> 게임을 종료합니다.

## 조건문
if / elif / else
* if문 : if문에 작성된 코드를 만족할 때 내부 코드 실행
* elif문 : 이전의 조건을 만족하지 못하고 추가로 다른 조건이 필요할 때 사용
* else문 : 모든 조건들을 만족하지 않으면 실행됨
```python
# if문 기본
score = 87
if score > 90:
    print('good')
elif score > 80:
    print('soso')
else:
    print('bad')

# 복수 조건문
## 순서 1. 결과: 매우 나쁨
dust = 155

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


## 순서 2. # 결과: 보통
dust = 155

if dust > 30:
    print('보통')
elif dust > 80:
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')


# 중첩 조건문 동작 예시
# 출력: 매우 나쁨
#      위험해요! 나가지 마세요!
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```
---
## 반복문
주어진 코드 블록을 여러 번 반복해서 실행하는 구문  


### for문
* 반복 가능(literable)한 객체의 요소들을 반복하는데 주로 사용
* 반복 횟수가 정해진 경우 주로 사용
```python
for 변수 in 반복 가능한 객체:
    코드 블록
```
for문 기본
```python
student_list = ['Alice', 'Bob', 'Charlie']

for student in student_list:
    print(f'Hello, {student}') 
# 출력
'''
Hello, Alice
Hello, Bob
Hello, Charlie
'''
```
#### for문 작동 원리
```python
# for문 작동 원리
item_list = ['apple', 'banana', 'coconut']

for item in item_list:  # item: 반복 변수
    print(item)

# 출력
'''
apple
banana
coconut
'''
```
#### 문자열, range, 딕셔너리, 인덱 순회
```python
# 문자열 순회
country = 'Korea'

for char in country:
    print(char)
# 출력
'''
K
o
r
e
a
'''

# range 순회
for i in range(5):
    print(i)
# 출력
'''
1
2
3
4
5
'''
# for문 dictionary 순회
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])
# 출력
'''
x
10
y
20
z
30    
'''
# 인덱스 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)): # 5
    numbers[i] = numbers[i] * 2

print(numbers)
# 출력
'''
[8, 12, 20, -16, 10]
'''
```
#### 중첩된 반복 - 중간에 print 해보는 습관 가지기
```python
# 중첩 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
# 중첩된 반복문은 안쪽부터 돈다.
# 출력
'''
A c
A d
B c
B d
'''

# 중첩 리스트 순회
elements = [['A', 'B'], ['c', 'd']]
'''
elements = [
    ['A', 'B'], 
    ['c', 'd']
]
'''
# 1
for elem in elements:
    print(elem)
# 출력
'''
['A', 'B']
['c', 'd']
'''
# 2
for elem in elements:
    for item in elem:
        print(item)
# 출력
'''
A
B
c
d
'''
```

---
### while문
* 조건이 참인 동안 반복
* 반복 횟수가 정해지지 않은 경우 주로 사용
```python
a = 0
while a < 3
    print(a)
    a += 1

print('끝')

# 출력
'''
0
1
2
'''
```

```python
input_value = ''
while input_value != 'exit':  # exit 를 입력하면 반복 종료
    input_value = input("Enter a value: ")
    print(input_value)
```
```python
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')
```
---
### 반복 제어문
for문과 while문은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음
* 중첩 반복문인 경우 해당 키워드가 작성된 코드 블록의 반복 흐름만 제어한다는 것!!!
#### break
* 해당 키워드를 만나게 되면 남은 코드를 무시하고 반복 즉시 종료
* 반복을 끝내야 할 명확한 조건이 있을 때 사용
```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4
```
```python
# break 키워드 예시 (for문)
# 리스트에서 첫번째 짝수만 찾은 후 반복 종료하기
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다')


# break 키워드 예시 (while문)
# 프로그램 종료 조건 만들기
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
```
#### continue
* 해당 키워드를 만나게 되면 다음 코드는 무시하고 다음 반복을 수행
```python
for i in range(10):
    if i % 2 == 0:
        continue # 짝수 pass
    print(i)  # 1 3 5 7 9
```
```python
# 리스트에서 홀수만 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue # 짝수 pass
    print(num)

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 1:
        print(num)
```

#### pass
* 아무 동작도 하지 않음
* 코드를 비워두면 오류가 발생하기 때문에 pass 키워드를 사용한다.
```python
# pass 키워드 예시 (while 문)
while True:
    if condition1:
        break
    elif condition2:
        pass  # 빈 코드를 의미
    else:
        print('출력')

# pass 키워드 예시 (if 문)
if condition:
    pass  # 아무런 동작도 수행하지 않음
else:
    pass  # 구조를 잡을 뿐


# pass 키워드 예시 (함수 정의)
def my_function():
    pass  # pass 없으면 오류 발생
```