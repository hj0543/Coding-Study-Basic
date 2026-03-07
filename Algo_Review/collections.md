
## 1. collections 모듈 (deque, Counter)

`collections`는 파이썬의 기본 자료구조(list, dict, tuple)를 확장하여 더 편리하고 강력한 기능을 제공하는 모듈이야.

### 💡 핵심 기능

1. **`deque` (데크):** 양방향 큐. 리스트보다 **삽입/삭제가 훨씬 빠름 ($O(1)$)**. BFS(너비 우선 탐색) 구현 시 필수야.
2. **`Counter` (카운터):** 등장 횟수 세기. 리스트나 문자열에서 **각 요소가 몇 번 나왔는지** 딕셔너리 형태로 바로 반환해 줘.

### 💻 기본 코드 (Python)

```python
from collections import deque, Counter

# 1. deque 사용법
q = deque([2, 3, 4])
q.append(5)      # 오른쪽 끝에 삽입
q.appendleft(1)  # 왼쪽 끝에 삽입
q.popleft()      # 왼쪽 끝에서 꺼내기 (O(1))
q.pop()          # 오른쪽 끝에서 꺼내기 (O(1))

# 2. Counter 사용법
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(data)
print(counts['apple'])     # 결과: 3
print(counts.most_common(1)) # 가장 많이 등장한 요소 1개 추출: [('apple', 3)]

```

---

## 2. bisect 모듈 (이진 탐색)

정렬된 배열에서 특정 원소를 찾거나, **원소가 들어갈 적절한 위치**를 찾을 때 사용하는 모듈이야. 직접 이진 탐색을 구현할 필요 없이 단 한 줄로 해결 가능해.

### 💡 핵심 기능

1. **`bisect_left(list, x)`:** 정렬을 유지하면서 리스트에 `x`를 삽입할 가장 왼쪽 인덱스를 반환해.
2. **`bisect_right(list, x)`:** 정렬을 유지하면서 리스트에 `x`를 삽입할 가장 오른쪽 인덱스를 반환해.

### 💻 기본 코드 (Python)

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

# 리스트 a에서 x가 들어갈 수 있는 왼쪽/오른쪽 위치 찾기
print(bisect_left(a, x))  # 결과: 2 (인덱스 2번 자리)
print(bisect_right(a, x)) # 결과: 4 (인덱스 4번 자리)

# 응용: 특정 범위 [left_value, right_value]에 속하는 원소 개수 구하기
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

print(count_by_range(a, 4, 4)) # 결과: 2 (4의 개수)
print(count_by_range(a, 2, 7)) # 결과: 3 (2, 4, 4)

```

### ⏱️ 시간 복잡도

이진 탐색 기반이므로 **$O(\log N)$**이야. 정렬된 대량의 데이터에서 특정 값의 개수를 세거나 위치를 찾을 때 `list.count()`($O(N)$)보다 압도적으로 빨라.

---

## 📝 예시 문제: 숫자 카드 2 (백준 10816번)

상근이는 숫자 카드 $N$개를 가지고 있다. 정수 $M$개가 주어졌을 때, 이 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

* **입력:** 카드 개수 $N$ ($1 \le N \le 500,000$), 카드 적힌 수, 질문 개수 $M$ ($1 \le M \le 500,000$).
* **접근:** $N$과 $M$이 매우 크므로 매번 리스트를 뒤지면 안 돼. **`Counter`**를 쓰거나, 정렬 후 **`bisect`**로 개수를 세면 끝이야.

### 💻 풀이 코드 (Python - Counter 버전)

```python
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 모든 카드의 개수를 한 번에 센다 (O(N))
counts = Counter(cards)

# 질문에 대해 바로 답을 출력 (O(M))
for t in targets:
    print(counts[t], end=' ')

```