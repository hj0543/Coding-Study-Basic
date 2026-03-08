아래는 **백준에서 자주 나오는 입력 형식**을 유형별로 정리하고, 각각에 대해 **입력 예시 + 파이썬 코드 템플릿**을 함께 붙인 것입니다.

---

## 1) 첫 줄에 `N`, 둘째 줄에 `N개` 정수(가로)

### 입력 예시

```
5
1 10 4 9 2
```

### 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
```

## +a
### 입력 예시

```
89, 90, 100
```

### 코드

```python
numbers = list(map(int, input().split(',')))
```
```python
a, b, c = map(int, input().split(','))
```
---

## 2) 첫 줄에 `N`, 다음 `N줄`에 정수 1개씩(세로)

### 입력 예시

```
5
1
10
4
9
2
```

### 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    nums = int(input())
```
## +a 'N'줄 갯수가 정해진 경우(세로)
nums = []
### 입력 예시
```
10
10
20
30
40
```
### 코드
```python
for _ in range(5):   # 입력 개수가 5개일 때
    nums.append(int(input()))
```
---

## 3) 첫 줄에 `N X`, 둘째 줄에 `N개` 정수(백준 10871 스타일)

### 입력 예시

```
10 5
1 10 4 9 2 3 8 5 7 6
```

### 코드

```python
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
```

---

## 4) 첫 줄에 `N M`, 다음 `N줄`에 `M개` 정수(2차원 배열/행렬)

### 입력 예시

```
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

### 코드

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
```

---

## 5) 첫 줄에 테스트케이스 `T`, 이후 `T줄`에 케이스(한 줄에 값 여러 개)

### 입력 예시

```
3
1 2
3 4
5 6
```

### 코드

```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    # 처리
```

---

## 6) 테스트케이스 `T`, 각 케이스가 여러 줄로 구성

### 입력 예시

```
2
5
1 2 3 4 5
3
10 20 30
```

### 코드

```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    # 처리
```

---

## 7) `N`이 안 주어짐: EOF(입력 끝까지) — 세로 입력

### 입력 예시

```
7
3
9
2
```

(여기서 파일/입력이 끝나면 종료)

### 코드(한 줄씩)

```python
import sys

nums = []
for line in sys.stdin:
    line = line.strip()
    if line:
        nums.append(int(line))
```

### 코드(통째로, 가장 강력)

```python
import sys

nums = list(map(int, sys.stdin.buffer.read().split()))
```

---

## 8) 특정 값이 나오면 종료(센티널, 예: 0이면 끝)

### 입력 예시

```
5
3
2
0
```

### 코드

```python
import sys
input = sys.stdin.readline

nums = []
while True:
    x = int(input())
    if x == 0:
        break
    nums.append(x)
```

---

## 9) 문자열 한 줄(공백 포함 가능)

### 입력 예시

```
Hello World from Baekjoon
```

### 코드

```python
import sys
input = sys.stdin.readline

s = input().rstrip("\n")  # 공백은 유지, 개행만 제거
```

---

## 10) 숫자/문자열을 “한 글자씩” 배열로 (예: 101110)

### 입력 예시

```
101110
```

### 코드(문자 리스트)

```python
s = input().strip()
arr = list(s)  # ['1','0','1','1','1','0']
```

### 코드(정수 리스트)

```python
s = input().strip()
arr = list(map(int, s))  # [1,0,1,1,1,0]
```

---

# 출력 템플릿도 같이(자주 씀)

## A) 리스트를 가로로(공백)

```python
print(" ".join(map(str, A)))
# 또는
print(*A)
```

## B) 리스트를 세로로(줄바꿈)

```python
print("\n".join(map(str, A)))
# 또는
print(*A, sep="\n")
```
