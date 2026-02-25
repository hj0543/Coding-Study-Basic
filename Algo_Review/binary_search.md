
## [Algorithm] 이분 탐색 (Binary Search) 완벽 정리

### 1. 이분 탐색이란?

정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 찾는 알고리즘**.

가장 쉬운 예시는 **'업-다운(Up-Down) 게임'**이다.

> 1부터 100 사이의 숫자를 맞출 때, 1, 2, 3... 순서대로 부르는 사람은 없다.
> 보통 **50(중간값)**을 먼저 부르고, "Up"이면 51~100 사이, "Down"이면 1~49 사이를 탐색한다.
> 이 과정을 반복하면 엄청나게 빠른 속도로 정답을 찾을 수 있다.

### 2. 핵심 조건 (★중요)

이분 탐색을 사용하려면 데이터가 반드시 **정렬(Sorted)되어 있어야 한다.**
정렬되지 않은 데이터에는 사용할 수 없다.

### 3. 동작 방식

변수 3개를 사용한다: `start`(시작점), `end`(끝점), `mid`(중간점).

1. `mid`를 설정한다. `(start + end) // 2`
2. `mid` 값과 찾으려는 값(`target`)을 비교한다.
* `target == mid`: 탐색 성공! (인덱스 반환)
* `target < mid`: 정답이 왼쪽에 있다. → `end = mid - 1`로 범위 축소.
* `target > mid`: 정답이 오른쪽에 있다. → `start = mid + 1`로 범위 축소.


3. `start > end`가 될 때까지 반복한다. (못 찾으면 종료)

### 4. 시간 복잡도: 

데이터가 2배로 늘어나도, 연산 횟수는 1회만 늘어난다.

* **순차 탐색(Linear Search):** 데이터 10억 개 → 최악의 경우 **10억 번** 비교.
* **이분 탐색(Binary Search):** 데이터 10억 개 → 약 **30번**만 비교하면 끝.

> **Why?** 

### 5. Python 코드 구현 (템플릿)

가장 많이 쓰이는 **반복문(Iterative)** 방식이다. (재귀보다 이 방식을 추천)

```python
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    # start가 end를 넘어설 때까지 반복
    while start <= end:
        mid = (start + end) // 2
        
        # 값을 찾은 경우
        if arr[mid] == target:
            return mid 
            
        # target이 중간값보다 큰 경우 (오른쪽 확인)
        elif arr[mid] < target:
            start = mid + 1
            
        # target이 중간값보다 작은 경우 (왼쪽 확인)
        else:
            end = mid - 1
            
    return -1  # 찾는 값이 없을 때

```
#### 개수구하기 (백준 10816)
```python
import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

N = int(input())
finder = list(map(int, input().split()))
find_range = sorted(finder)

M = int(input())
target = list(map(int, input().split()))
result = [0] * M

for i in range(M):
    result[i] += upper_bound(find_range, target[i]) - lower_bound(find_range, target[i])

print(*result)
```
### 6. Python 꿀팁: `bisect` 라이브러리

파이썬은 이분 탐색을 위한 표준 라이브러리를 제공한다. 직접 구현할 필요 없이 이걸 쓰면 매우 편하다.

```python
from bisect import bisect_left, bisect_right

nums = [1, 2, 4, 4, 8]
target = 4

# bisect_left: 정렬된 순서를 유지하며 target을 삽입할 가장 왼쪽 인덱스
print(bisect_left(nums, target))  # 결과: 2

# bisect_right: 정렬된 순서를 유지하며 target을 삽입할 가장 오른쪽 인덱스
print(bisect_right(nums, target)) # 결과: 4

```

> **Tip:** 특정 범위 `[left_val, right_val]`에 속하는 데이터의 개수를 구할 때 `bisect_right - bisect_left`를 쓰면 $O(1)$이나 다름없이(정확히는 ) 구할 수 있다.

### 7. 응용: 파라메트릭 서치 (Parametric Search)

이분 탐색의 심화 버전. 코딩 테스트 고난이도 문제(랜선 자르기, 나무 자르기 등)에 주로 나온다.

* **개념:** "최적화 문제(최댓값/최솟값 찾기)"를 "결정 문제(Yes/No)"로 바꾸어 푸는 것.
* **예시:** "랜선을 최대 길이 몇으로 잘라야 할까?" → "길이를 X로 잘랐을 때, 개수가 충분한가? (Yes/No)"
* Yes면 길이를 더 늘려보고(Up), No면 길이를 줄인다(Down).

---

### 💡 요약

1. **조건:** 데이터가 정렬되어 있을 때만 사용 가능.
2. **속도:** $O(\log N)$으로 엄청 빠름.
3. **구현:** `start <= end` 조건을 기억하고, `mid`를 기준으로 범위를 반씩 줄인다.
4. **라이브러리:** 단순 탐색은 `bisect` 모듈을 적극 활용하자.
