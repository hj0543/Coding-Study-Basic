
# 📝 실전 문제로 보는 검색과 정렬

## 1. 이진 검색 활용: 책 페이지 찾기

이진 검색의 핵심인 **"범위를 반으로 줄여나가는 과정"**을 이해하기 가장 좋은 예제이다.

### ❓ 문제

책의 전체 페이지 수가 `N`쪽이다. 우리가 찾고자 하는 페이지가 `P`쪽일 때, 이진 검색으로 이 페이지를 찾으려면 **몇 번 만에** 찾을 수 있는지 구하시오.
(단, 검색 구간의 시작을 `start`, 끝을 `end`라 할 때, 중간 페이지 `middle = int((start + end) / 2)`로 계산한다.)

### 💡 풀이 접근

1. 초기 범위: `start = 1`, `end = N`
2. `middle` 계산 후 `target`과 비교한다.
* `target == middle`: 찾음 (종료)
* `target < middle`: 왼쪽 구간 선택  `end = middle` (또는 `middle - 1`)
* `target > middle`: 오른쪽 구간 선택  `start = middle` (또는 `middle + 1`)
* *(문제의 조건에 따라 범위 갱신 방식이 조금씩 다를 수 있으나, 보통 `middle-1`, `middle+1`을 사용한다.)*



### 💻 코드

```python
def binary_search_count(N, target):
    start = 1
    end = N
    count = 0 # 탐색 횟수
    
    while start <= end:
        middle = (start + end) // 2
        count += 1
        
        if middle == target: # 찾았다!
            return count
        elif middle > target: # 찾는 쪽이 더 작으면 왼쪽으로
            end = middle - 1
        else: # 찾는 쪽이 더 크면 오른쪽으로
            start = middle + 1
            
    return -1 # 못 찾음

# 전체 400쪽, 목표 300쪽
total_page = 400
target_page = 300
attempts = binary_search_count(total_page, target_page)

print(f"탐색 횟수: {attempts}번")

```

---

## 2. 선택 정렬 활용: 오름차순 정렬 과정

선택 정렬은 **"가장 작은 것을 골라 맨 앞으로 보낸다"**는 단순한 논리를 반복한다.

### ❓ 문제

다음 리스트를 선택 정렬을 사용하여 오름차순으로 정렬하시오. 각 단계(Pass)마다 리스트가 어떻게 변하는지 과정을 확인하시오.
`data = [64, 25, 12, 22, 11]`

### 💡 풀이 접근

1. **Pass 1**: 전체 중 최솟값(`11`)을 찾아 맨 앞(`64`)과 교환한다. `[11, 25, 12, 22, 64]`
2. **Pass 2**: 두 번째 칸부터 끝까지 중 최솟값(`12`)을 찾아 두 번째(`25`)와 교환한다. `[11, 12, 25, 22, 64]`
3. 이 과정을 `N-1`번 반복한다.

### 💻 코드

```python
def selection_sort_trace(arr):
    N = len(arr)
    
    for i in range(N - 1): # 마지막 하나는 자동 정렬되므로 N-1번만 수행
        min_idx = i # 기준 위치를 최솟값 인덱스로 가정
        
        # i+1부터 끝까지 훑으면서 진짜 최솟값 찾기
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # 값 교환 (Swap)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # 과정 출력
        print(f"{i+1}단계: {arr}")

data = [64, 25, 12, 22, 11]
selection_sort_trace(data)

# 출력 결과
# 1단계: [11, 25, 12, 22, 64] -> 11이 맨 앞으로 옴
# 2단계: [11, 12, 25, 22, 64] -> 12가 두 번째로 옴
# 3단계: [11, 12, 22, 25, 64] -> 22가 세 번째로 옴
# 4단계: [11, 12, 22, 25, 64] -> 25가 네 번째로 옴 (정렬 완료)

```

---

## 3. 셀렉션 알고리즘: k번째로 작은 수 찾기

선택 정렬을 응용하여 전체를 다 정렬하지 않고도 원하는 순위의 값을 찾을 수 있다.

### ❓ 문제

주어진 리스트에서 **3번째로 작은 수**를 구하시오. (전체 정렬을 끝까지 수행할 필요 없음)
`data = [9, 5, 3, 1, 7]`

### 💻 코드

```python
def find_kth_small(arr, k):
    # k번째까지만 정렬을 수행함 (시간 절약)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr[k-1] # 인덱스는 0부터 시작하므로 k-1

data = [9, 5, 3, 1, 7]
k = 3
result = find_kth_small(data, k)
print(f"{k}번째로 작은 수: {result}") 
# 1단계: [1, 5, 3, 9, 7]
# 2단계: [1, 3, 5, 9, 7]
# 3단계: [1, 3, 5, 9, 7] -> 3번째 값인 5 반환

```

---

✅ **다음 단계**
지금까지 배열과 검색/정렬 알고리즘의 기초를 탄탄히 다졌다. 이제 프로그래밍의 난이도가 한 단계 올라가는 **문자열(String)** 처리로 넘어가서, 아스키코드, 문자열 뒤집기, 문자열 비교 알고리즘 등을 정리해 보자.