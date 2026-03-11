퀵 정렬(Quick Sort)은 '분할 정복' 알고리즘의 대명사이자, 이름 그대로 실전에서 가장 '빠른' 정렬 알고리즘이다.

병합 정렬이 무조건 배열을 반으로 쪼개고 봤다면, 퀵 정렬은 기준이 되는 **'피벗(Pivot)'**을 하나 잡고, 이 피벗보다 작은 데이터는 왼쪽으로, 큰 데이터는 오른쪽으로 싹 몰아넣는(Partitioning) 방식을 사용한다.

### 💡 핵심 원리: 기준점을 잡고 패거리를 나눈다

1. **피벗 선택:** 배열에서 원소 하나를 골라 기준점(피벗)으로 삼는다. (보통 맨 앞, 맨 뒤, 혹은 중간값을 고른다.)
2. **분할(Partition):** 피벗을 기준으로 피벗보다 작은 놈들은 왼쪽으로, 큰 놈들은 오른쪽으로 보낸다.
3. **정복(Conquer):** 분할된 왼쪽 배열과 오른쪽 배열 각각에 대해 다시 새로운 피벗을 잡고 1~2번 과정을 반복한다. (재귀 호출)
4. 배열의 크기가 1 이하가 되면 더 이상 나눌 수 없으므로 정렬이 완료된다.

---

### 💻 퀵 정렬 완벽 템플릿 (Python) - 느리다... 아래의 hoare_partition 을 이용한 방법으로 알아두자.

C언어나 자바에서는 포인터(인덱스) 두 개를 양끝에서 출발시켜 서로 위치를 맞바꾸는(Swap) 복잡한 방식을 쓰지만, 파이썬의 **리스트 컴프리헨션**을 사용하면 퀵 정렬을 단 몇 줄 만에 아주 우아하게 구현할 수 있다. 코딩 테스트에서 직접 구현해야 한다면 이 방식이 압도적으로 직관적이고 기억하기 쉽다.

```python
def quick_sort(arr):
    # 기저 조건: 배열의 길이가 1 이하라면 이미 정렬된 것이므로 그대로 반환한다.
    if len(arr) <= 1:
        return arr

    # 1. 피벗 설정 (여기서는 맨 첫 번째 원소를 고름)
    pivot = arr[0]
    # 2. 피벗을 제외한 나머지 배열
    tail = arr[1:]

    # 3. 분할 (리스트 컴프리헨션으로 직관적으로 분류)
    left_side = [x for x in tail if x <= pivot] # 피벗보다 작거나 같은 것들
    right_side = [x for x in tail if x > pivot] # 피벗보다 큰 것들

    # 4. 분할된 양쪽을 재귀적으로 정렬한 뒤, 가운데에 피벗을 끼워 넣어 합친다.
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# 테스트
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print("파이써닉 퀵 정렬 결과:", quick_sort(arr))
# 결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

---

### ⏱️ 시간 복잡도와 치명적인 함정

* **평균 시간 복잡도:** **O(N log N)**. 데이터를 절반씩 쪼개 나가며 정렬하므로 병합 정렬과 동일하게 매우 빠르다. 메모리 공간을 덜 차지하기 때문에 실제 컴퓨터 환경에서는 병합 정렬보다 미세하게 더 빠르다.
* **🔥 최악의 경우 (치명적 단점):** **O(N^2)**. 만약 **'이미 정렬되어 있는 배열'**에서 맨 앞 원소를 피벗으로 계속 고른다면 어떻게 될까? 분할이 절반씩 예쁘게 되지 않고 한쪽으로만 극단적으로 쏠리게 되어, 결국 모든 원소를 하나씩 비교하는 최악의 사태가 벌어진다.

*(참고로 파이썬의 기본 정렬인 `arr.sort()`는 이 퀵 정렬의 단점을 보완하고 병합 정렬의 장점을 섞은 '팀 소트(Tim Sort)' 알고리즘을 사용하므로 최악의 경우에도 **O(N log N)**을 보장한다.)*

---

```python
### hoare기법
arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# [참고] 피벗의 위치를 다양하게 고르는 경우 3가지를 함수로 만들었습니다.


# 피벗: 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition1(left, right):
    pivot = arr[left]  # 피벗을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right

    while i <= j:  # 교차가 되면 끝
        while i <= j and arr[i] <= pivot:  # i 는 pivot 보다 큰 값을 검색 (작거나 같으면 i += 1)
            i += 1

        while i <= j and arr[j] >= pivot:  # j 는 pivot 보다 작은 값을 검색 (크거나 같으면 j -= 1)
            j -= 1

        if i < j:  # swap
            arr[i], arr[j] = arr[j], arr[i]

    # pivot 과 j 위치를 swap
    arr[left], arr[j] = arr[j], arr[left]
    return j


# 피벗: 제일 오른쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
def hoare_partition2(left, right):
    pivot = arr[right]  # 피벗을 제일 오른쪽 요소로 설정
    i = left
    j = right - 1

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]
    return i


# 피벗: 중간 요소로 설정
# 일반적으로 더 균형 잡힌 분할이 가능하며, 퀵 정렬의 성능을 최적화할 수 있습니다.
def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left]  # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        # pivot = hoare_partition2(left, right)
        # pivot = hoare_partition3(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
```

---

```python
### lomuto기법

# 퀵 정렬 중 lomuto partition 을 활용한 코드입니다.
# i, j 가 hoare 와는 다르게 앞에서부터 함께 이동한다는 점을 이해해주시면 됩니다.
#  - hoare 와 동일하게 i 는 pivot 보다 큰 값을, j 는 작은 값을 찾아나갑니다.

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def lomuto_partition(left, right):
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
```
print(arr)
