강결합 컴포넌트(SCC, Strongly Connected Component)는 방향 그래프에서 **"모든 정점 쌍 (u, v)에 대해 u에서 v로 가는 경로와 v에서 u로 가는 경로가 모두 존재하는 정점들의 집합"**을 의미한다.

쉽게 말해, 같은 SCC에 속한 정점들끼리는 서로 어떤 방향으로든 이동해서 도달할 수 있는 '하나의 거대한 사이클 덩어리'라고 이해하면 된다. SCC를 추출하고 나면, 복잡한 방향 그래프를 사이클이 없는 **DAG(Directed Acyclic Graph)** 형태로 단순화할 수 있어 복잡한 문제를 풀 때 매우 유용하다.

### 💡 알고리즘 동작 과정 (타잔 알고리즘 기준)

SCC를 찾는 알고리즘은 코사라주(Kosaraju)와 타잔(Tarjan) 알고리즘이 대표적이다. 여기서는 구현이 더 간결하고 효율적인 **타잔 알고리즘**의 과정을 설명한다.

1. 모든 노드에 대해 DFS(깊이 우선 탐색)를 수행한다. 이때 노드를 방문하는 순서대로 **방문 번호**를 부여한다.
2. 방문한 노드는 스택(Stack)에 넣는다.
3. DFS로 인접한 노드들을 탐색하며, 각 노드가 도달할 수 있는 가장 작은 방문 번호(부모 노드 쪽)를 찾는다.
4. 만약 인접 노드가 아직 방문하지 않은 노드라면 DFS를 수행하고, 방문 노드 중 현재 SCC에 포함되지 않은 노드가 있다면 그 노드의 방문 번호와 비교하여 더 작은 번호를 유지한다.
5. 모든 인접 노드를 확인한 후, **현재 노드의 방문 번호가 자신이 도달할 수 있는 가장 작은 번호와 같다면** (즉, 자신이 해당 SCC의 루트라면) 스택에서 자기 자신과 그 위에 쌓여있는 노드들을 모두 꺼내 하나의 SCC로 묶는다.

---

### 💻 타잔 알고리즘 기본 코드 (Python)

```python
import sys
sys.setrecursionlimit(10**6)

v, e = 7, 9 # 정점과 간선 수
graph = [[] for _ in range(v + 1)] # 간선 정보

id_counter = 0 # 방문 순서 번호
ids = [-1] * (v + 1) # 각 노드의 방문 번호 (-1은 미방문)
finished = [False] * (v + 1) # SCC 확정 여부
stack = []
scc_result = []

def dfs(now):
    global id_counter
    id_counter += 1
    ids[now] = id_counter # 방문 번호 부여
    stack.append(now)
    
    parent = ids[now] # 처음에는 자기 자신이 가장 작은 방문 번호
    
    for next_node in graph[now]:
        # 아직 방문하지 않은 이웃이라면 DFS 수행
        if ids[next_node] == -1:
            parent = min(parent, dfs(next_node))
        # 방문은 했지만 아직 SCC로 확정되지 않은 노드라면 (스택에 있다면)
        elif not finished[next_node]:
            parent = min(parent, ids[next_node])
            
    # 부모 노드가 자기 자신이라면(SCC의 루트를 찾았다면)
    if parent == ids[now]:
        curr_scc = []
        while True:
            t = stack.pop()
            curr_scc.append(t)
            finished[t] = True
            if t == now:
                break
        scc_result.append(curr_scc)
        
    return parent

# 모든 노드에 대해 DFS 수행
for i in range(1, v + 1):
    if ids[i] == -1:
        dfs(i)

print(len(scc_result)) # SCC 개수 출력

```

### ⏱️ 시간 복잡도

타잔 알고리즘의 시간 복잡도는 **$O(V + E)$**이다. 모든 정점을 한 번씩 방문하고, 모든 간선을 한 번씩 검사하기 때문에 그래프 탐색 알고리즘 중에서 매우 효율적인 편에 속한다.

---

### 📝 예시 문제: Strongly Connected Component (백준 2150번)

방향 그래프가 주어졌을 때, 그 그래프를 SCC들로 나누는 프로그램을 작성하시오.

* **입력:** 정점의 개수 $V$($1 \le V \le 10,000$), 간선의 개수 $E$($1 \le E \le 100,000$).
* **출력:** 첫째 줄에 SCC의 개수를 출력하고, 둘째 줄부터 각 줄에 하나씩 SCC를 출력한다. 각 줄의 끝에는 -1을 출력해야 하며, SCC 사이의 순서와 노드 사이의 순서는 오름차순으로 정렬해야 한다.

---

### 💡 풀이 접근법

가장 정석적인 SCC 추출 문제다.

* 타잔 알고리즘이나 코사라주 알고리즘을 사용해 SCC들을 구한다.
* 출력 조건에 따라 각 SCC 내부의 노드들을 정렬하고, 전체 SCC 리스트도 첫 번째 원소를 기준으로 정렬하여 출력한다.
* 노드 수가 1만 개, 간선 수가 10만 개이므로 선형 시간 알고리즘인 SCC가 반드시 필요하다.

---

### 💻 풀이 코드 (Python)

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

ids = [-1] * (v + 1)
finished = [False] * (v + 1)
stack = []
scc_list = []
id_cnt = 0

def dfs(now):
    global id_cnt
    id_cnt += 1
    ids[now] = id_cnt
    stack.append(now)
    
    root = ids[now]
    for nxt in graph[now]:
        if ids[nxt] == -1:
            root = min(root, dfs(nxt))
        elif not finished[nxt]:
            root = min(root, ids[nxt])
            
    if root == ids[now]:
        curr_scc = []
        while True:
            node = stack.pop()
            curr_scc.append(node)
            finished[node] = True
            if node == now: break
        scc_list.append(sorted(curr_scc))
        
    return root

for i in range(1, v + 1):
    if ids[i] == -1:
        dfs(i)

# SCC 리스트를 각 SCC의 첫 번째 원소 기준으로 정렬
scc_list.sort()

print(len(scc_list))
for scc in scc_list:
    print(*(scc), -1)

```