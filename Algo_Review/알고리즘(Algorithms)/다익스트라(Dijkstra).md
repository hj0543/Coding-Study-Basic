다익스트라(Dijkstra) 알고리즘은 특정한 하나의 노드에서 출발하여 그래프 내의 다른 모든 노드로 가는 최단 경로를 구하는 알고리즘이다. 그래프에 음의 가중치를 가진 간선(Negative Edge)이 없을 때만 정상적으로 동작하며, 매 상황에서 가장 비용이 적은 노드를 선택한다는 점에서 그리디(Greedy) 알고리즘으로 분류된다. 현재는 최적화를 위해 주로 **우선순위 큐(Priority Queue)**를 활용하여 구현한다.

### 💡 알고리즘 동작 과정

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 모두 무한대(Infinity)로 초기화하고, 출발 노드 자신에 대한 최단 거리는 0으로 설정하여 우선순위 큐에 넣는다.
3. 우선순위 큐에서 거리가 가장 짧은 노드를 꺼낸다.
4. 해당 노드를 거쳐서 연결된 다른 노드로 가는 비용을 계산한다.
5. 계산된 비용이 최단 거리 테이블에 기록된 기존 비용보다 짧다면, 최단 거리 테이블을 갱신하고 우선순위 큐에 넣는다.
6. 우선순위 큐가 빌 때까지 3~5번의 과정을 반복한다.

> **참고:** 한 번 큐에서 꺼내져 처리가 완료된 노드는 최단 거리가 확정된 것이므로 더 이상 거리가 줄어들지 않는다. 즉, 다익스트라 알고리즘은 각 노드에 대한 최단 거리를 한 번씩만 확정한다.

---

### 💻 다익스트라 알고리즘 기본 코드 (Python)

파이썬의 내장 모듈인 `heapq`를 사용하여 최소 힙(Min Heap) 기반의 우선순위 큐를 구현한 표준 코드다.

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

v, e = 6, 11 # 노드의 개수(v)와 간선의 개수(e)
start = 1    # 시작 노드 번호

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(v + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v + 1)

# 모든 간선 정보 입력받기 (예시 생략)
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c)) # a번 노드에서 b번 노드로 가는 비용이 c

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
            
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

```

### ⏱️ 시간 복잡도

우선순위 큐를 활용한 다익스트라 알고리즘의 시간 복잡도는 **$O(E \log V)$** 이다. ($V$: 노드의 개수, $E$: 간선의 개수)
모든 간선은 최대 한 번씩 확인되며, 힙(Heap)에 간선 정보를 넣고 빼는 과정에서 $O(\log V)$의 시간이 소요되기 때문에 노드와 간선의 개수가 많아도 매우 빠르게 동작한다.

---

### 📝 예시 문제: 최단경로 (백준 1753번)

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. (단, 모든 간선의 가중치는 10 이하의 자연수이다.)

* **입력:** 첫째 줄에 정점의 개수 $V$ ($1 \le V \le 20,000$)와 간선의 개수 $E$ ($1 \le E \le 300,000$)가 주어진다. 둘째 줄에는 시작 정점의 번호 $K$가 주어진다. 셋째 줄부터 $E$개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 $(u, v, w)$가 순서대로 주어진다. 이는 $u$에서 $v$로 가는 가중치 $w$인 간선이 존재한다는 뜻이다.
* **출력:** 첫째 줄부터 $V$개의 줄에 걸쳐, $i$번째 줄에 시작점에서 $i$번 정점까지의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 `INF`를 출력한다.

---

### 💡 풀이 접근법

시작점이 정해져 있고 음의 가중치가 없으며, 정점과 간선의 개수가 충분히 크기 때문에 **우선순위 큐를 활용한 다익스트라 알고리즘**을 사용해야 시간 초과 없이 해결할 수 있는 가장 전형적인 문제다.

* **노드(Node):** 정점 $V$
* **방향 간선(Edge):** $u \rightarrow v$ (비용 $w$)
* 시작 정점 $K$를 큐에 넣고 다익스트라를 돌린 뒤, 완성된 `distance` 테이블의 값을 차례대로 출력하면 된다.

---

### 💻 풀이 코드 (Python)

```python
import sys
import heapq

# 입력 속도 최적화
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

# 방향 그래프 간선 정보 입력
for _ in range(e):
    u, dest, w = map(int, input().split())
    graph[u].append((dest, w)) # u에서 dest로 가는 가중치 w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리된 적 있는 노드라면 무시 (기록된 최단거리보다 현재 큐에서 뽑은 거리가 크면 의미 없음)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            next_node = i[0]
            weight = i[1]
            cost = dist + weight

            # 거쳐가는 것이 더 저렴한 경우 최단거리 테이블 갱신 및 큐에 삽입
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(start)

# 결과 출력
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

```

---

다익스트라 알고리즘은 매우 빠르고 유용하지만, 앞서 언급했듯 '음의 간선'이 존재할 때는 사용할 수 없다. 만약 음수 가중치가 포함된 그래프에서 최단 경로를 구하거나 음수 사이클의 존재 여부를 판별해야 한다면 **'벨만-포드(Bellman-Ford) 알고리즘'**을 사용해야 하는데, 이 알고리즘에 대해서도 동일한 형식으로 정리해 줄까?