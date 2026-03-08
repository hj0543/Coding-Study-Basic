순열(Permutation)과 조합(Combination)은 코딩 테스트에서 '모든 경우의 수'를 찾아야 하는 **완전 탐색(Brute Force)**의 가장 뼈대가 되는 개념이다.

쉽게 말해 **순열**은 "순서를 따져서 뽑는 것(A-B와 B-A는 다름)"이고, **조합**은 "순서 상관없이 뽑는 것(A-B와 B-A는 같음)"이다.

파이썬에서는 이 두 가지를 구현하는 방법이 크게 2가지가 있다. 하나는 파이썬이 제공하는 **'치트키(`itertools`)'**를 쓰는 것이고, 다른 하나는 **'백트래킹(재귀)'**을 이용해 직접 바닥부터 짜는 것이다. 두 가지 모두 자유자재로 쓸 줄 알아야 한다.

---

### 💡 1. 파이썬의 축복, `itertools` 사용하기 (가장 빠르고 쉬움)

코딩 테스트에서 단순히 모든 순열이나 조합을 구해서 확인만 하면 될 때는 무조건 내장 라이브러리인 `itertools`를 쓰는 게 정답이다. C언어로 구현되어 있어서 속도도 압도적으로 빠르다.

```python
from itertools import permutations, combinations

arr = ['A', 'B', 'C']

# 1. 순열 (Permutation): 3개 중에서 2개를 뽑아 일렬로 나열
print("--- 순열 (Permutations) ---")
for p in permutations(arr, 2):
    print(p)
# 결과: ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')

# 2. 조합 (Combination): 3개 중에서 순서 상관없이 2개를 뽑기
print("\n--- 조합 (Combinations) ---")
for c in combinations(arr, 2):
    print(c)
# 결과: ('A', 'B'), ('A', 'C'), ('B', 'C')

```

---

### 💡 2. 백트래킹(재귀)으로 직접 구현하기 (🔥매우 중요)

`itertools`가 아무리 좋아도, **"A를 뽑았으면 B는 절대 뽑지 마라"** 같은 복잡한 조건(가지치기)이 붙으면 `itertools`로는 해결할 수 없다. 이때는 직접 재귀 함수를 이용해 구현해야 한다.

상태를 저장하고, 탐색이 끝나면 다시 원상 복구(`pop`, `False`)시킨다는 **백트래킹**의 핵심 개념이 여기서 완벽하게 쓰인다.

#### 💻 순열 직접 구현하기 (`visited` 배열 사용)

순열은 순서가 중요하므로, 내가 이번 턴에 이 원소를 썼는지 안 썼는지 기록하는 `visited` 배열이 필요하다.

```python
arr = ['A', 'B', 'C']
n = len(arr)
r = 2 # 2개를 뽑음

visited = [False] * n # 방문 여부 체크
out = [] # 뽑은 원소들을 담을 스택(배열)

def dfs_perm(depth):
    # 기저 조건: r개를 모두 뽑았다면 출력하고 종료
    if depth == r:
        print(out)
        return
        
    for i in range(n):
        if not visited[i]:         # 아직 안 뽑은 원소라면
            visited[i] = True      # 1. 뽑았다고 표시
            out.append(arr[i])     # 2. 결과 배열에 넣음
            
            dfs_perm(depth + 1)    # 3. 다음 깊이로 이동 (재귀 호출)
            
            # 4. 탐색을 마치고 돌아왔다면 원상 복구 (Backtracking!)
            out.pop()              
            visited[i] = False     

print("--- 백트래킹 순열 ---")
dfs_perm(0)

```

#### 💻 조합 직접 구현하기 (`start` 인덱스 사용)

조합은 순서가 상관없기 때문에, 이미 뽑은 원소보다 **'뒤에 있는 원소들'**만 확인하면 된다. 그래서 `visited` 대신 시작점인 `start` 변수를 넘겨주는 방식으로 구현한다.

```python
arr = ['A', 'B', 'C']
n = len(arr)
r = 2 # 2개를 뽑음

out = [] # 뽑은 원소들을 담을 스택

def dfs_comb(depth, start):
    # 기저 조건: r개를 모두 뽑았다면 출력하고 종료
    if depth == r:
        print(out)
        return
        
    # start 인덱스부터 끝까지만 탐색 (이전 원소는 쳐다보지도 않음)
    for i in range(start, n):
        out.append(arr[i])         # 1. 일단 뽑아서 넣음
        
        dfs_comb(depth + 1, i + 1) # 2. '다음 인덱스(i+1)'부터 뽑으라고 넘겨줌 (재귀)
        
        # 3. 탐색을 마치고 돌아왔다면 원상 복구 (Backtracking!)
        out.pop()

print("--- 백트래킹 조합 ---")
dfs_comb(0, 0) # 깊이 0, 시작 인덱스 0부터 탐색 시작

```

---

### ⏱️ 시간 복잡도

* **순열:** $O(N!)$ (팩토리얼)
* **조합:** $O(2^N)$ 또는 $O(_{N}\mathrm{C}_{R})$

순열과 조합은 경우의 수가 기하급수적으로 폭발하기 때문에, 원소의 개수 $N$이 **10~15**를 넘어가면 시간 초과가 발생할 확률이 매우 높다. 문제에서 $N$이 매우 작게 주어졌다면 "완전 탐색(순열/조합) 문제"임을 의심해 봐야 한다.