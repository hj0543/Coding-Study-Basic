


#====================소수========================















### n 이하의 소수





### n이하의 소수의 개수
```python
def count_primes(n):
    if n < 2:
        return 0
    # 0부터 n까지 소수 여부를 저장하는 리스트 (True로 초기화)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # 2부터 n의 제곱근까지 반복
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # i의 배수들을 False로 변경
            sieve[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))
            
    # True인 개수를 카운트
    return sum(sieve)
```