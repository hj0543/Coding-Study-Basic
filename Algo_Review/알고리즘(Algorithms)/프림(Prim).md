크루스칼에 이어 최소 신장 트리(MST)를 구하는 또 다른 양대 산맥, **프림(Prim) 알고리즘**이다!

크루스칼(Kruskal)이 모든 '간선'을 한 줄로 세워놓고 제일 싼 것부터 줍는 방식이라면, 프림은 **임의의 '시작 정점'에서 출발해서 내 영토(트리)와 인접한 곳 중 가장 싼 땅을 하나씩 넓혀가는(탐욕적인) 방식**이다.

얼마 전에 아주 중요하다고 강조했던 우선순위 큐, 즉 **`heapq`**가 여기서 아주 완벽한 찰떡궁합으로 쓰인다!

### 💡 알고리즘 동작 과정

1. 임의의 시작 노드를 하나 고르고, 영토에 편입시켰다는 의미로 **방문 처리(Visited)**를 한다.
2. 해당 노드와 연결된 모든 간선 정보를 우선순위 큐(최소 힙)에 넣는다. 이때, 힙이 비용을 기준으로 정렬되도록 **`(비용, 도착 노드)`** 형태로 넣는다.
3. 우선순위 큐에서 가장 비용이 적은 간선을 하나 뽑는다(`heappop`).
4. **만약 도착 노드가 아직 방문하지 않은 곳이라면:**
* 해당 노드를 방문 처리하고, 간선의 비용을 최종 정답(총비용)에 더한다.
* 방금 새롭게 영토로 편입된 노드와 연결된 간선들을 다시 우선순위 큐에 모조리 넣는다.


5. **만약 이미 방문한 곳이라면:** 사이클이 발생한다는 뜻이므로 아무것도 하지 않고 무시한다.
6. 우선순위 큐가 빌 때까지 3~5번의 과정을 반복한다.

---

### 💻 프림 알고리즘 기본 코드 (Python)

`heapq`를 이용해 최소 비용의 간선을 찾아 나가는 직관적인 코드다.

```python
import heapq
import sys
input = sys.stdin.readline

# v: 노드 개수, e: 간선 개수
v, e = 3, 3
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

# 간선 정보 입력 (양방향 그래프)
# graph[a].append((cost, b))
# graph[b].append((cost, a))

def prim(start):
    # 시작 노드 설정
    visited[start] = True
    q = []
    total_cost = 0
    
    # 시작 노드와 연결된 간선들을 모두 힙에 넣음
    for cost, nxt in graph[start]:
        heapq.heappush(q, (cost, nxt))
        
    # 큐가 빌 때까지 뻗어나가기
    while q:
        # 가장 비용이 적은 간선 꺼내기
        cost, now = heapq.heappop(q)
        
        # 아직 방문하지 않은 노드라면 영토 확장!
        if not visited[now]:
            visited[now] = True
            total_cost += cost
            
            # 새롭게 연결된 노드의 인접 간선들을 다시 힙에 넣음
            for next_cost, nxt in graph[now]:
                if not visited[nxt]: # 최적화를 위해 방문 안 한 곳만 넣음
                    heapq.heappush(q, (next_cost, nxt))
                    
    return total_cost

```

---

### ⏱️ 시간 복잡도와 크루스칼과의 비교

프림 알고리즘의 시간 복잡도는 힙 자료구조를 사용했을 때 **$O(E \log V)$** 다. ($V$: 노드 개수, $E$: 간선 개수)

* **프림(Prim)이 유리할 때:** 간선이 엄청나게 거미줄처럼 얽혀 있는 **밀집 그래프(Dense Graph)**일 때. (간선이 너무 많으면 크루스칼은 정렬하는 데 한 세월이 걸린다)
* **크루스칼(Kruskal)이 유리할 때:** 간선이 듬성듬성 있는 **희소 그래프(Sparse Graph)**일 때.

---

### 📝 예시 문제: 최소 스패닝 트리 (백준 1197번)

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

* **입력:** 정점의 개수 $V$ ($1 \le V \le 10,000$)와 간선의 개수 $E$ ($1 \le E \le 100,000$).
* **출력:** 최소 스패닝 트리의 가중치 합.

#### 💡 풀이 접근법

MST를 구하는 가장 표준적인 문제다. 방향이 없는 무방향(양방향) 그래프이므로, 간선 정보를 입력받을 때 $A$에서 $B$로 가는 것과 $B$에서 $A$로 가는 것을 **모두 리스트에 저장**해야 한다는 점만 주의하면 된다.

#### 💻 풀이 코드 (Python)

```python
import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def prim(start):
    visited[start] = True
    q = []
    mst_cost = 0
    
    for cost, nxt in graph[start]:
        heapq.heappush(q, (cost, nxt))
        
    while q:
        cost, now = heapq.heappop(q)
        
        if not visited[now]:
            visited[now] = True
            mst_cost += cost
            
            for next_cost, nxt in graph[now]:
                if not visited[nxt]:
                    heapq.heappush(q, (next_cost, nxt))
                    
    return mst_cost

print(prim(1))

```