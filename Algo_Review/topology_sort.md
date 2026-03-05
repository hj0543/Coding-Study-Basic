위상 정렬을 구현할 때는 주로 **진입차수(In-degree)**와 **큐(Queue)**를 활용하는 Kahn's Algorithm을 사용한다.

### 💡 알고리즘 동작 과정

1. 진입차수(특정한 노드로 들어오는 간선의 개수)가 0인 노드를 큐에 넣는다.
2. 큐에서 노드를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다. (연결된 노드의 진입차수를 1씩 뺀다.)
3. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
4. 큐가 빌 때까지 2번과 3번의 과정을 반복한다.

> **참고:** 모든 노드를 방문하기 전에 큐가 빈다면 그래프 내에 사이클(Cycle)이 존재하는 것이다. 사이클이 포함된 그래프는 위상 정렬을 수행할 수 없다.

---

### 💻 위상 정렬 기본 코드 (Python)

가장 직관적이고 많이 쓰이는 파이썬(Python) 기반의 기본 코드다.

```python
from collections import deque

# 노드의 개수(v)와 간선의 개수(e) 설정
v, e = 7, 8

# 모든 노드에 대한 진입차수는 0으로 초기화 (1번 노드부터 사용하기 위해 v+1)
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 인접 리스트 초기화
graph = [[] for _ in range(v + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)    # 정점 A에서 B로 이동 가능
    indegree[e] += 1      # 도착점 B의 진입차수를 1 증가

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 1. 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # 2. 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 3. 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 사이클 발생 여부 확인 (결과 리스트의 길이가 전체 노드 개수와 다르면 사이클 존재)
    print(*result)

topology_sort()

```

### ⏱️ 시간 복잡도

위상 정렬의 시간 복잡도는 **O(V + E)** 입니다. (V: 노드의 개수, E: 간선의 개수)
차례대로 모든 노드를 확인하면서 각 노드에서 뻗어 나가는 간선을 차례대로 제거하기 때문에, 그래프의 모든 노드와 간선을 딱 한 번씩만 확인하게 되어 매우 빠른 속도를 자랑한다.

---

### 📝 예시 문제: 줄 세우기 (백준 2252번)

N명의 학생들을 키 순서대로 줄을 세우려고 합니다. 하지만 모든 학생의 키를 한 번에 측정한 것이 아니라, 일부 학생들의 키를 두 명씩 비교한 결과만 주어집니다. 이 결과를 바탕으로 학생들을 줄 세우는 프로그램을 작성해야 합니다.

* **입력:** 첫째 줄에 N(학생 수, $1 \le N \le 32,000$), M(키를 비교한 횟수, $1 \le M \le 100,000$)이 주어집니다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어집니다. 이는 **학생 A가 학생 B보다 앞에 서야 한다는 의미**입니다.
* **출력:** 학생들을 앞에서부터 줄을 세운 결과를 출력합니다. (답이 여러 가지인 경우에는 아무거나 출력해도 됩니다.)

---

### 💡 풀이 접근법

이 문제는 **'순서가 정해진 작업'**을 나열하는 것이므로 위상 정렬을 사용하기에 완벽한 조건입니다.

* **노드(Node):** 각 학생
* **방향 간선(Edge):** 키 비교 결과 (A가 B보다 앞에 서야 한다면 `A -> B`로 간선을 연결)
* **진입차수(In-degree):** 자신보다 앞에 서야 하는 학생의 수

진입차수가 0인 학생(자신보다 앞에 서야 할 사람이 아무도 없는 학생)부터 차례대로 줄을 세우면 됩니다.

---

### 💻 풀이 코드 (Python)

```python
import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print(*result)

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1    # 이걸 빼먹음;;

topology_sort()

```

일반 큐(Queue) 대신 **우선순위 큐(Priority Queue, heapq)**를 사용하는 응용 문제(예: 백준 1766번 '문제집')에 대한 풀이법도 연달아 설명해 드릴까요?
