## 1) `join()` : 문자열들을 “구분자”로 이어붙여 하나의 문자열로 만들기

### 기본 형태

```python
"구분자".join(문자열_리스트)
```

예:

```python
words = ["a", "b", "c"]
print(" ".join(words))   # "a b c"
print("-".join(words))   # "a-b-c"
print("".join(words))    # "abc"
```

### 동작 원리

* `"구분자"`를 **사이에 끼워 넣으며** 문자열들을 하나로 합칩니다.
* 결과는 **새 문자열**입니다. (원본 리스트는 안 바뀜)

#### 예시로 “사이에 끼워 넣는다”는 뜻

```python
ans = ["1", "4", "2", "3"]
" ".join(ans)
```

→ `"1" + " " + "4" + " " + "2" + " " + "3"`
→ `"1 4 2 3"`

---

### `join`의 핵심 규칙: “반드시 문자열만”

`join`은 내부 요소가 문자열이어야 합니다.

```python
ans = [1, 4, 2, 3]
print(" ".join(ans))  # TypeError 발생
```

따라서 아래 중 하나가 필요합니다.

#### 방법 A: 넣을 때부터 문자열로 저장

```python
ans.append(str(x))
```

#### 방법 B: 합치기 전에 문자열로 변환

```python
print(" ".join(map(str, ans)))
```

---

## 2) `print`로 하나씩 찍는 것 vs `join`으로 한 번에 찍는 것

### 하나씩 출력 (끝 공백 처리 귀찮음)

```python
for x in ans:
    print(x, end=" ")
```

* 마지막에도 공백이 찍힐 수 있음(문제에 따라 상관 없기도 함)
* 출력 형식을 맞추기 위해 제어가 필요할 때가 많음

### `join`으로 출력 (형식 깔끔)

```python
print(" ".join(ans))
```

* 공백이 정확히 “사이”에만 들어감
* 마지막에 쓸데없는 공백이 없음

---

## 3) 자주 나오는 실수 모음


### (1) 정수 리스트를 join하기

```python
ans = [1, 2, 3]
print(" ".join(ans))  # TypeError
```
