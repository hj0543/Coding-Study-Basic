```python
def fibo(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, b + a
```
