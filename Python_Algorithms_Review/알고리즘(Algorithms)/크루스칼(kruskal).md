
크루스칼 알고리즘은 그래프 내의 모든 노드를 가장 적은 비용으로 연결하는 **최소 신장 트리(MST, Minimum Spanning Tree)**를 찾기 위한 대표적인 그리디(Greedy) 알고리즘이다. 이를 구현할 때는 사이클 발생 여부를 판별하기 위해 주로 **서로소 집합(Disjoint Set, Union-Find)** 자료구조를 활용한다.

### 💡 알고리즘 동작 과정

1. 모든 간선 데이터를 비용(가중치)을 기준으로 **오름차순 정렬**한다.
2. 정렬된 간선을 하나씩 확인하며, 현재의 간선이 노드들 간에 **사이클(Cycle)을 발생시키는지 확인**한다. (Find 연산)
3. 사이클이 발생하지 않는 경우에만 최소 신장 트리에 포함시킨다. (Union 연산)
4. 사이클이 발생하는 경우에는 포함시키지 않고 다음 간선으로 넘어간다.
5. 모든 간선에 대해 2~4번의 과정을 반복한다.

> **참고:** 트리의 성질에 따라, 완성된 최소 신장 트리에 포함되는 간선의 개수는 항상 **노드의 개수 - 1**개가 됩니다. 만약 이 개수를 채웠다면 반복문을 미리 종료하여 최적화할 수도 있습니다.

---

### 💻 크루스칼 알고리즘 기본 코드 (Python)

서로소 집합(Union-Find) 함수와 함께 사용되는 크루스칼 알고리즘의 뼈대 코드다.

```python
# 특정 원소가 속한 집합을 찾기 (Find)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 (경로 압축)
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 번호의 노드가 부모가 되도록 설정 (관례적)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 7, 9 # 노드의 개수(v)와 간선의 개수(e)
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용을 담을 변수

# 간선 정보 입력받기 (예시 생략, a번 노드와 b번 노드를 연결하는 비용이 cost라고 가정)
# edges.append((cost, a, b))

# 1. 간선을 비용 순으로 오름차순 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 2. 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b) # 3. 두 노드를 연결 (같은 집합으로 합치기)
        result += cost             # 총비용에 추가

print(result)

```

### ⏱️ 시간 복잡도

* 크루스칼 알고리즘의 시간 복잡도는 **$O(E \log E)$** 다. ($E$: 간선의 개수)
* 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 작업은 간선들을 가중치 기준으로 정렬하는 작업이다.
* 파이썬의 내장 정렬 함수를 사용하면 $O(E \log E)$의 시간 복잡도로 정렬이 가능하며, 서로소 집합(Union-Find) 알고리즘의 시간 복잡도는 정렬 알고리즘보다 작으므로 전체 시간 복잡도에 큰 영향을 주지 않는다.

---

### 📝 예시 문제: 최소 스패닝 트리 (백준 1197번)

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리(MST)를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말합니다.

* **입력:** 첫째 줄에 정점의 개수 $V$ ($1 \le V \le 10,000$)와 간선의 개수 $E$ ($1 \le E \le 100,000$)가 주어집니다. 다음 $E$개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 $A, B, C$가 주어집니다. 이는 $A$번 정점과 $B$번 정점이 가중치 $C$인 간선으로 연결되어 있다는 의미입니다.
* **출력:** 첫째 줄에 최소 스패닝 트리의 가중치를 출력합니다.

---

### 💡 풀이 접근법

문제 이름부터 대놓고 '최소 스패닝 트리'를 요구하고 있으며, 노드와 간선 정보가 주어지므로 **크루스칼 알고리즘**을 그대로 적용하면 풀리는 기본 문제입니다.

* **노드(Node)와 간선(Edge):** 주어지는 $V$와 $E$
* **정렬 기준:** 간선의 가중치 $C$
* 모든 간선을 리스트에 담아 가중치를 기준으로 정렬한 뒤, 사이클이 발생하지 않는 간선들만 골라 가중치를 누적합하면 됩니다.

---

### 💻 풀이 코드 (Python)

```python
import sys
input = sys.stdin.readline

# Find 연산 (경로 압축 기법 적용)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 정점의 개수 V와 간선의 개수 E 입력받기
v, e = map(int, input().split())

parent = [0] * (v + 1) # 부모 테이블
edges = []             # 간선 정보를 담을 리스트
total_cost = 0         # 최소 스패닝 트리의 가중치 합

# 부모 테이블을 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선 정보 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())
    # 비용(c)을 기준으로 정렬하기 위해 튜플의 첫 번째 원소를 c로 설정
    edges.append((c, a, b))

# 1. 간선을 비용 기준으로 오름차순 정렬
edges.sort()

# 크루스칼 알고리즘 수행
for edge in edges:
    cost, a, b = edge
    
    # 2. 사이클이 발생하지 않는 경우(루트 노드가 서로 다른 경우)에만 처리
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b) # 3. 트리에 포함 (집합 합치기)
        total_cost += cost         # 가중치 누적

# 결과 출력
print(total_cost)

```