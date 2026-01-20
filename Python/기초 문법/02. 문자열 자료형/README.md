# 2. 문자열 자료형 (String)

### 1. 문자열 만들기 (4가지 방법)
> 문자열은 큰따옴표(`"`)나 작은따옴표(`'`)로 감싸서 만듭니다.

```python
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''
```
---
### 2. 문자열 안에 따옴표 포함하기
#### 작은따옴표 안에 큰따옴표를 넣거나, 그 반대로 사용하면 됩니다.
```Python
#1. 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"

# 2. 큰따옴표(") 포함시키기
say = '"Python is very easy." he says.'

# 3. 백슬래시(\) 이용하기 (이스케이프 코드)
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
```
---
### 3. 여러 줄인 문자열 만들기
#### 이스케이프 코드 \n을 쓰거나, 따옴표 3개를 연속으로 씁니다.
**이스케이프 코드**
> \n : 줄 바꿈  
> \t : 탭  
> \\\ : 문자 \  
> \' : 작은 따옴표  
> \" : 큰 따옴표
```Python
# 방법 1: 이스케이프 코드 사용
multiline = "Life is too short\nYou need python"

# 방법 2: 따옴표 3개 사용 (추천 ⭐)
multiline = """
Life is too short
You need python
"""
```

---
### 4. 문자열 연산
```Python
head = "Python"
tail = " is fun!"

# 더하기 (Concatenation)
head + tail  # 'Python is fun!'

# 곱하기 (반복)
head * 2     # 'PythonPython'

# 길이 구하기 (Length)
a = "Life is too short"
len(a)       # 17
```
---
### 5. 인덱싱과 슬라이싱
#### 리스트와 동일한 방식입니다.
> (0부터 시작, [시작:끝])
#### 불변성
```Python
my_str = hello
my_str[-1] = z # Error
# 정수도 안됨.
```
```Python
a = "Life is too short, You need Python"

a[3]      # 'e'
a[-1]     # 'n' (맨 뒤)
a[0:4]    # 'Life' (0 <= a < 4)
a[19:]    # 'You need Python' (19부터 끝까지)
```
---
### 6. 문자열 포맷팅 (Formatting)
#### 문자열 안에 값을 삽입하는 방법입니다.   
> f-string이 가장 최신 방식입니다.   

#### 6-1. 포맷 코드표 (`%`)  
* **%s**: 문자열 (String)  
* **%c**: 문자 1개 (Character)  
* **%d**: 정수 (Integer)  
* **%f**: 부동소수 (Floating-point)  

```Python
# 1. % 포맷팅
"I eat %d apples." % 3           # 'I eat 3 apples.'
"I eat %s apples." % "five"      # 'I eat five apples.'

# 2. format 함수
"I eat {0} apples".format(3)     # 'I eat 3 apples'
"number: {0}, day: {1}".format(10, 3)

# 3. f-string (파이썬 3.6+ 추천 ⭐)
name = 'Alice'
age = 30
greeting = f'안녕하세요, 제 이름은 {name}이고, 나이는 {age}살입니다.'
print(greeting)  # 안녕하세요, 제 이름은 Alice이고, 나이는 30살입니다.
# 중괄호 {} 안에 표현식도 가능
calculation = f'2 곱하기 3은 {2 * 3}입니다.'
print(calculation)  # 2 곱하기 3은 6입니다.
```

---
### 7. 문자열 관련 함수 (Methods)  
> 문자열 변수 뒤에 `.`을 붙여 사용합니다.  

* **count**: 문자 개수 세기  
    * `a.count('b')`  
* **find**: 위치 찾기 (없으면 -1 반환)  
    * `a.find('b')`  
* **index**: 위치 찾기 (없으면 오류 발생)  
    * `a.index('b')`  
* **join**: 문자열 삽입  
    * `",".join('abcd')`  
* **upper**: 대문자로 변환  
    * `a.upper()`  
* **lower**: 소문자로 변환  
    * `a.lower()`  
* **lstrip / rstrip / strip**: 공백 지우기 (좌 / 우 / 양쪽)  
    * `a.strip()`  
* **replace**: 문자열 바꾸기  
    * `a.replace("Life", "Your leg")`  
* **split**: 문자열 나누기 (리스트로 반환)  
    * `a.split()`  

```Python
a = "hobby"

# 개수 세기
a.count('b')   # 2

# 위치 찾기
a.find('b')    # 2 (인덱스 번호)
a.find('k')    # -1 (없음)

# 문자열 삽입 (join)
",".join('abcd')  # 'a,b,c,d'

# 대소문자 변환
a = "hi"
a.upper()      # 'HI'

# 공백 제거
a = " hi "
a.strip()      # 'hi'

# 문자열 바꾸기 (replace)
a = "Life is too short"
a.replace("Life", "Your leg") # 'Your leg is too short'

# 문자열 나누기 (split) -> 리스트 반환
a = "Life is too short"
a.split()      # ['Life', 'is', 'too', 'short'] (공백 기준)
b = "a:b:c:d"
b.split(':')   # ['a', 'b', 'c', 'd'] (기호 기준)
```
