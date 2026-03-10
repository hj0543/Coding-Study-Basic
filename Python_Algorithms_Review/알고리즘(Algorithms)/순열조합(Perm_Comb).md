순열, 중복순열, 조합, 중복조합은 코딩 테스트 '완전 탐색(Brute Force)'과 '백트래킹(Backtracking)'을 정복하기 위한 4대장이다.

파이썬의 내장 모듈인 `itertools`를 쓰면 아주 쉽게 구현할 수 있지만, 문제에 **"특정 원소는 연속해서 뽑을 수 없다"** 같은 까다로운 조건(가지치기)이 붙는 순간 `itertools`는 무용지물이 된다. 따라서 재귀 함수(DFS)를 이용해 이 4가지를 직접 바닥부터 구현하는 방법은 구구단처럼 반드시 손에 익혀두어야 한다.

---

### 💡 4대장 한눈에 구별하기

이 4가지는 **'순서를 따지는가?'**와 **'중복해서 뽑아도 되는가?'** 딱 두 가지 기준으로 나뉜다.

| 구분 | 순서 (Order) | 중복 (Repetition) | 핵심 구현 논리 |
| --- | --- | --- | --- |
| **순열 (Permutation)** | O | X | 내가 이 원소를 썼는지 확인하는 **`visited`** 배열이 필요하다. |
| **중복순열 (Perm. with Repetition)** | O | O | 방문 확인 필요 없이 **그냥 무한정** 뽑으면 된다. |
| **조합 (Combination)** | X | X | 순서가 상관없으므로, 이미 뽑은 것의 **'다음 인덱스(`i + 1`)'**부터 뽑는다. |
| **중복조합 (Comb. with Repetition)** | X | O | 중복은 되지만 순서는 상관없으므로, **'현재 인덱스(`i`)'**부터 다시 뽑는다. |

---

### 💻 직접 구현 완벽 템플릿 (Python)

4가지 알고리즘 모두 기본적인 뼈대는 **"원소를 하나 넣고(`append`), 다음 깊이로 재귀 호출을 한 뒤, 돌아오면 다시 빼낸다(`pop`)"**는 백트래킹의 기본 원리를 완벽하게 공유한다. 미세한 차이점만 비교해 보라.

공통으로 사용할 기본 세팅은 다음과 같다.

```python
arr = ['A', 'B', 'C']
n = len(arr)
r = 2      # 2개를 뽑는다고 가정
out = []   # 뽑은 결과를 담을 배열

```

#### 1. 순열 (Permutation)

* **특징:** A-B와 B-A는 다르다. 똑같은 것을 두 번 뽑을 수는 없다.
* **핵심:** 방문 여부를 체크하는 `visited` 배열을 사용한다.

```python
visited = [False] * n

def perm(depth):
    if depth == r:
        print(out)
        return
        
    for i in range(n):
        if not visited[i]:         # 아직 안 뽑은 원소라면
            visited[i] = True      # 방문 처리
            out.append(arr[i])     
            
            perm(depth + 1)        # 다음 깊이로 이동
            
            out.pop()              # 원상 복구 (Backtracking)
            visited[i] = False     # 방문 처리 해제

print("--- 순열 ---")
perm(0)
# 결과: ['A', 'B'], ['A', 'C'], ['B', 'A'], ['B', 'C'], ['C', 'A'], ['C', 'B']

```

#### 2. 중복순열 (Permutation with Repetition)

* **특징:** 비밀번호 찾기처럼 A-A, B-B 중복해서 뽑을 수 있다.
* **핵심:** `visited` 배열 자체가 아예 필요 없다. 무조건 0번 인덱스부터 다 찔러본다.

```python
def perm_rep(depth):
    if depth == r:
        print(out)
        return
        
    for i in range(n):
        # 방문 체크 없이 그냥 무조건 넣음
        out.append(arr[i])
        perm_rep(depth + 1)
        out.pop()

print("--- 중복순열 ---")
perm_rep(0)
# 결과: ['A', 'A'], ['A', 'B'], ['A', 'C'], ['B', 'A'], ['B', 'B'], ...

```

#### 3. 조합 (Combination)

* **특징:** A-B와 B-A는 같은 것으로 취급한다. (순서 상관없음)
* **핵심:** 탐색의 시작점을 의미하는 `start` 변수를 넘겨받고, 재귀를 탈 때 **`i + 1`**을 넘겨준다.

```python
def comb(depth, start):
    if depth == r:
        print(out)
        return
        
    # start부터 끝까지만 탐색 (이전 인덱스는 무시)
    for i in range(start, n):
        out.append(arr[i])
        
        # '다음 인덱스'부터 뽑도록 i + 1을 넘김
        comb(depth + 1, i + 1) 
        
        out.pop()

print("--- 조합 ---")
comb(0, 0)
# 결과: ['A', 'B'], ['A', 'C'], ['B', 'C']

```

#### 4. 중복조합 (Combination with Repetition)

* **특징:** A-A, B-B처럼 중복은 허용하지만, A-B와 B-A는 여전히 같은 것으로 취급한다.
* **핵심:** `start` 변수를 넘겨받지만, 중복해서 뽑을 수 있으므로 재귀를 탈 때 **`i`**를 그대로 넘겨준다.

```python
def comb_rep(depth, start):
    if depth == r:
        print(out)
        return
        
    for i in range(start, n):
        out.append(arr[i])
        
        # 중복을 허용하므로 '현재 인덱스'를 그대로 넘김 (i + 1이 아님!)
        comb_rep(depth + 1, i) 
        
        out.pop()

print("--- 중복조합 ---")
comb_rep(0, 0)
# 결과: ['A', 'A'], ['A', 'B'], ['A', 'C'], ['B', 'B'], ['B', 'C'], ['C', 'C']

```

---

백트래킹의 뼈대 하나만 똑바로 세워두면, `visited`를 쓰느냐 마느냐, 인덱스를 `i`로 주느냐 `i + 1`로 주느냐의 아주 작은 차이만으로 이 4가지를 완벽하게 통제할 수 있다.

---

## 예제 : **'N-Queen (N-퀸)'**

크기 $N \times N$의 체스판 위에 퀸 $N$개를 서로 공격할 수 없게 놓는 경우의 수를 구하는 문제다. 퀸은 상하좌우, 대각선 8방향으로 끝까지 움직일 수 있으므로, **"같은 행, 같은 열, 같은 대각선에는 절대 다른 퀸을 둘 수 없다"**는 것이 핵심 규칙이다.

### 💡 핵심 아이디어: 1차원 배열로 압축하기 (🔥초특급 꿀팁)

초보자들이 가장 많이 하는 실수가 체스판을 2차원 배열(`board[N][N]`)로 만드는 것이다. 하지만 백트래킹의 효율을 극대화하려면 **1차원 배열 하나로 끝내야 한다.**

`row`라는 1차원 배열을 만들고, **`row[i] = j`의 의미를 "i번째 행의 j번째 열에 퀸이 있다"**라고 약속하는 것이다. 애초에 한 행에는 퀸을 하나밖에 못 두기 때문에, 이렇게 1차원 배열을 쓰면 '같은 행에 퀸이 있는지'는 검사할 필요조차 완벽하게 사라진다.

### 💻 N-Queen 완벽 템플릿 (Python)

```python
n = 8 # 8x8 체스판이라고 가정
row = [0] * n
result = 0

# 퀸을 놓을 수 있는지 (유망한지) 검사하는 함수
def is_promising(x):
    # 0번째 행부터 바로 윗행(x-1)까지만 검사하면 됨
    for i in range(x):
        # 1. 같은 열에 다른 퀸이 있는가? (row[x] == row[i])
        # 2. 대각선에 다른 퀸이 있는가? (행의 차이의 절댓값 == 열의 차이의 절댓값)
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

# x번째 행에 퀸을 놓는 함수 (DFS 백트래킹)
def n_queens(x):
    global result
    
    # 기저 조건: n개의 퀸을 모두 놓았다면 (마지막 행까지 무사히 통과했다면)
    if x == n:
        result += 1
        return
        
    # 0열부터 n-1열까지 퀸을 하나씩 놓아봄
    for i in range(n):
        row[x] = i # x번째 행, i번째 열에 퀸을 일단 둔다.
        
        # 그 자리가 유망하다면 (공격받지 않는다면) 다음 행으로 넘어간다.
        if is_promising(x):
            n_queens(x + 1)
            # 만약 유망하지 않다면? is_promising이 False이므로 
            # 재귀를 타지 않고 무시해버림 (Pruning, 가지치기!)
            
n_queens(0) # 0번째 행부터 탐색 시작
print(result)

```

---

### ⏱️ 백트래킹의 위력 (가지치기)

단순하게 모든 칸에 퀸을 놓아보는 완전 탐색의 경우의 수는 $N^N$이라는 우주적인 숫자가 나온다. 하지만 위 코드처럼 `is_promising` 함수로 **"어? 여기 놓으면 무조건 죽네? 이 밑으로는 아예 탐색 안 해!"** 하고 가차 없이 잘라버리는(Pruning) 과정 덕분에, 실제 탐색 시간은 획기적으로 줄어든다.

(물론 최악의 경우 시간 복잡도는 여전히 $O(N!)$에 가깝기 때문에, 파이썬으로 이 문제를 풀 때는 $N$이 15를 넘어가면 시간 초과가 날 확률이 매우 높다는 점은 기억해 두어야 한다.)