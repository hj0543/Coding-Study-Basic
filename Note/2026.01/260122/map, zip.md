
# 📝 파이썬 내장 함수: map과 zip

데이터를 효율적으로 변환하고 묶어주는 강력한 도구들이다.

## 1. map 함수

**`map(function, iterable)`**
반복 가능한 데이터(리스트 등)의 **모든 요소에 특정 함수를 적용**하고, 그 결과를 `map object`로 반환한다.

### 특징

* **지연 실행 (Lazy Evaluation)**: 결과가 바로 리스트로 나오지 않고, 메모리 효율을 위해 `map object` 형태로 반환된다.
* 눈으로 결과를 확인하려면 `list()`와 같은 형변환이 필요하다.

### ① 기본 사용법

숫자 리스트를 문자열 리스트로 변환하는 예시이다.

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)       # <map object at ...> (주소값 출력)
print(list(result)) # ['1', '2', '3'] (리스트로 변환해야 내용 보임)

```

### ② 활용 1: 입력값 처리 (필수 암기 패턴)

알고리즘 문제 풀이 등에서 사용자 입력을 받아 숫자로 변환할 때 가장 많이 사용한다.
`input().split()`은 문자열 리스트를 반환하므로, 이를 한 번에 정수로 바꿀 때 유용하다.

```python
# 사용자 입력: "10 20 30" (공백으로 구분)
input_data = "10 20 30" # 예시를 위해 변수로 대체

# 1. 문자열 리스트 생성
print(input_data.split()) # ['10', '20', '30']

# 2. 정수 리스트로 변환
numbers = list(map(int, input_data.split()))
print(numbers) # [10, 20, 30]

```

### ③ 활용 2: 람다(Lambda)와 함께 사용

단순한 연산을 적용할 때, 굳이 함수를 따로 정의하지 않고 `lambda`를 사용하면 코드가 간결해진다.

```python
numbers = [1, 2, 3, 4, 5]

# 일반 함수 정의
def square(x):
    return x**2
    
print(list(map(square, numbers))) # [1, 4, 9, 16, 25]

# 람다 함수 사용 (권장)
print(list(map(lambda x: x**2, numbers))) # [1, 4, 9, 16, 25]

```

---

## 2. zip 함수

**`zip(*iterables)`**
여러 개의 반복 가능한 데이터를 받아, **같은 인덱스(위치)에 있는 요소끼리 묶어 튜플(Tuple)**로 반환한다.

### 특징

* 옷의 지퍼(Zipper)처럼 양쪽을 맞물리게 하는 원리다.
* `map`과 마찬가지로 `zip object`를 반환하므로 리스트 등으로 변환해야 내용을 볼 수 있다.

### ① 기본 사용법

두 개의 리스트를 하나로 묶는 예시이다.

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']

pair = zip(girls, boys)
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]

```

### ② 활용 1: 여러 데이터 동시 순회

국어, 수학, 영어 점수가 각각 다른 리스트에 있을 때, 학생별로 점수를 묶어서 처리할 수 있다.

```python
kr = [10, 20, 30]
math = [20, 40, 50]
en = [40, 20, 30]

for scores in zip(kr, math, en):
    print(scores) 
# (10, 20, 40)
# (20, 40, 20)
# (30, 50, 30)

```

### ③ 활용 2: 2차원 리스트 뒤집기 (전치 행렬)

행과 열을 바꿀 때 `*`(언패킹)과 `zip`을 함께 사용하면 매우 강력하다.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# *matrix는 [1, 2, 3], [4, 5, 6], [7, 8, 9] 세 개의 리스트로 풀린다.
# zip은 이 세 리스트의 같은 인덱스끼리 묶는다.
transposed = list(zip(*matrix))

print(transposed)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)] -> 세로로 묶임

```

### ⚠️ 주의사항: 길이가 다를 경우

반복 가능한 자료형들의 길이가 다를 경우, **가장 짧은 길이를 기준으로 묶이고 남는 요소는 버려진다.**

```python
nums = [1, 2, 3]
chars = ['a', 'b'] # 길이가 더 짧음

print(list(zip(nums, chars))) # [(1, 'a'), (2, 'b')] -> 3은 버려짐

```

*(참고: 긴 쪽에 맞추려면 `itertools.zip_longest` 함수를 사용해야 한다.)*

---

✅ **다음 단계**
`map`과 `filter`를 비교하거나, 파이썬스러운 코드의 정점인 **리스트 컴프리헨션(List Comprehension)**으로 위 내용들을 대체하는 방법을 정리해보자.