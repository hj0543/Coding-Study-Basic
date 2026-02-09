### 팩토리얼(Factorial)
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
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







