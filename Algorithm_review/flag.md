## 1. 플래그를 False(아직 못 찾음)로 시작
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
