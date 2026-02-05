# 04-1 함수 (Function)

### 1. 함수란?
> 입력값을 가지고 어떤 일을 수행한 다음에 결과값을 내놓는 "박스"와 같습니다.
> 반복되는 코드를 줄이고, 프로그램의 흐름을 한눈에 알아보기 쉽게 만들어줍니다.

**기본 구조 (`def`):**
```python
def 함수이름(매개변수):
    수행할_문장1
    수행할_문장2
    ...
    return 결과값
```
#### 함수를 사용하는 이유
* 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
* 재사용성이 높아지고, 코드의 가독성과 유지보수성 향상

**함수 사용 전**
```python
# 5와 3을 더하기
num1 = 5
num2 = 3
result1 = num1 + num2
print(result1)

# 10과 20을 더하기 (코드 중복 발생!)
num3 = 10
num4 = 20
result2 = num3 + num4
print(result2)
```
**함수 사용 후**
```python
# 1. 덧셈 기능을 가진 함수 정의
def get_sum(num1, num2):
    return num1 + num2

# 2. 서로 다른 입력값으로 함수 사용하기 -> 함수 호출
result_1 = get_sum(5, 3)
result_2 = get_sum(10, 20)

# 3. 결과 확인
print(result_1) # 8
print(result_2) # 30
```
```python
def make_sum(pram1, pram2) # 함수 정
    """이것은 두 수를 받아 두 수의 합을 반환하는 함수입니다. # 2-함수body  # 3-Docstring
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2 # 4-함수 반환 
result = make_sum(100, 30) # 5-함수 호출
print(result) # 130
```
#### 1-함수 정의
* 함수 정의는 def 키워드로 시작
* def 키워드 이후 함수 이름 작성  

#### 2-함수 body
* 콜론(:) 다음에 들여쓰기 된 코드 블록
* 함수가 실행 될 때 수행되는 코드를 정의  

#### 3-Docstring
* 함수 body 앞에 선택적으로 작성 가능한 함수 설명서  

#### 4-함수 반환 값
* 함수는 필요한 경우 결과를 반환할 수 있음
* return 키워드 이후에 반환할 값을 명시
* return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환  
* 함수 내에서 return 문이 없다면 None이 반환  

#### 5-함수 호출
* 함수를 사용하기 위해서는 호출이 필요
* 함수의 이름과 소괄호를 활용해 호출
* 필요한 경우 인자(argument)를 전달해야 함
* 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨
---
### 2. 매개변수와 인수
> 매개변수(Parameter): 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
> 인수(Arguments): 함수를 호출할 때 전달하는 실제되는 값
```Python
def add_numbers(x, y):  # x와 y는 매개변수(parameter)
    result = x + y
    return result

a = 2
b = 3

sum_result = add_numbers(a, b)  # a와 b는 인자(argument)
print(sum_result)
```
---
### 3. 함수의 인자(Arguments) 정리

#### 1) 매개변수(Parameter) vs 인자(Argument)
* 매개변수: 함수를 정의할 때 전달받은 값을 저장하는 변수
* 인자: 함수를 호출할 때 실제로 전달하는 값

```Python

def add_numbers(x, y):  # x, y는 매개변수
    result = x + y
    return result

a, b = 2, 3
sum_result = add_numbers(a, b)  # a, b는 인자
```
#### 2) 인자의 종류
* 위치 인자 (Positional Arguments)
> 함수 호출 시 인자의 위치에 따라 매개변수에 값이 전달됩니다.
> 
> 호출 시 반드시 값을 전달해야 합니다.
> 
> 순서가 바뀌면 의도치 않은 결과가 나올 수 있습니다.

* 기본 인자 값 (Default Argument Values)
> 함수 정의 시 매개변수에 미리 기본값을 할당하는 방식입니다.
> 
> 인자를 전달하지 않으면 설정된 기본값이 사용됩니다.

```Python

def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')  # age에 기본값 30 할당
```
* 키워드 인자 (Keyword Arguments)
> 인자의 이름을 명시하여 값을 전달합니다.
> 
> 인자의 순서는 중요하지 않으며, 특정 매개변수에 값을 직접 할당할 수 있습니다.
> 
> 주의: 호출 시 키워드 인자는 반드시 위치 인자 뒤에 위치해야 합니다.

* 임의의 인자 목록 (Arbitrary Argument Lists / *args)
> 정해지지 않은 개수의 인자를 처리할 때 사용합니다.
> 
> 매개변수 앞에 *를 붙이며, 전달된 인자들은 tuple로 묶여 처리됩니다.

* 임의의 키워드 인자 목록 (Arbitrary Keyword Argument Lists / **kwargs)
> 정해지지 않은 개수의 키워드 인자를 처리합니다.
> 
> 매개변수 앞에 **를 붙이며, 전달된 인자들은 dictionary로 묶여 처리됩니다.

#### 3) 왜 위치 인자가 키워드 인자보다 앞에 와야 할까?
> 순서의 모호성 때문입니다.
> 
> 위치 인자는 순서에 의존하여 값이 전달되는데, 이미 키워드 인자로 순서가 깨진 상태에서 이름 없는 값(위치 인자)을 던지면 컴퓨터가 해당 값이 몇 번째 자리에 들어가야 하는지 판단할 수 없게 됩니다.

#### 4) 함수 인자 권장 작성 순서
> 혼란을 줄이기 위해 아래 순서로 작성하는 것을 권장합니다.
> 
> **위치 인자 → 기본 인자 → 가변 인자(*args) → 가변 키워드 인자(kwargs)

```Python

def func(pos1, pos2, default_arg='default', *args, **kwargs):
    ...
```
---
### 4. 입력값과 결과값에 따른 함수의 형태
> 함수는 들어오는 값(Input)과 나가는 값(Output)의 유무에 따라 4가지 형태가 있습니다.

#### 1) 일반적인 함수 (입력 O, 출력 O)

```Python

def add(a, b): 
    result = a + b 
    return result

# 사용법: 결괏값을 받을 변수 = 함수명(입력인수1, 입력인수2, ...)
a = add(3, 4)
```
#### 2) 입력값이 없는 함수 (입력 X, 출력 O)

```Python

def say(): 
    return 'Hi' 

# 사용법: 결괏값을 받을 변수 = 함수명()
a = say()
```
#### 3) 결과값이 없는 함수 (입력 O, 출력 X)

```Python

def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
    # return이 없음

# 사용법: 함수명(입력인수1, 입력인수2, ...)
add(3, 4)
```
#### 4) 입력값도 결과값도 없는 함수 (입력 X, 출력 X)

```Python

def say(): 
    print('Hi')

# 사용법: 함수명()
say()
```
### 5. 입력값이 몇 개가 될지 모를 때 (*args)
> 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어줍니다.

```Python

def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result 

result = add_many(1, 2, 3)      # 6
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 55
```
---
### 6. 함수의 결과값은 언제나 하나이다
> return a+b, a*b 처럼 2개를 돌려주면, 자동으로 튜플 (합, 곱) 1개로 묶어서 반환합니다.

```Python

def add_mul(a, b): 
    return a+b, a*b

result = add_mul(3, 4)
# result -> (7, 12)

# 값을 분리해서 받고 싶을 때
sum, mul = add_mul(3, 4)
# sum -> 7, mul -> 12
```
### 7. 매개변수 초깃값 미리 설정하기
> 매개변수에 미리 값을 넣어두면, 호출할 때 값을 안 넣어도 기본값이 사용됩니다.  
> 주의: 초기화하고 싶은 매개변수는 항상 맨 뒤에 둬야 합니다.  

```Python

def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박응용", 27)        # man은 기본값 True 적용
say_myself("박응용", 27, False) # man에 False 적용
```
---
### 8. 함수 안에서 함수 밖의 변수를 변경하는 법 (global)
> 함수 안에서 사용하는 변수는 기본적으로 함수 안에서만 유효합니다.  
> 밖의 변수를 쓰려면 global 키워드가 필요하지만, 가급적 return을 사용하는 것이 좋습니다.

```Python

a = 1 
def vartest(): 
    global a 
    a = a + 1 

vartest() 
# a -> 2
```
---
### 9. lambda (람다)
> 함수를 한 줄로 간결하게 만들 때 사용합니다.
> def를 사용할 수 없는 곳(리스트 내부 등)에 주로 쓰입니다.

#### 구조: lambda 매개변수1, 매개변수2, ... : 표현식

```Python

# 일반 함수
def add(a, b):
    return a+b

# 람다 표현식 (위와 동일)
add = lambda a, b: a+b
result = add(3, 4)  # 7
```
