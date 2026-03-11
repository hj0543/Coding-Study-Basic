병합 정렬(Merge Sort)은 **'분할 정복(Divide and Conquer)'**의 정수를 보여주는 알고리즘이다.

배열을 더 이상 쪼갤 수 없을 때까지 반으로 계속 나눈 뒤, 다시 합치면서(Merge) 정렬을 수행하는 방식이다. 데이터의 상태가 어떻든 간에 항상 **$O(N \log N)$** 이라는 매우 안정적이고 빠른 속도를 보장하는 것이 가장 큰 무기다.

### 💡 핵심 원리: 반으로 쪼개고, 정렬하며 합친다

1. **분할(Divide):** 배열의 길이가 1이 될 때까지 무조건 절반으로 쪼갠다.
2. **정복(Conquer):** 쪼개진 배열들을 2개씩 짝지어서, 크기를 비교하며 정렬된 상태로 임시 배열에 합쳐 올린다.
3. **결합(Combine):** 이 과정을 반복해 원래 배열의 크기까지 도달하면 완벽한 정렬이 끝난다.

---

### 💻 병합 정렬 완벽 템플릿 (Python)

파이썬의 리스트 슬라이싱을 활용하면 코드가 매우 직관적이고 우아해진다. 분할하는 함수와 병합하는 로직을 하나로 합친 가장 스탠다드한 코드다.

```python
def merge(left_list, right_list):
    """
    두 개의 정렬된 리스트를 받아서 하나로 합치는 함수
    """
    merged = []
    left = 0
    right = 0
    
    # 양쪽 리스트에 원소가 남아있는 동안 비교하며 병합
    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            merged.append(left_list[left])
            left += 1
        else:
            merged.append(right_list[right])
            right += 1
            
    # 한쪽 리스트가 먼저 소모된 경우, 남은 원소들을 뒤에 붙임
    merged += left_list[left:]
    merged += right_list[right:]
    
    return merged

def merge_sort(arr):
    """
    재귀적으로 배열을 분할한 뒤 merge 함수를 호출하는 메인 함수
    """
    # 기저 조건: 길이가 1 이하면 이미 정렬된 상태
    if len(arr) <= 1:
        return arr
        
    # 1. 분할 (Divide)
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # 2. 병합 (Merge) - 분리된 merge 함수 호출
    return merge(left_half, right_half)

# 테스트
arr = [38, 27, 43, 3, 9, 82, 10]
result = merge_sort(arr)
print(f"정렬 전: {arr}")
print(f"정렬 후: {result}")

```

---

### ⏱️ 시간 복잡도와 치명적인 단점

* **시간 복잡도:** 최선, 평균, 최악의 경우 모두 **$O(N \log N)$** 을 완벽하게 보장한다. (배열을 반으로 쪼개는 깊이가 $\log N$이고, 각 깊이마다 원소를 비교하고 합치는 데 $N$의 시간이 걸리기 때문이다.)
* **공간 복잡도:** **$O(N)$**. 이것이 병합 정렬의 유일하고도 치명적인 단점이다. 기존 배열의 값을 서로 맞바꾸는(Swap) 방식이 아니라, `merged`라는 **새로운 임시 배열(메모리)을 계속 만들어야만 작동**하기 때문이다. 메모리 제한이 극단적으로 빡빡한 코딩 테스트 문제에서는 이 점을 주의해야 한다.