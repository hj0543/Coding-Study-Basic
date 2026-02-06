## [TIL] Python 큐(Queue) 회전과 람다(Lambda) 정렬 정복하기

### 1. 큐(Queue) 회전시키기 (ft. 요세푸스 문제)

큐의 맨 앞(왼쪽)에 있는 원소를 꺼내서 다시 맨 뒤(오른쪽)로 보내는 동작. 흔히 '회전한다'고 표현함.

#### 방법 1: 직접 구현

`popleft()`로 꺼낸 값을 즉시 `append()`에 넣는다.

```python
from collections import deque
q = deque([1, 2, 3])

q.append(q.popleft()) 
# 결과: [2, 3, 1] (반시계 방향 1칸 회전)

```

#### 방법 2: `rotate()` 함수 사용 (추천 ⭐️)

`collections.deque`의 내장 메서드를 사용하면 훨씬 직관적이고 빠르다.

* **음수(-)**: 왼쪽으로 회전 (앞 -> 뒤)
* **양수(+)**: 오른쪽으로 회전 (뒤 -> 앞)

```python
q.rotate(-1)  # 왼쪽으로 1칸 회전 (위의 코드와 동일)
q.rotate(-2)  # 왼쪽으로 2칸 회전

```

> **Tip:** 요세푸스 문제(백준 1158번)처럼 번째 사람을 제거해야 할 때, 매번 번 반복문을 돌리는 대신 `q.rotate(-(k-1))` 한 줄로 처리가 가능하다.

### 2. 정렬 시 다중 조건 설정하기 (`key=lambda`)

`sort()` 함수 사용 시 `key` 인자에 **튜플(tuple)**을 넘기면 여러 개의 정렬 기준을 순서대로 적용할 수 있다.

#### 핵심 문법

```python
# 기준 1: 길이(len(x)) -> 짧은 순
# 기준 2: 단어(x) -> 사전 순 (길이가 같을 때만 적용됨)
words.sort(key=lambda x: (len(x), x))

```
### 백준 10814
```python
import sys
input = sys.stdin.readline

N = int(input())
#21 Junkyu
# 21 Dohyun
# 20 Sunyoung

members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name])

members.sort(key=lambda x: (x[0]))

for member in members:
    print(*member)
    
# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun
```
#### 원리 이해 (백준 1181번)

파이썬은 튜플을 비교할 때 **앞에서부터 순차적으로** 비교한다.

1. `len(x)`를 먼저 비교해 정렬.
2. 만약 `len(x)`가 같다면, 그제서야 뒤에 있는 `x`(단어 자체)를 비교해 사전 순 정렬.
3. 데이터(단어)는 정렬된 순서에 맞춰서 통째로 이동한다.

### 3. 숫자 리스트를 문자열로 합치기 (`join` 에러 해결)

`join()` 함수는 **문자열(str) 리스트**만 합칠 수 있다. 숫자(int) 리스트를 넣으면 `TypeError` 발생.

#### 에러 코드

```python
arr = [1, 2, 3]
print(", ".join(arr)) 
# TypeError: sequence item 0: expected str instance, int found

```

#### 해결 방법 (`map` 활용)

`map(str, 리스트)`를 사용해 내부 원소를 모두 문자로 변환한 뒤 합친다.

```python
arr = [1, 2, 3]
# 1. map으로 숫자를 문자로 변환: [1, 2, 3] -> ["1", "2", "3"]
# 2. ", "로 이어 붙이기
print(", ".join(map(str, arr)))
# 결과: "1, 2, 3"

```

---

### 💡 오늘의 교훈

1. **Deque의 `rotate**`: 큐를 뱅글뱅글 돌려야 한다면 `rotate`를 기억하자. 코드가 훨씬 짧아진다.
2. **Lambda 정렬**: "길이 순으로 먼저, 그 다음 사전 순으로" 같은 복합 조건은 `(우선순위1, 우선순위2)` 튜플 형태로 간단히 해결할 수 있다. 복잡한 정렬 알고리즘을 짤 필요가 없다!
