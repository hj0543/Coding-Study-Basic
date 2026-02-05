이 두 알고리즘은 **삼성 A형 및 코딩 테스트의 꽃**이다. 그래프 탐색을 모르면 A형 문제는 손도 못 댄다고 보면 된다.

---

# 📝 DFS & BFS (그래프 탐색)

그래프(정점과 간선으로 연결된 구조)의 모든 정점을 **빠짐없이 방문**하는 두 가지 방법이다.

## 1. DFS (Depth-First Search, 깊이 우선 탐색)

**"한 우물만 끝까지 판다."**

* **개념**: 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 **해당 분기를 완벽하게 탐색**하는 방식이다.
* **자료구조**: **스택(Stack)** 또는 **재귀(Recursion)**를 사용한다.
* **특징**: 코드가 직관적이고 구현이 쉽다. (단, 재귀 깊이가 너무 깊어지면 에러가 날 수 있다.)
* **활용**: 미로 찾기, 경로의 존재 여부, 백트래킹(가능한 모든 경우의 수 따지기).

## 2. BFS (Breadth-First Search, 너비 우선 탐색)

**"주변부터 차근차근 넓혀간다."**

* **개념**: 루트 노드에서 시작해서 **인접한 노드를 먼저 모두 탐색**한 후, 다음 깊이로 넘어가는 방식이다.
* **자료구조**: **큐(Queue)**를 사용한다. (Python에서는 `collections.deque` 필수)
* **특징**: 시작점에서 끝점까지의 **최단 거리(최소 이동 횟수)**를 보장한다.
* **활용**: 최단 경로 찾기, 바이러스 퍼뜨리기, 영역 넓이 구하기.

---

# 3. 실전 구현 패턴 (암기 필수)

### ① DFS (재귀 구현)

```python
# visited: 방문 여부 기록 리스트
# graph: 인접 리스트 (연결 정보)
def dfs(v):
    visited[v] = True
    print(v, end=' ') # 방문 처리
    
    # 현재 노드(v)와 연결된 노드(i)들을 확인
    for i in graph[v]:
        if not visited[i]: # 방문하지 않았다면
            dfs(i) # 더 깊이 들어감 (재귀)

```

### ② BFS (큐 구현)

```python
from collections import deque

def bfs(start):
    queue = deque([start]) # 큐 생성 및 시작점 삽입
    visited[start] = True  # 시작점 방문 처리
    
    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐에서 하나 꺼냄
        print(v, end=' ')
        
        # 꺼낸 노드와 연결된 노드 확인
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # 큐에 삽입
                visited[i] = True # 미리 방문 처리 (중복 방지)

```

---

# 4. 필수 백준 문제 & 풀이

가장 기본이 되는 두 문제를 선정했다. 이 두 코드는 안 보고 짤 수 있을 정도로 외워야 한다.

## ① 기본기 점검: [Silver 2] DFS와 BFS (1260번)

두 탐색 방식의 순서 차이를 명확히 이해하는 문제다.

* **링크**: [https://www.acmicpc.net/problem/1260](https://www.acmicpc.net/problem/1260)
* **핵심**:
* 정점 번호가 작은 것을 먼저 방문해야 하므로 **정렬(Sort)**이 필요하다.
* DFS와 BFS 함수를 각각 구현해서 결과를 출력한다.



### 💻 풀이 코드

```python
import sys
from collections import deque
input = sys.stdin.readline

# 정점(N), 간선(M), 시작점(V)
N, M, V = map(int, input().split())

# 인접 리스트 생성 (정점 번호가 1부터 시작하므로 N+1 크기)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 연결

# 작은 번호부터 방문하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS 구현
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# BFS 구현
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 실행
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print() # 줄바꿈
bfs(V)

```

---

## ② A형 필수 유형: [Silver 1] 미로 탐색 (2178번)

**"2차원 배열 + 최단 거리"**는 무조건 **BFS**다. DFS로 풀면 최단 거리를 보장하기 어렵고 시간 초과가 날 수 있다.

* **링크**: [https://www.acmicpc.net/problem/2178](https://www.acmicpc.net/problem/2178)
* **핵심**:
* 델타 탐색(상하좌우)을 BFS 안에서 수행한다.
* **방문한 칸에 값을 1씩 더해가며 이동 거리(Depth)를 기록**하는 테크닉이 중요하다.



### 💻 풀이 코드

```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# 미로 정보 입력 (문자열 붙어서 들어오므로 strip 처리)
maze = [list(map(int, input().strip())) for _ in range(N)]

# 델타 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크
            if 0 <= nx < N and 0 <= ny < M:
                # 벽(0)이면 무시
                if maze[nx][ny] == 0:
                    continue
                
                # 길(1)인 경우에만 이동 (처음 방문하는 곳만)
                if maze[nx][ny] == 1:
                    # 이전 위치 값 + 1을 저장하여 거리 기록
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
    
    # 도착점(N-1, M-1)의 값 반환
    return maze[N-1][M-1]

print(bfs(0, 0))

```

---

### ✅ 다음 학습 가이드

이제 그래프 탐색의 기초를 마쳤다. 다음 단계는 **DFS의 심화 버전인 [백트래킹(Backtracking)]**이다.
백트래킹은 A형 문제에서 **"경우의 수 찾기"**나 **"최적화 문제"**를 해결하는 핵심 열쇠다. (예: N-Queen, 연산자 끼워넣기 등)