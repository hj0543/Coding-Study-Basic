재귀 함수는 **DFS(깊이 우선 탐색)**와 **백트래킹**의 기초가 되는 매우 중요한 개념이다. "자신을 다시 호출한다"는 특성 때문에 처음엔 어렵게 느껴질 수 있지만, **종료 조건(Base Case)**과 **패턴(Recursive Case)**만 확실히 잡으면 코드가 매우 간결해진다.

---

# 1. 재귀 함수 핵심 개념

**"함수 안에서 자기 자신을 다시 부르는 함수"**

반드시 두 가지 부분이 있어야 한다.

1. **종료 조건 (Base Case)**: 더 이상 재귀를 부르지 않고 끝나는 조건. (없으면 무한 루프에 빠져 에러 발생)
2. **재귀 호출 (Recursive Case)**: 문제를 더 작은 단위로 쪼개서 자신을 호출하는 부분.

### ⚡ 기본 형태 (암기)

```python
def recursion(n):
    # 1. 종료 조건
    if n == 0:
        return
    
    # 2. 로직 수행
    print(n)
    
    # 3. 재귀 호출 (문제를 줄여서 호출)
    recursion(n - 1)

```

---

# 2. 기초 연습: [Bronze 5] 팩토리얼 (10872번)

재귀의 가장 기초적인 예제다.  이라는 점화식을 그대로 코드로 옮기면 된다.

* **링크**: [https://www.acmicpc.net/problem/10872](https://www.acmicpc.net/problem/10872)
* **점화식**: `f(n) = n * f(n-1)`
* **종료 조건**: `n`이 `0`이거나 `1`이면 `1`을 반환.

### 💻 풀이 코드

```python
import sys
input = sys.stdin.readline

def factorial(n):
    # 종료 조건: 0! = 1, 1! = 1
    if n <= 1:
        return 1
    
    # 재귀 호출: n * (n-1)!
    return n * factorial(n - 1)

N = int(input())
print(factorial(N))

```

---

# 3. 분할 정복 (2D 배열 재귀): [Silver 1] Z (1074번)

**"2차원 배열 + 재귀"** 유형의 대표 문제다. 삼성 A형이나 코딩 테스트에서 자주 나오는 **분할 정복(Divide and Conquer)** 로직을 연습하기 좋다.

* **링크**: [https://www.acmicpc.net/problem/1074](https://www.acmicpc.net/problem/1074)
* **핵심**:
*  배열을 4등분(Z모양 순서)하여 내가 찾는 좌표 `(r, c)`가 어디에 속하는지 찾는다.
* 속하지 않는 영역은 과감히 건너뛰고(숫자를 더해주고), 속하는 영역으로 범위를 좁혀 재귀 호출한다.



### 💻 풀이 코드

```python
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def z_search(n, x, y):
    # n: 현재 탐색하는 크기 지수 (2^n)
    # x, y: 현재 탐색 영역의 왼쪽 위 좌표
    
    # 종료 조건: 1x1 크기가 되면 0 반환 (도착)
    if n == 0:
        return 0
    
    # 절반 크기 계산
    half = 2 ** (n - 1)
    
    # 사분면 크기 (한 사분면의 칸 수)
    # 예: n=2이면 한 변 4, 반은 2, 면적은 4
    area = half * half 
    
    # 1사분면 (좌상)
    if r < x + half and c < y + half:
        return z_search(n - 1, x, y)
        
    # 2사분면 (우상) -> 1사분면 크기만큼 더하고 시작
    elif r < x + half and c >= y + half:
        return area + z_search(n - 1, x, y + half)
        
    # 3사분면 (좌하) -> 1, 2사분면 크기만큼 더하고 시작
    elif r >= x + half and c < y + half:
        return 2 * area + z_search(n - 1, x + half, y)
        
    # 4사분면 (우하) -> 1, 2, 3사분면 크기만큼 더하고 시작
    else:
        return 3 * area + z_search(n - 1, x + half, y + half)

# [주의] 이 문제는 재귀로 "탐색"만 하면 시간 초과가 날 수 있음.
# 위 코드처럼 "좌표 계산"을 통해 건너뛰는 방식이 정석임.
print(z_search(N, 0, 0))

```

---

# 4. 패턴 재귀: [Silver 2] 색종이 만들기 (2630번)

특정 영역이 모두 같은 색인지 확인하고, 아니면 **4등분**해서 다시 확인하는 문제다. **쿼드 트리(Quad Tree)**라고도 불린다.

* **링크**: [https://www.acmicpc.net/problem/2630](https://www.acmicpc.net/problem/2630)
* **핵심**:
* 현재 영역이 모두 같은 색(`0` 또는 `1`)인지 검사한다.
* 하나라도 다른 색이 섞여 있다면, 가로/세로를 절반으로 잘라 4개의 작은 영역에 대해 재귀 호출한다.



### 💻 풀이 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 하얀색(0), 파란색(1) 개수
white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    color = paper[x][y] # 첫 번째 칸의 색깔 기준
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]: # 다른 색이 섞여 있으면
                # 4등분 해서 재귀 호출
                half = n // 2
                cut(x, y, half)             # 1사분면
                cut(x, y + half, half)      # 2사분면
                cut(x + half, y, half)      # 3사분면
                cut(x + half, y + half, half) # 4사분면
                return # 쪼개고 나면 현재 함수는 종료
    
    # 반복문을 무사히 통과했다면 모두 같은 색임
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, N)
print(white)
print(blue)

```

---

### ✅ 학습 가이드

1. **팩토리얼**로 재귀의 기본 구조(종료 조건 + 호출)를 익힌다.
2. **색종이 만들기(2630)**를 풀면서 2차원 배열에서 영역을 쪼개 들어가는 감각을 익힌다.
3. **Z(1074)**는 좌표 계산이 들어가서 조금 까다로울 수 있으니, 색종이 문제를 먼저 풀고 도전하는 것을 추천한다.

이 재귀 로직에 익숙해져야 다음 단계인 **백트래킹(N-Queen 등)**을 수월하게 정복할 수 있다.