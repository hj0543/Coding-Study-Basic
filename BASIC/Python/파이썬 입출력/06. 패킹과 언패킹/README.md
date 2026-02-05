# [Python] 패킹(Packing)과 언패킹(Unpacking)

파이썬에서는 여러 개의 값을 하나로 묶거나(Packing), 묶여있는 값을 다시 여러 개의 변수로 풀어내는(Unpacking) 편리한 기능을 제공합니다.

### 1. 패킹 (Packing)

여러 개의 값을 하나의 변수에 담는 것을 의미합니다. 변수에 여러 값을 대입하면 자동으로 **튜플(Tuple)**로 묶입니다.

```python
# 1. 변수 할당에서의 패킹
numbers = 1, 2, 3, 4, 5
print(numbers)  # (1, 2, 3, 4, 5) -> tuple 타입

# 2. 함수 매개변수에서의 패킹 (*args)
# 매개변수 앞에 '*'를 붙이면, 전달받은 모든 위치 인자를 하나의 튜플로 묶습니다.
def sum_all(*args):
    print(args)  # (1, 2, 3)
    return sum(args)

sum_all(1, 2, 3)

```

### 2. 언패킹 (Unpacking)

리스트나 튜플 등 컬렉션(Container)에 묶여 있는 값들을 풀어서 각각의 변수나 인자로 전달하는 것을 의미합니다.

```python
# 1. 변수 할당에서의 언패킹
packed_data = (10, 20, 30)
a, b, c = packed_data  # 변수의 개수와 요소의 개수가 같아야 함

print(a)  # 10
print(b)  # 20
print(c)  # 30

# 2. 함수 호출 시의 언패킹 (*)
# 리스트나 튜플 앞에 '*'를 붙이면, 요소들을 풀어서 각각의 인자로 전달합니다.
def add(x, y):
    return x + y

numbers = [10, 20]
# add(numbers) -> 에러 발생 (인자는 2개 필요한데 리스트 1개만 전달됨)
add(*numbers)  # add(10, 20)과 동일하게 동작

```

### 3. `*` (Asterisk)와 `**` (Double Asterisk)의 차이

#### `*` (Asterisk): 리스트/튜플

* **패킹:** 여러 개의 인자를 **튜플**로 묶음 (`*args`)
* **언패킹:** 리스트나 튜플의 요소를 풀어서 전달

#### `**` (Double Asterisk): 딕셔너리

* **패킹:** 여러 개의 키워드 인자를 **딕셔너리**로 묶음 (`**kwargs`)
* **언패킹:** 딕셔너리의 키-값 쌍을 풀어서 키워드 인자로 전달

```python
def print_info(name, age):
    print(f"이름: {name}, 나이: {age}")

user_info = {'name': 'Alice', 'age': 30}

# 딕셔너리 언패킹: **를 사용하여 키워드 인자로 전달
print_info(**user_info)  # print_info(name='Alice', age=30) 와 동일

```

### 4. 활용 팁: 남은 요소 할당하기

언패킹 시 `*`를 변수 앞에 붙이면, 남은 요소들을 리스트로 묶어 할당할 수 있습니다.

```python
numbers = [1, 2, 3, 4, 5]

first, *rest, last = numbers

print(first) # 1
print(rest)  # [2, 3, 4] -> 남은 요소들이 리스트로 패킹됨
print(last)  # 5

```
