세그먼트 트리(Segment Tree)는 여러 개의 데이터가 연속적으로 존재할 때, **특정 구간의 합(또는 최솟값, 최댓값, 곱 등)을 빠르고 효율적으로 구하기 위해 사용하는 이진트리 형태의 자료구조**다.

배열의 특정 구간 합을 구할 때 보통 '누적 합(Prefix Sum)' 배열을 사용하지만, 중간에 데이터가 빈번하게 변경(Update)되는 상황이라면 누적 합 배열을 매번 다시 계산해야 하므로 효율성이 크게 떨어진다. 세그먼트 트리는 이렇게 **데이터 변경과 구간 연산(쿼리)이 모두 자주 일어나는 상황**에서 진가를 발휘한다.

### 💡 알고리즘 동작 과정

세그먼트 트리의 각 노드는 배열의 특정 구간에 대한 연산 결과(예: 구간 합)를 저장한다. 루트 노드는 전체 구간의 결과를, 자식 노드들은 부모 노드가 담당하는 구간의 절반씩을 나누어 담는다.

1. **트리 초기화 (Init):** 주어진 원본 배열을 바탕으로 이진트리를 재귀적으로 구성한다. 리프 노드는 원본 배열의 개별 데이터이고, 부모 노드는 두 자식 노드의 합을 저장한다.
2. **데이터 변경 (Update):** 특정 인덱스의 값이 변경되면, 해당 데이터가 위치한 리프 노드의 값을 수정한다. 이후 부모 노드로 거슬러 올라가면서 루트 노드에 도달할 때까지 트리의 각 노드 값을 다시 계산하여 갱신한다.
3. **구간 연산 (Query):** 구하고자 하는 목표 구간과 현재 노드가 담당하는 구간을 비교한다.
* 노드의 구간이 목표 구간에 완전히 포함되면 그 노드의 값을 반환한다.
* 노드의 구간이 목표 구간과 전혀 겹치지 않으면 의미 없는 값(합 구하기의 경우 0)을 반환한다.
* 구간이 일부만 겹친다면, 자식 노드로 내려가며 위 과정을 반복한 뒤 결과를 합쳐서 반환한다.



> **참고:** 세그먼트 트리를 배열로 구현할 때, 트리의 크기는 데이터의 개수 $N$에 대해 넉넉하게 **$N \times 4$**로 설정하는 것이 일반적이고 안전하다.

---

### 💻 세그먼트 트리 기본 코드 (Python)

가장 기본이 되는 '구간 합 구하기' 목적의 세그먼트 트리 뼈대 코드다.

```python
# 원본 배열 arr, 세그먼트 트리 tree
arr = [1, 2, 3, 4, 5]
n = len(arr)
tree = [0] * (n * 4) # 트리의 크기는 4N으로 넉넉하게 할당

# 1. 트리 초기화 함수 (node: 현재 노드 인덱스, start~end: 노드가 담당하는 원본 배열 구간)
def init(node, start, end):
    # 리프 노드인 경우 (구간의 시작과 끝이 같은 경우) 원본 배열의 값을 트리에 저장
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    # 왼쪽 자식과 오른쪽 자식 트리를 재귀적으로 초기화하고, 두 값의 합을 부모 노드에 저장
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

# 2. 데이터 변경 함수 (index: 변경할 원본 배열 인덱스, diff: 변경된 차이값)
def update(node, start, end, index, diff):
    # 변경할 인덱스가 현재 노드의 담당 구간에 포함되지 않으면 무시
    if index < start or index > end:
        return
    
    # 구간에 포함된다면 현재 노드의 값 갱신
    tree[node] += diff
    
    # 리프 노드가 아니라면 자식 노드들도 재귀적으로 갱신
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

# 3. 구간 합 구하기 함수 (left~right: 합을 구하고자 하는 목표 구간)
def query(node, start, end, left, right):
    # 1) 목표 구간이 현재 노드의 구간과 전혀 겹치지 않는 경우
    if left > end or right < start:
        return 0
    
    # 2) 목표 구간이 현재 노드의 구간을 완전히 포함하는 경우
    if left <= start and end <= right:
        return tree[node]
    
    # 3) 구간이 일부만 겹치는 경우, 자식 노드들로 내려가서 탐색 후 합산
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

# 초기화 실행 (루트 노드는 1번 인덱스, 배열 구간은 0 ~ n-1)
init(1, 0, n - 1)

```

### ⏱️ 시간 복잡도

* **트리 초기화:** $O(N)$
* **데이터 변경 (Update):** $O(\log N)$ (루트에서 리프까지 트리의 높이만큼만 탐색)
* **구간 연산 (Query):** $O(\log N)$

만약 데이터 변경이 $M$번, 구간 합 쿼리가 $K$번 일어난다면 세그먼트 트리의 총시간 복잡도는 **$O((M+K)\log N)$** 이다. 변경이 일어날 때마다 매번 $O(N)$이 걸리는 단순 배열 탐색에 비해 획기적으로 빠르다.

---

### 📝 예시 문제: 구간 합 구하기 (백준 2042번)

어떤 $N$개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 $1,2,3,4,5$ 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다.

* **입력:** 첫째 줄에 수의 개수 $N$ ($1 \le N \le 1,000,000$)과 수의 변경이 일어나는 횟수 $M$, 구간의 합을 구하는 횟수 $K$가 주어진다. 둘째 줄부터 $N+1$번째 줄까지 수가 주어진다. 다음 $M+K$개의 줄에는 세 개의 정수 $a, b, c$가 주어지는데, $a$가 1인 경우 $b$번째 수를 $c$로 바꾸고 $a$가 2인 경우에는 $b$번째 수부터 $c$번째 수까지의 합을 구하여 출력하면 된다.
* **출력:** 첫째 줄부터 $K$줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -2^63보다 크거나 같고, 2^63-1보다 작거나 같은 정수이다. (파이썬은 정수 오버플로우를 크게 신경 쓰지 않아도 된다.)

---

### 💡 풀이 접근법

문제 이름 그대로 세그먼트 트리를 구현하는 가장 스탠다드한 문제다. 값의 변경과 구간 합 연산이 빈번하게 섞여서 주어지므로, 일반적인 1차원 배열이나 누적 합으로는 시간 초과가 발생한다.

* **주의할 점:** 문제에서 배열 인덱스는 1부터 시작하는 것으로 입력이 들어온다 ($b$번째 수). 우리가 구현한 트리 함수는 0-based 인덱스를 기준($0$ ~ $N-1$)으로 하므로, 함수를 호출할 때 입력받은 $b$와 $c$에서 1을 빼주어 인덱스를 맞춰주는 것이 핵심이다.
* $a=1$일 때 단순 덧셈이 아니라 $b$번째 수를 $c$로 **교체**하는 것이므로, 기존 값과의 차이(`diff = c - arr[b-1]`)를 구해서 `update` 함수에 넘겨주고, 원본 배열 `arr`의 값도 $c$로 업데이트해 주어야 한다.

---

### 💻 풀이 코드 (Python)

```python
import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (n * 4)

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        # b번째 수를 c로 변경 (인덱스는 b-1)
        b -= 1
        diff = c - arr[b] # 기존 값과의 차이 계산
        arr[b] = c        # 원본 배열 업데이트
        update(1, 0, n - 1, b, diff) # 세그먼트 트리 업데이트
    elif a == 2:
        # b번째부터 c번째까지의 합 (인덱스는 b-1, c-1)
        print(query(1, 0, n - 1, b - 1, c - 1))

```

---

세그먼트 트리는 코드가 다소 길고 복잡해 보이지만, 이 뼈대만 외워두면 최솟값/최댓값을 구하는 문제 등으로 쉽게 변형해서 사용할 수 있다.