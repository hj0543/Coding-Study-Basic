
## 1. 플래그 변수의 기본 원리
보통 True 혹은 False 값을 가지는 불리언(Boolean) 변수를 사용합니다.

초기화: 루프 시작 전에 "아직 못 찾았다"(False)라고 설정합니다.

상태 변경: 루프 중간에 원하는 조건을 만족하면 "찾았다"(True)로 바꿉니다.

확인: 루프가 다 끝난 뒤 플래그 값을 보고 후속 처리를 합니다.

## 2. 2중 for문에서 플래그 사용하기
```python
found_flag = False

for i in range(5):
    for j in range(5):
        if i + j == 100: # 절대 일어날 수 없는 조건 예시
            print(f"찾았다: {i}, {j}")
            found_flag = True # 찾았으므로 스위치를 올림(True)
            break # 안쪽 루프 탈출
            
    if found_flag: # 안쪽에서 찾았다면 바깥쪽 루프도 바로 탈출
        break

# 2. 모든 루프가 끝난 뒤 플래그 상태 확인
if not found_flag:
    print("아무리 찾아도 값이 없네요!")
```
