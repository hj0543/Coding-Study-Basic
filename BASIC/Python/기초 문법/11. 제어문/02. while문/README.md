# 02 while문 (While Loop)

### 1. while문의 기본 구조
* 조건문이 **참(True)**인 동안, while문 아래에 속한 문장들을 계속해서 수행합니다.
* if - elif - elif - else 구문을 while로 간단하게 나타낼 수 있다. 

**기본 생김새:**   
```python
while 조건문:
    수행할_문장1
    수행할_문장2
    ...
```
---
### 2. 기본 예제 (나무 찍기)
> "열 번 찍어 안 넘어가는 나무 없다"는 속담을 파이썬으로 구현한 예제입니다.   

```Python

treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10: # 나무 찍은 횟수가 10회가 되면 ~~
        print("나무 넘어갑니다.")
```
* 결과: 나무를 1번~10번 찍는 메시지가 출력되고, 10번이 되면 "나무 넘어갑니다." 출력 후 종료됩니다.   
---
### 3. while문 강제로 빠져나가기 (break)
> 반복문 수행 중 특정 조건에서 즉시 반복을 멈추고 싶을 때 break를 사용합니다.

```Python

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break  # while문을 즉시 탈출!
```
---
### 4. 맨 처음으로 돌아가기 (continue)
> 반복문 안에서 continue를 만나면, 아래 문장들을 수행하지 않고 while문의 맨 처음(조건문)으로 돌아갑니다.

```Python

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0: 
        continue   # 짝수면 아래 print를 하지 않고 조건문으로 돌아감
    print(a)
결과: 1, 3, 5, 7, 9 (홀수만 출력됨)
```
---
### 5. 무한 루프 (Infinite Loop)
> 조건문을 항상 True로 설정하면 영원히 반복되는 무한 루프를 만들 수 있습니다. (멈추려면 Ctrl+C를 눌러야 합니다.)

```Python

while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
```
