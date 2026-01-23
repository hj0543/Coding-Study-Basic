## 1) if / elif / else의 역할

* **if**: 조건이 참(True)이면 해당 블록 실행
* **elif**: (else if) 앞의 조건들이 거짓(False)일 때, *추가 조건*을 검사
* **else**: 위의 모든 조건이 거짓일 때 실행(“그 외 전부”)

핵심은 **위에서 아래로 한 줄씩 검사하다가, 처음으로 True가 나온 블록 하나만 실행하고 끝**난다는 점입니다.

---

## 2) 기본 문법(형태)

```python
if 조건식1:
    실행문A
elif 조건식2:
    실행문B
elif 조건식3:
    실행문C
else:
    실행문D
```

* `elif`는 **0개 이상** 가능
* `else`는 **선택**(없어도 됨)
* `:` 필수, 들여쓰기(보통 4칸)로 블록 구분

---

## 3) 실행 흐름(중요)

예시:

```python
x = 75

if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
else:
    print("F")
```

* `x >= 90` 거짓 → 다음으로
* `x >= 80` 거짓 → 다음으로
* `x >= 70` 참 → `"C"` 출력 후 **종료**
* `else`는 실행되지 않음

즉, **여러 조건이 동시에 참이어도 “첫 True”만 실행**합니다.

---

## 4) 조건식이란?

조건식은 결과가 **True/False**로 평가되는 표현식입니다.

### (1) 비교 연산자

* `==` 같다, `!=` 다르다
* `<, <=, >, >=`

```python
if a == 10:
    ...
```

### (2) 논리 연산자

* `and` : 둘 다 참일 때 참
* `or` : 하나라도 참이면 참
* `not` : 참/거짓 반전

```python
if age >= 19 and has_id:
    ...
```

### (3) 멤버십 / 포함 여부

* `in`, `not in`

```python
if "a" in word:
    ...
```

### (4) “Truthy / Falsy” (파이썬 특징)

파이썬은 True/False가 아니라도 조건에 올 수 있고, 다음은 보통 False 취급됩니다.

* `0`, `0.0`
* `""` (빈 문자열)
* `[]`, `{}`, `set()` (빈 컨테이너)
* `None`

```python
s = ""
if s:          # 빈 문자열이면 False
    print("있음")
else:
    print("비어있음")
```

---

## 5) 자주 쓰는 패턴

### 패턴 A) 범위 체크(점수/구간)

순서를 잘 잡아야 합니다.

```python
score = 83
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### 패턴 B) “조기 종료” 가드(guard)

예외/불가능 케이스를 먼저 걸러서 코드를 단순화합니다.

```python
if n <= 0:
    print("양수만 가능")
else:
    print(n * 2)
```

### 패턴 C) 조건을 변수로 뽑아 가독성 올리기

```python
is_adult = age >= 19
if is_adult:
    ...
```

### 패턴 D) 중첩 if (필요할 때만)

```python
if x > 0:
    if x % 2 == 0:
        print("양수 짝수")
    else:
        print("양수 홀수")
else:
    print("0 또는 음수")
```

---

## 6) 흔한 실수 TOP

### 실수 1) `=` 와 `==` 혼동

* `=`: 대입(할당)
* `==`: 비교

```python
# if x = 3:  (오류)
if x == 3:
    ...
```

### 실수 2) 범위 조건 순서가 잘못됨

아래는 전부 `"통과"`만 나옵니다. (10 이상이면 이미 첫 if가 True)

```python
x = 95
if x >= 10:
    print("통과")
elif x >= 90:
    print("A")
```

### 실수 3) `if` 여러 개를 `elif` 대신 써서 중복 실행됨

`if`를 연속으로 쓰면 “각각 독립”이라 여러 번 실행될 수 있습니다.

```python
x = 95
if x >= 90:
    print("A")
if x >= 80:
    print("B")  # 이것도 출력됨
```

반면 `elif`면 하나만 출력됩니다.

### 실수 4) 조건식에서 항상 True가 되는 표현

```python
if x == 1 or 2:   # 틀림 (항상 True로 평가될 수 있음)
    ...
```

올바른 방식:

```python
if x == 1 or x == 2:
    ...
# 또는
if x in (1, 2):
    ...
```

---

## 7) 한 줄 조건식(삼항 연산자)

간단한 대입에는 깔끔합니다.

```python
result = "합격" if score >= 60 else "불합격"
```
