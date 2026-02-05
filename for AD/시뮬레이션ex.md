이 문제들은 삼성 A형 대비를 위해 **선택이 아닌 필수**로 풀어봐야 하는 문제들이다.

---

# 1. 로봇 청소기 유형

가장 정석적인 시뮬레이션 문제다. 앞서 정리한 **"회전 + 후진"** 로직을 그대로 사용한다.

### 🎯 [Gold 5] 로봇 청소기 (14503번)

* **링크**: [https://www.acmicpc.net/problem/14503](https://www.acmicpc.net/problem/14503)
* **특징**:
* 조건이 매우 구체적이다. (청소한다  회전한다  전진/후진한다)
* **방향 정의**: 0:북, 1:동, 2:남, 3:서 (시계 방향)
* **왼쪽 회전**: `(d - 1) % 4` (파이썬은 음수 모듈러 연산이 자동으로 처리되어 `(0-1)%4 = 3`이 된다.)



**💡 풀이 Tip**

```python
# 후진 로직 필수!
# 방향 d를 바꾸지 않고 뒤로 가는 좌표 계산
back_r = r - dr[d]
back_c = c - dc[d]

if grid[back_r][back_c] == 1: # 뒤가 벽이면
    break # 종료

```

---

# 2. 중력 (Gravity) 유형

블록이 터지고(`BFS`)  빈 공간으로 떨어진다(`중력`)는 패턴이다.

### 🎯 [Gold 4] Puyo Puyo (11559번)

* **링크**: [https://www.acmicpc.net/problem/11559](https://www.acmicpc.net/problem/11559)
* **특징**:
* 같은 색 4개가 상하좌우 연결되면 터진다 (**BFS**).
* 터진 공간(`.`)이 생기면 위에 있는 블록들이 바닥으로 떨어진다 (**중력**).
* 연쇄가 몇 번 일어나는지 카운트한다.



**💡 풀이 Tip (중력 함수)**
이 함수는 그냥 외워두는 것이 좋다.

```python
def apply_gravity():
    for j in range(6): # 열(Col) 단위로 처리
        temp = []
        for i in range(12):
            if field[i][j] != '.':
                temp.append(field[i][j]) # 블록만 추출
        
        # 다시 채우기 (위쪽은 ., 아래쪽은 블록)
        for i in range(12 - len(temp)):
            field[i][j] = '.'
        for k in range(len(temp)):
            field[12 - len(temp) + k][j] = temp[k]

```

---

# 3. 달팽이 (Tornado) 유형

달팽이 배열 로직의 **기초**와 **심화(A형 기출)** 문제다.

### ① 기초: [Silver 3] 달팽이 (1913번)

* **링크**: [https://www.acmicpc.net/problem/1913](https://www.acmicpc.net/problem/1913)
* **특징**:
* `N x N` 배열의 중앙에서 시작하여 `1, 2, 3...` 순서로 밖으로 나간다.
* **이동 거리 규칙**: `1, 1, 2, 2, 3, 3...` (방향 2번 바꿀 때마다 거리 +1)
* 이 문제로 기본 `while`문 로직을 먼저 연습해야 한다.



### ② 심화(A형 기출): [Gold 3] 마법사 상어와 토네이도 (20057번)

* **링크**: [https://www.acmicpc.net/problem/20057](https://www.acmicpc.net/problem/20057)
* **특징**:
* **달팽이 이동 로직**은 1913번과 **100% 동일**하다.
* 차이점은 이동할 때마다 모래가 흩날리는 **델타 탐색(비율 계산)**이 추가된 것이다.
* 즉, **[달팽이 이동] + [시뮬레이션]** 융합 문제다.



**💡 풀이 Tip (이동 로직)**

```python
# 중앙 시작
r, c = N//2, N//2
move_len = 1
d_idx = 0

while r != 0 or c != 0: # (0,0)에 도착할 때까지
    for _ in range(2): # 같은 길이로 2번 방향 전환
        for _ in range(move_len):
            # 1. 한 칸 이동
            r += dr[d_idx]
            c += dc[d_idx]
            
            # 2. 여기서 모래 흩날리는 로직(함수) 수행
            spread_sand(r, c, d_idx)
            
            if r == 0 and c == 0: return # 종료 조건
            
        d_idx = (d_idx + 1) % 4 # 방향 변경
        
    move_len += 1 # 이동 거리 증가

```

---

### ✅ 추천 공부 순서

1. **[1913 달팽이]**로 `while`문 2번 돌려서 거리 늘리는 감각을 익힌다.
2. **[14503 로봇 청소기]**로 회전과 후진을 구현해본다.
3. **[11559 Puyo Puyo]**는 BFS를 공부한 직후에 **중력** 파트 구현용으로 푼다.
4. **[20057 토네이도]**는 A형 시험 직전에 최종 점검용으로 푼다.