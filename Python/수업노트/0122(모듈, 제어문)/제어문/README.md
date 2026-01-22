# 제어문
코드의 실행 흐름을 제어하는 데 사용되는 구문
조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행
#### 조건문 - if, elif, else
```python
if score >= 90:
    message = "축하합니다! 최고입니다!"
elif score >= 70:
    print("멋져요! 잘하셨어요!")
else:
    print("조금 더 노력해보세요!")
```
#### 반복문 - for, while, break, continue
```python
for i in range(N):
    twinkle(message)
```
> **N = 3**이라고 가정 (3번 반복)
> **message**는 앞서 95점을 받아 **"축하합니다! 최고입니다!"**가 저장되었다고 가정
> twinkle() 함수는 메시지 앞뒤에 별(★)을 붙여서 출력하는 기능이라고 가정
> 실행 결과: range(3)이므로 i가 0, 1, 2로 변하면서 총 3번 실행됩니다.
> 
> Plaintext
> 
> ★ 축하합니다! 최고입니다! ★
> ★ 축하합니다! 최고입니다! ★
> ★ 축하합니다! 최고입니다! ★

```python
while True:
    print("계속할까요? (y/n)")
    answer = input()
    if answer == 'y':
        play()
    else:
        print("게임을 종료합니다.")
        break
```
> 계속할까요? (y/n)
> y
> (play() 함수가 실행되어 게임이 진행됨...)
> 
> 계속할까요? (y/n)
> n
> 게임을 종료합니다.
