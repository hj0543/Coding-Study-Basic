`try` / `except`는 **에러가 발생할 수 있는 코드를 안전하게 실행**하기 위한 파이썬의 예외 처리 구조
프로그램이 중간에 멈추지 않게 하고, 에러 상황에 맞는 처리 할 수 있음.

---

## 🔹 기본 구조

```python
try:
    # 에러가 발생할 수 있는 코드
except:
    # 에러가 발생했을 때 실행할 코드
```

---

## 📌 1. 왜 쓰는가?

예를 들어:

```python
print(10 / 0)
```

이 코드는 실행하면 **ZeroDivisionError**가 발생해서 프로그램이 즉시 종료

하지만 `try-except`를 쓰면:

```python
try:
    print(10 / 0)
except:
    print("0으로 나눌 수 없습니다.")
```

👉 프로그램이 멈추지 않고, 대신 메시지를 출력함.

---

## 📌 2. 여러 종류의 에러를 구분해서 처리

```python
try:
    x = int(input())
    y = 10 / x
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자를 입력해야 합니다.")
```

👉 에러 종류에 따라 다른 메시지를 출력할 수 있음.

---

## 📌 3. 에러가 없을 때만 실행되는 `else`

```python
try:
    x = int(input())
except ValueError:
    print("숫자가 아닙니다.")
else:
    print("입력한 숫자:", x)
```

👉 에러가 없을 때만 `else` 블록 실행.

---

## 📌 4. 에러가 있든 없든 항상 실행되는 `finally`

```python
try:
    f = open("data.txt")
    print(f.read())
except:
    print("파일이 없습니다.")
finally:
    print("프로그램 종료")
```

👉 파일이 있든 없든 `"프로그램 종료"`는 항상 출력됨.

---

## 📌 5. 백준에서 자주 쓰는 패턴 (EOF 처리)

입력이 끝날 때까지 계속 읽고 싶을 때:

```python
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
```
* 입력을 받고 A+B를 출력

* 예외가 발생하면 반복문을 종료 (break)

* 예외 처리가 while 안에 있음

⚠️ 단점:

except:는 모든 예외를 잡음 → 버그도 같이 숨김 (좋은 습관은 아님)



👉 입력이 더 이상 없으면 `EOFError`가 발생 → `except`로 잡고 종료.

## 6. 그대로 출력하기
```python
try:
    while True:
        print(input())
except EOFError:
    pass
```
* 입력만 받고 아무 출력도 하지 않음

* EOFError가 나면 조용히 종료 (pass)

* 예외 처리가 while 바깥에 있음

⚠️ 문제점:

숫자 개수가 부족하거나 형식이 잘못되면 ValueError가 발생 → 프로그램이 종료됨 (잡히지 않음)


---

## 🧠 핵심 요약

| 구성        | 의미            |
| --------- | ------------- |
| `try`     | 에러가 날 수 있는 코드 |
| `except`  | 에러가 났을 때 실행   |
| `else`    | 에러가 없을 때 실행   |
| `finally` | 무조건 실행        |
