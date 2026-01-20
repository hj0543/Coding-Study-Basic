### None : 아무것도 없음을 나타내는 특별한 값
```python
my_variable = None
print(my_variable)  # None
```

### Boolean -> 주로 조건, 반복문과 함께 사용 됨.
```python
is_active = True
is_logged_in = False

print(is_active)      # True
print(is_logged_in)   # False
print(10 > 5)  # True
print(10 == 5) # False
```

### Python Collection 자료형 비교

파이썬의 주요 컬렉션 데이터 타입들의 특징 비교표입니다.

| 자료형 (Type) | 변경 가능 여부 (Mutable) | 순서 존재 여부 (Ordered) | 중복 허용 | 특징 및 문법 예시 |
| :--- | :---: | :---: | :---: | :--- |
| **str** (문자열) | ❌ (Immutable) | ⭕ (Sequence) | ⭕ | 문자들의 집합<br>`"Hello"` |
| **list** (리스트) | ⭕ (Mutable) | ⭕ (Sequence) | ⭕ | 가장 범용적인 배열<br>`[1, 2, 3]` |
| **tuple** (튜플) | ❌ (Immutable) | ⭕ (Sequence) | ⭕ | 수정 불가능한 리스트<br>`(1, 2, 3)` |
| **dict** (딕셔너리)| ⭕ (Mutable) | ⭕ (Ordered)* | ❌ (Key만) | Key:Value 쌍으로 저장<br>`{'a': 1}` |
| **set** (집합) | ⭕ (Mutable) | ❌ (Unordered) | ❌ | 중복 제거 및 집합 연산<br>`{1, 2, 3}` |

> ***참고:** Python 3.7 버전부터 `dict`는 삽입 순서를 보장합니다 (이전 버전에서는 순서가 없었습니다).*

### 1. 가변 자료형 (Mutable)
생성된 후에 값을 변경할 수 있는 객체입니다.  
메모리 주소(id)를 유지한 채로 내용을 수정, 추가, 삭제할 수 있습니다.

#### 특징:
* 데이터의 수정이 빈번할 때 유용합니다.
* dict의 Key나 set의 원소로 사용할 수 없습니다 (값이 변할 수 있기 때문에 해시값을 고정할 수 없음).
* 종류: list, dict, set
```python
# 리스트는 내용물을 바꿀 수 있습니다.
my_list = [1, 2, 3]
print(f"변경 전 ID: {id(my_list)}")

my_list[0] = 99  # 첫 번째 값을 99로 변경
print(my_list)   # 출력: [99, 2, 3]

# 내용을 바꿨지만, 리스트 자체의 주소(ID)는 같습니다.
print(f"변경 후 ID: {id(my_list)}")
```

### 2. 불변 자료형 (Immutable)
한 번 생성되면 값을 변경할 수 없는 객체입니다. 값을 바꾸려 하면, 실제로는 수정되는 것이 아니라 새로운 객체가 생성되는 것입니다.

특징:

* 값이 변하지 않음을 보장하므로 안전합니다.

* dict의 Key, set의 원소로 사용할 수 있습니다.

* 수정하려 하면 에러가 나거나, 아예 새로운 주소를 가진 변수가 됩니다.

* 종류: int, float, str, tuple, bool
```python
text = "Python"

# 문자열의 특정 문자를 바꾸려고 하면 에러가 발생합니다.
try:
    text[0] = "J" # 'P'를 'J'로 바꾸기 시도
except TypeError as e:
    print(f"에러 발생: {e}")
    # 출력: 'str' object does not support item assignment
```
