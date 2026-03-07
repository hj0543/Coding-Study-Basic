최소 공통 조상(LCA, Lowest Common Ancestor) 알고리즘은 트리(Tree) 구조에서 임의의 두 노드가 주어졌을 때, 두 노드의 공통된 조상 중에서 가장 가까운(깊이가 가장 깊은) 조상 노드를 찾는 알고리즘이다.

트리 관련 문제에서 두 노드 사이의 최단 경로나 거리를 구할 때 핵심적으로 사용된다. 노드를 하나씩 거슬러 올라가는 기본 방식이 있지만, 코딩 테스트에서는 효율성을 위해 다이나믹 프로그래밍(DP)을 활용하여 탐색 속도를 비약적으로 끌어올린 **'빠른 LCA(Fast LCA)'** 방식이 주로 출제된다.

### 💡 알고리즘 동작 과정

1. 뎁스 파인딩(DFS/BFS)을 통해 모든 노드에 대한 깊이(Depth)와 첫 번째(바로 위) 부모 노드를 계산하여 저장한다.
2. 다이나믹 프로그래밍(DP)을 활용해 각 노드의 $2^i$번째 부모 노드 정보를 미리 계산하여 테이블(희소 배열, Sparse Table)에 저장한다.
3. 최소 공통 조상을 찾을 두 노드 $A, B$를 확인한다.
4. 두 노드의 깊이가 동일해지도록, 더 깊은 곳에 있는 노드를 2의 제곱수($2^i$)만큼씩 위로 점프시키며 부모 노드로 거슬러 올라가게 한다.
5. 깊이가 같아졌음에도 두 노드가 다르다면, 공통 조상을 만날 때까지 두 노드를 동시에 2의 제곱수만큼 위로 점프시킨다.
6. 두 노드의 바로 위 부모가 같아지는 지점을 찾으면, 그 부모 노드가 바로 최소 공통 조상이다.

> **참고:** 부모 테이블을 채우는 핵심 점화식은 다음과 같다.
> `parent[x][i] = parent[parent[x][i-1]][i-1]`
> 즉, $x$의 $2^i$번째 부모는 **'$x$의 $2^{i-1}$번째 부모의 $2^{i-1}$번째 부모'**라는 의미다. 이 점화식 덕분에 매번 1칸씩 올라갈 필요 없이 $1, 2, 4, 8, 16 \dots$ 칸씩 기하급수적으로 건너뛸 수 있다.

---

### 💻 빠른 최소 공통 조상(LCA) 기본 코드 (Python)

부모 노드를 $2^i$칸씩 건너뛰며 찾는 희소 배열(Sparse Table) 기반의 $O(\log N)$ 최적화 코드다.

```python
import sys
sys.setrecursionlimit(int(1e5))
LOG = 21 # 2^20 = 1,048,576이므로, 노드 개수가 10만 개 단위일 때 충분한 크기

# 노드의 개수 n
n = 15 
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
d = [0] * (n + 1)                          # 각 노드까지의 깊이
c = [False] * (n + 1)                      # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]         # 트리 정보 (간선)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 통과
            continue
        parent[y][0] = x # y의 1번째(2^0) 부모를 x로 설정
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수 (DP 테이블 채우기)
def set_parent():
    dfs(1, 0) # 1번 노드가 루트라고 가정
    for i in range(1, LOG):
        for j in range(1, n + 1):
            # j번 노드의 2^i번째 부모는, j번 노드의 2^(i-1)번째 부모의 2^(i-1)번째 부모
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# a와 b의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정 (통일성을 위해)
    if d[a] > d[b]:
        a, b = b, a
        
    # 1. 두 노드의 깊이(depth)를 동일하게 맞추기
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
            
    # 깊이를 맞췄는데 두 노드가 같다면, 그 노드가 바로 LCA
    if a == b:
        return a
        
    # 2. 부모가 같아지기 직전까지 동시에 위로 점프하기
    for i in range(LOG - 1, -1, -1):
        # 2^i번째 부모가 서로 다르다면 점프 진행
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            
    # 마지막엔 두 노드의 바로 윗 부모(2^0)가 공통 조상이 됨
    return parent[a][0]

```

### ⏱️ 시간 복잡도

빠른 LCA 알고리즘의 시간 복잡도는 다음과 같다.

* **전처리 (깊이 및 부모 테이블 기록):** **$O(N \log N)$** ($N$: 노드의 개수)
* **LCA 쿼리 (최소 공통 조상 찾기):** **$O(\log N)$** 총 $M$개의 쿼리(질의)가 주어질 때 전체 시간 복잡도는 **$O((N+M)\log N)$** 이 된다. 매 쿼리마다 노드를 하나씩 거슬러 올라가면 $O(NM)$이 걸려 시간 초과가 나지만, 2의 제곱수 형태로 건너뛰기 때문에 매우 큰 데이터에서도 순식간에 정답을 찾을 수 있다.

---

### 📝 예시 문제: LCA 2 (백준 11438번)

$N$개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 $N$번까지 번호가 매겨져 있으며, 루트는 1번이다. 두 노드의 쌍 $M$개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

* **입력:** 첫째 줄에 노드의 개수 $N$ ($2 \le N \le 100,000$)이 주어지고, 다음 $N-1$개 줄에 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고 싶은 쌍의 개수 $M$ ($1 \le M \le 100,000$)이 주어지고, 다음 $M$개 줄에 정점 쌍이 주어진다.
* **출력:** $M$개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

---

### 💡 풀이 접근법

노드의 개수 $N$과 질의 개수 $M$이 모두 최대 10만 개다. 만약 $O(N)$이 소요되는 기본 LCA 알고리즘을 사용한다면 최악의 경우 100억 번의 연산이 필요하므로 무조건 시간 초과(TLE)가 발생한다. 따라서 반드시 **희소 배열(DP)을 활용한 $O(\log N)$ 최적화 LCA 알고리즘**을 사용해야 한다.

* **노드(Node)와 간선(Edge):** 주어지는 간선은 방향성이 없으므로 양방향으로 그래프를 구성한 뒤, 1번 노드부터 DFS를 돌려 부모-자식 관계와 깊이를 명확히 정립한다.
* 이후 `set_parent()` 함수로 DP 테이블을 완성하고, 주어지는 $M$개의 쿼리에 대해 `lca(a, b)`를 수행하면 된다.

---

### 💻 풀이 코드 (Python)

```python
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
LOG = 21 

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]
d = [0] * (n + 1)
c = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

# 양방향 그래프 연결 정보 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a
    
    # 1. 깊이 맞추기
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
            
    if a == b:
        return a
        
    # 2. 공통 조상 찾기
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            
    return parent[a][0]

# DP 테이블 초기화
set_parent()

m = int(input())
# M개의 쿼리 처리
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

```