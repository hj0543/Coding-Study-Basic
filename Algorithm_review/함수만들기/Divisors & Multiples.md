






### 약수
```python
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: # 제곱수가 아닌 경우 대칭되는 약수 추가
                divisors.append(n // i)
    return sorted(divisors)
```
### 배수




### 최대공약수



### 최소공배수