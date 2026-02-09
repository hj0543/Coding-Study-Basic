# 5. 딕셔너리 자료형 (Dictionary)

### 1. 딕셔너리란?
> **Key(키)** 와 **Value(값)** 의 쌍으로 이루어진 자료형입니다.  
> 순차적으로 요소값을 구하지 않고 **Key를 통해 Value를 얻는 것**이 가장 큰 특징입니다. (Java의 Map, JS의 JSON과 유사) -> **순서와 중복이 없는 변경 가능**한 자료형 (indexing 불가능)

#### key
* 고유해야함 -> 중복될 수 없음.
* 변경 불가능한 자료형만 사용 가능(str, int, float, tuple)**(list, dict X)**
#### value : 키에 해당하는 실제 데이터
* 어떤 자료형이든 자유롭게 사용 가능
-> 실제 사전 생각하면 됨.
```python
my_dict ={}
my_dict2 = {'key': 'value'}
my_dict3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict)    # {}
print(my_dict2)   # {'key': 'value'}
print(my_dict3)  # {'apple': 12, 'list': [1, 2, 3]}
```
**기본 생김새:** `{Key1: Value1, Key2: Value2, ...}`

```python
# 다양한 딕셔너리 형태
dic = {'name': 'pey', 'phone': '0109993323', 'birth': '1118'}
a = {1: 'hi'}
b = {'a': [1, 2, 3]}  # Value에는 리스트도 넣을 수 있음
```
---
### 2. 딕셔너리 쌍 추가, 수정, 삭하기
> 딕셔너리는 순서가 없으므로 인덱싱(순서)이 아닌 Key를 사용합니다.

```Python
my_dict = {'apple': 12, 'list': [1, 2, 3]}

# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 수정
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}

# 삭제
del my_dict['list']
print(my_dict)  # {'apple': 100, 'banana': 50}

```
---
### 3. 딕셔너리 사용하는 법 (중요 ⭐)
> 리스트나 튜플, 문자열은 인덱싱이나 슬라이싱을 하지만, 딕셔너리는 오직 Key를 사용해 Value를 얻습니다.

```Python

grade = {'pey': 10, 'julliet': 99}

# Key를 사용해 Value 얻기(Key에 접근 시 대괄호'[]' 사용)
grade['pey']      # 10
grade['julliet']  # 99

a = {1: 'a', 2: 'b'}
a[1]  # 'a' (리스트의 0번째, 1번째가 아니라 Key가 1인 값을 찾음)
a[2]  # 'b'
```

#### 학생 정보가 담긴 중첩 딕셔너리
```Python
# 학생 정보가 담긴 중첩 딕셔너리
students = {
    "철수": {
        "나이": 20,
        "전공": "컴퓨터공학"
    },
    "영희": {
        "나이": 22,
        "전공": "시각디자인"
    }
}

# 1. '철수'의 '전공'을 찾고 싶을 때
major = students["철수"]["전공"]
print(major)  # 결과: 컴퓨터공학

# 2. '영희'의 '나이'를 찾고 싶을 때
age = students["영희"]["나이"]
print(age)    # 결과: 22
```
**get을 사용하기**
```python
# 철수의 전공 찾기
major = students.get("철수").get("전공")
print(major)  # 결과: 컴퓨터공학

# 존재하지 않는 키를 찾을 경우 (에러 대신 None 반환)
address = students.get("철수").get("주소")
print(address) # 결과: None
```

---
### 4. 딕셔너리 만들 때 주의사항
> 중복 Key 사용 금지: Key가 중복되면 하나를 제외한 나머지는 무시됩니다.  
> Key에 리스트 사용 금지: Key는 변하지 않는 값(Immutable)이어야 하므로 리스트는 쓸 수 없습니다.  
(단, 튜플은 사용 가능)

```Python

# 중복 Key (뒤의 값이 덮어씀)
a = {1: 'a', 1: 'b'}
# a -> {1: 'b'}

# Key에 리스트 사용 불가 (오류 발생)
# a = {[1, 2]: 'hi'} -> TypeError 발생
```
---
### 5. 딕셔너리 관련 함수 (Methods)
#### 1) keys: Key 리스트 만들기

* a.keys() -> dict_keys(['name', 'phone', 'birth'])

* 리스트로 변환하려면: list(a.keys())

#### 2) values: Value 리스트 만들기

* a.values() -> dict_values(['pey', '0119993323', '1118'])

#### 3) items: Key, Value 쌍 얻기 (튜플 형태)

* a.items() -> dict_items([('name', 'pey'), ('phone', '011999')])

#### 4) clear: 쌍 모두 지우기

* a.clear() -> {} (빈 딕셔너리)

#### 5) get: Key로 Value 얻기 (안전한 방법)

* a.get('name') -> 'pey'

* a['nokey'] -> 오류 발생

* a.get('nokey') -> None 반환 (오류 없음)

* a.get('nokey', 'foo') -> 'foo' (값이 없으면 디폴트 값 반환)

#### 6) in: 해당 Key가 딕셔너리 안에 있는지 조사

* 'name' in a -> True

* 'email' in a -> False

```Python

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

# keys() 사용 및 리스트 변환
list(a.keys())  # ['name', 'phone', 'birth']

# get() vs []
# print(a['nokey']) -> Error!
print(a.get('nokey'))  # None (에러 안 남)
print(a.get('foo', 'bar')) # 'bar' (기본값 설정 가능)

# in (조사)
'name' in a     # True
'email' in a    # False
```
