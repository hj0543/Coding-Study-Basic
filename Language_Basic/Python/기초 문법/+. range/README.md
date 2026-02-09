range()는 1개, 2개 또는 3개의 매개변수를 가질 수 있습니다.
```python 
range(start, stop, step) # 슬라이싱과 비슷하게 생김
```
#### range(stop)
* 매개변수가 하나면 stop으로 인식
* start는 0, step은 1이 기본값으로 자동 설정
* range(5) -> 0, 1, 2, 3, 4

#### range(start, stop) -> start부터 stop-1까지
* 매개변수가 두 개면 start, stop으로 인식
* step은 1이 기본값으로 자동 설정
* range(2, 5) -> 2, 3, 4

#### range(start, stop, step) -> start부터 stop-1까지 step 간격으로
* 모든 매개변수를 start, stop, step으로 직접 지정
* range(2, 10, 2) -> 2, 4, 6, 8

```python
my_range = range(5)
my_range2 = range(1, 10)
my_range3 = range(5, 0, -1)

print(my_range) # range(0, 5)
print(my_range2) # range(1, 10)
print(my_range3) # range(5, 0, -1)

print(list(my_range))   # [0, 1, 2, 3, 4]
print(list(my_range2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range3))  # [5, 4, 3, 2, 1]
```
---

#### step이 양수인 경우
숫자가 start부터 stop-1까지 step 간격으로 증가
range(1, 10, 2) -> 1, 3, 5, 7, 9
```python
# 시작 값이 끝 값보다 작은 경우 (정상)
print(list(range(1, 5)))   # [1, 2, 3, 4]
# 시작 값이 끝 값보다 큰 경우 (비정상)
print(list(range(5, 1)))   # []

```
#### step이 음수인 경우
step이 음수일 때
숫자가 start부터 stop+1까지 step 간격으로 감소
range(10, 1, -2) -> 10, 8, 6, 4, 2
```python
# 시작 값이 끝 값보다 큰 경우 (정상)
print(list(range(5, 1, -1)))  # [5, 4, 3, 2]
# 시작 값이 끝 값보다 작은 경우 (비정상)
print(list(range(1, 5, -1)))  # []
```
