### Bubble sort
```python
def bubble_sort(a, N) : 	# 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1) : # 범위의 끝 위치
        for j in range(i) :		# 비교할 왼쪽 원소 인덱스 j
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j] 
```

### Counting sort
```python
def counting_sort(DATA, TEMP, k):


# DATA [] -- 입력 배열(0 to k)
# TEMP [] -- 정렬된 배열.
# COUNTS [] -- 카운트 배열.

    COUNTS = [0] * (k + 1)

    for i in range(0, len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k + 1):
        COUNTS[i] += COUNTS[i - 1]

    for i in range(len(TEMP) - 1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]

arr = [0,4,1,3,1,2,4,1]
tmp = [0]*len(arr)
counting_sort(arr, tmp, 5)
print(tmp)
```