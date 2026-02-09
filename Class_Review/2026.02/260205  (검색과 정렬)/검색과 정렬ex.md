
# 📝 실전 백준 문제로 보는 검색과 정렬

## 1. 이진 검색 기초: [Silver 4] 수 찾기 (1920번)

이진 검색의 가장 교과서적인 문제입니다. `N`개의 데이터 안에 특정 `target`이 존재하는지 빠르게 확인해야 합니다.

* **문제 링크**: [https://www.acmicpc.net/problem/1920](https://www.acmicpc.net/problem/1920)
* **핵심 포인트**:
* 데이터의 개수 `N`이 최대 10만, 탐색할 수 `M`이 최대 10만입니다.
* 단순 순차 탐색()을 하면 시간 초과가 납니다.
* 반드시 **정렬(`sort`) 후 이진 검색()**을 사용해야 합니다.



### 💻 풀이 코드

```python
import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] > target: # 타겟이 더 작으므로 왼쪽 탐색
            end = mid - 1
        else: # 타겟이 더 크므로 오른쪽 탐색
            start = mid + 1
            
    return False

# 1. 입력 및 정렬
N = int(input())
# 이진 검색의 필수 전제조건: 정렬!
A = list(map(int, input().split()))
A.sort() 

M = int(input())
targets = list(map(int, input().split()))

# 2. 각 타겟에 대해 이진 검색 수행
for t in targets:
    if binary_search(A, t):
        print(1)
    else:
        print(0)

```

---

## 2. 정렬의 응용: [Silver 5] 소트인사이드 (1427번)

선택 정렬 로직을 이해하고 있다면 쉽게 풀 수 있는 문제입니다. (물론 파이썬 내장 함수가 강력하지만, 정렬 원리를 복습하기 좋습니다.)

* **문제 링크**: [https://www.acmicpc.net/problem/1427](https://www.acmicpc.net/problem/1427)
* **핵심 포인트**:
* 숫자의 각 자릿수를 분리하여 **내림차순**으로 정렬해야 합니다.
* 선택 정렬을 사용한다면 `max_idx`를 찾아 맨 앞과 교환하는 방식을 씁니다.



### 💻 풀이 코드 (선택 정렬 구현)

```python
import sys
input = sys.stdin.readline

# 문자열로 받아서 리스트로 변환
arr = list(map(int, list(input().strip())))
N = len(arr)

# 선택 정렬 (내림차순)
for i in range(N - 1):
    max_idx = i # 최댓값 위치 찾기
    
    for j in range(i + 1, N):
        if arr[j] > arr[max_idx]: # 더 큰 값 발견
            max_idx = j
            
    # Swap (교환)
    arr[i], arr[max_idx] = arr[max_idx], arr[i]

# 결과 출력 (리스트 -> 문자열)
print(''.join(map(str, arr)))

```

---

## 3. 정렬 + 좌표 압축(순위 찾기): [Silver 2] 좌표 압축 (18870번)

"k번째로 작은 수" 개념을 확장하여, **"나보다 작은 수가 몇 개인지"**를 찾는 문제입니다. 정렬과 이진 검색(또는 딕셔너리)을 결합해야 합니다.

* **문제 링크**: [https://www.acmicpc.net/problem/18870](https://www.acmicpc.net/problem/18870)
* **핵심 포인트**:
* 중복된 수를 제거(`set`)하고 정렬하면, **인덱스가 곧 '나보다 작은 수의 개수'**가 됩니다.
* 예: `[-10, -9, 2, 4]` 에서 `2`의 인덱스는 2이고, 이는 `2`보다 작은 수가 2개(`-10, -9`)라는 뜻입니다.



### 💻 풀이 코드

```python
import sys
input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))

# 1. 중복 제거 및 정렬
# sorted_coords[i] : i번째로 작은 수
sorted_coords = sorted(list(set(coords)))

# 2. 딕셔너리로 {숫자 : 순위(인덱스)} 매핑 생성
# 리스트 탐색 시간(O(N))을 줄이기 위해 해시(O(1)) 사용
rank_dic = {value : idx for idx, value in enumerate(sorted_coords)}

# 3. 원본 좌표를 순위로 변환하여 출력
for x in coords:
    print(rank_dic[x], end=' ')

```

---

✅ **다음 단계**
지금까지 배열과 검색/정렬 알고리즘의 기초를 탄탄히 다졌다. 이제 프로그래밍의 난이도가 한 단계 올라가는 **문자열(String)** 처리로 넘어가서, 아스키코드, 문자열 뒤집기, 문자열 비교 알고리즘 등을 정리해 보자.
