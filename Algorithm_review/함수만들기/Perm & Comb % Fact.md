### 팩토리얼(Factorial) - 순열
```python
def factorial(n):
    total = 1
    for i in range(n):
        total *= n
    return total
```

### 조합(Combination)
```python
def comb(n, r)
    factorial(n) / (factorial(n - r) * factorial(r))
```

**세 수의 조합**
```python
def comb(a, b, c)
    factorial(a + b + c) / (factorial(a) * factorial(b) * factorial(c))
```







