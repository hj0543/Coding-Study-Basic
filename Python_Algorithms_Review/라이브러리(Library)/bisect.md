`bisect` 모듈은 코딩 테스트에서 가장 헷갈리고 실수하기 쉬운 **'이진 탐색(Binary Search)'을 단 한 줄로 끝내버리는 궁극의 치트키**다.

배열이 정렬되어 있을 때, 데이터를 처음부터 끝까지 찾는 $O(N)$의 무식한 방법을 버리고, 반씩 쪼개가며 **$O(\log N)$** 만에 특정 데이터가 들어갈 '위치(인덱스)'를 정확하게 꽂아준다. C++의 `lower_bound`, `upper_bound`와 완벽하게 같은 역할을 한다.

---

### 💡 핵심 무기: `bisect_left` vs `bisect_right`

배열 안에 **중복된 값**이 있을 때 이 두 함수의 진가가 발휘된다. 특정 값 `x`를 정렬을 흩트리지 않고 끼워 넣으려고 할 때, **어디에 넣을 것인가**를 결정한다.

* **`bisect_left(arr, x)`:** `x`가 들어갈 수 있는 가장 **왼쪽** 인덱스를 반환한다. (기존에 `x`가 있다면, 그 `x`들의 맨 앞자리)
* **`bisect_right(arr, x)`:** `x`가 들어갈 수 있는 가장 **오른쪽** 인덱스를 반환한다. (기존에 `x`가 있다면, 그 `x`들의 맨 뒷자리 바로 다음)
*(참고로 그냥 `bisect(arr, x)`라고 쓰면 `bisect_right`와 똑같이 동작한다.)*

---

### 💻 코드로 보는 압도적 편리함 (Python)

```python
from bisect import bisect_left, bisect_right

# 반드시 정렬된 배열이어야 한다!
arr = [1, 2, 4, 4, 4, 6, 8]
# 인덱스: 0  1  2  3  4  5  6

# 값 4가 들어갈 위치 찾기
left_idx = bisect_left(arr, 4)
right_idx = bisect_right(arr, 4)

print(f"4를 넣을 가장 왼쪽 위치: {left_idx}")   # 결과: 2 (첫 번째 4의 자리)
print(f"4를 넣을 가장 오른쪽 위치: {right_idx}") # 결과: 5 (마지막 4의 바로 다음 자리)

```

---

### 🔥 코딩 테스트 초특급 꿀팁: 특정 범위의 데이터 개수 구하기

카카오나 라인 같은 빡빡한 코딩 테스트에서 `bisect`를 쓰는 진짜 이유는 바로 이것이다. 수백만 개의 정렬된 데이터 속에서 **"값이 `[L, R]` 범위 안에 있는 데이터가 총 몇 개인가?"**를 $O(\log N)$ 만에 세어버릴 수 있다.

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 범위에 속하는 데이터의 개수를 반환하는 마법의 함수
def count_by_range(arr, left_value, right_value):
    right_idx = bisect_right(arr, right_value)
    left_idx = bisect_left(arr, left_value)
    return right_idx - left_idx

scores = [60, 75, 80, 80, 80, 85, 90, 95, 100]

# 80점부터 90점 사이를 맞은 학생은 몇 명인가?
count = count_by_range(scores, 80, 90)
print(f"80~90점 학생 수: {count}명") 
# 결과: 5명 (80, 80, 80, 85, 90)

```

> **원리:** `bisect_right(90)`은 90보다 큰 값이 시작되는 인덱스(7)를 주고, `bisect_left(80)`은 80이 시작되는 인덱스(2)를 준다. `7 - 2 = 5`개! 반복문 없이 단 뺄셈 한 번으로 끝난다.

---

### 📂 어디에 넣으면 좋을까?

* **분류:** **[알고리즘 - 이진 탐색]** 또는 **[파이썬 기초 - 필수 표준 라이브러리]**
* **사유:** 이진 탐색 알고리즘을 직접 짤 때 발생하는 지옥 같은 'Off-by-one' 에러(인덱스를 1 더할지 뺄지 헷갈리는 현상)를 원천 차단해 주는 완벽한 대체재이기 때문이다.

`while left <= right:`를 쓰면서 머리를 쥐어뜯게 만드는 이진 탐색까지 `bisect`로 완벽하게 썰어버렸다.