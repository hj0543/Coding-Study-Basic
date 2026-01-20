# 03 for문 (For Loop)

### 1. for문의 기본 구조
> 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례대로 변수에 대입되어 문장들을 수행합니다.

**기본 생김새:**
```python
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
    ...
```
#### 기본 예제 1 (리스트):
```Python

test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)
````
* 결과: one, two, three가 순서대로 출력됩니다.

#### 기본 예제 2 (튜플 리스트):

````Python

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
````
* 해석: 튜플 (1, 2)가 (first, last)에 대입되어 first=1, last=2가 됩니다.

* 결과: 3, 7, 11이 차례대로 출력됩니다.
---
### 2. for문 응용하기 (총점 검사)
> "5명의 학생 시험 점수가 60점이 넘으면 합격, 아니면 불합격"을 판별하는 예제입니다.

```Python

marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number + 1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
```
---
### 3. for문과 continue
> while문과 마찬가지로 continue를 만나면 아래 문장들을 수행하지 않고 다음 반복으로 넘어갑니다.  
> (60점 이상인 사람에게만 축하 메시지를 보내고, 나머지는 건너뛰는 예제)

```Python

marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number + 1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다." % number)
```
---
### 4. range 함수 사용하기 (중요 ⭐)
> for문은 숫자 리스트를 자동으로 만들어주는 range 함수와 자주 함께 사용됩니다.  
> range(시작_숫자, 끝_숫자) 형태이며, 끝 숫자는 포함되지 않습니다.

* range(10): 0부터 9까지 (10 미만)

* range(1, 11): 1부터 10까지 (11 미만)

#### 1부터 10까지 더하기:

```Python

add = 0 
for i in range(1, 11): 
    add = add + i 

print(add)  # 55
```
#### 구구단 출력하기 (이중 for문):

```Python

for i in range(2, 10):        # 2단 ~ 9단
    for j in range(1, 10):    # 1 ~ 9 곱하기
        print(i*j, end=" ") 
    print('')
```
* end=" " : 다음 줄로 넘어가지 않고 한 줄에 계속 출력하기 위해 사용

* print('') : 단이 끝날 때마다 줄 바꿈을 하기 위해 사용

---
### 5. 리스트 내포 (List comprehension)
> 리스트 안에 for문을 포함하여 코드를 매우 직관적이고 짧게 만드는 파이썬만의 강력한 기능입니다.

#### 기본 문법: [표현식 for 항목 in 반복가능객체 if 조건문]

#### 사용 전 (일반적인 코드):

```Python

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

# result -> [3, 6, 9, 12]
```
#### 사용 후 (리스트 내포 사용):

```Python

a = [1, 2, 3, 4]
result = [num * 3 for num in a]

# result -> [3, 6, 9, 12]
```

#### 조건문 추가 (짝수에만 3을 곱하고 싶다면):

```Python

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]

# result -> [6, 12]
```
