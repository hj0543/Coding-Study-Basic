# 함수
특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

### 함수를 사용하는 이유
* 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
* 재사용성이 높아지고, 코드의 가독성과 유지보수성 향상

#### 1-함수 정의
* 함수 정의는 def 키워드로 시작
* def 키워드 이후 함수 이름 작성  

#### 2-함수 body
* 콜론(:) 다음에 들여쓰기 된 코드 블록 

#### 3-Docstring
* 함수 body 앞에 선택적으로 작성 가능한 함수 설명서  

#### 4-함수 반환 값
> 함수는 **필요한 경우** 결과를 반환할 수 있음
> return 키워드 이후에 반환할 값을 명시
> return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환  
> 함수 내에서 return 문이 없다면 None이 반환  

#### 5-함수 호출
> 함수를 사용하기 위해서는 호출이 필요
> 함수의 이름과 소괄호를 활용해 호출
> 필요한 경우 인자(argument)를 전달해야 함
> 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨

### 함수와 반환 값 (첫 번째 고비)
* print() 함수는 반환값이 없음 (반환 != 출력)
* 파이썬에서 반환 값이 없는 함수는 기본적으로 None을 반환한다고 간주되기 때문임.
```python
def my_func():
    """
    Docstring for my_func
    이 함수는 호출되면 터미널에 hello를 출력하는 함수입니다.
    """
    print("hello")

result3 = my_func()  # hello 출력
print(result3)  # None 출력
```

### 매개변수와 인자 (두 번째 고비)
* 매개변수 : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수 
  -> ★ 어떤 데이터인지 알 수 있는 명확한 이름
* 인자 : 함수를 호출할 때, 실제로 전달되는 값
```Python
def add_numbers(x, y):  # x와 y는 매개변수(parameter)
    result = x + y
    return result

a = 2
b = 3

sum_result = add_numbers(a, b)  # a와 b는 인자(argument)
print(sum_result)
```

#### 1) 인자의 종류
* 위치 인자 (Positional Arguments)
> 함수 호출 시 인자의 위치에 따라 매개변수에 값이 그대로 전달된다.
> 
> 호출 시 반드시 값을 전달해야 한다.
> 
> 순서가 바뀌면 의도치 않은 결과가 나올 수 있다.
```Python

def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.  
greet('25', Alice) # 안녕하세요, 25님! Alice살이시군요.  
greet('Alice') # Type Error  
```

* 기본 인자 값 (Default Argument Values)
> 함수 정의 시 매개변수에 미리 기본값을 할당하는 방식
> 
> 인자를 전달하지 않으면 설정된 기본값이 사용된다.
```python
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') # 안녕하세요, Bob님! 30살이시군요.  
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.      
```

* 키워드 인자 (Keyword Arguments)
> 인자의 이름을 명시하여 값을 전달한다.
> 
> 인자의 순서는 중요하지 않으며, 특정 매개변수에 값을 직접 할당할 수 있다.
> 
> 주의: 호출 시 키워드 인자는 반드시 위치 인자 뒤에 위치해야 한다.
```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name = 'Dave', age = 35) # 안녕하세요, Dave님! 35살이시군요.       
greet(age = 35, name = 'Dave') # 안녕하세요, Dave님! 35살이시군요.     

greet(age = 35, 'Dave') # positional argument follows keyword argument.
```

#### 2) 왜 위치 인자가 키워드 인자보다 앞에 와야 할까?
> 순서의 모호성 때문
> 
> 위치 인자는 순서에 의존하여 값이 전달되는데, 이미 키워드 인자로 순서가 깨진 상태에서 이름 없는 값(위치 인자)을 던지면 컴퓨터가 해당 값이 몇 번째 자리에 들어가야 하는지 판단할 수 없게 됩니다.
> 순서 의존 : 위치 인자는 첫 번째, 두 번째라는 순서에 따라 값이 전달됨
> 순서 파괴 : 키워드 인자는 순서를 무시하고 이름을 직접 지정함

#### 3) 함수 인자 권장 작성 순서
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