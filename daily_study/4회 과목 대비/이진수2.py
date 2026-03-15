import sys
sys.stdin = open('이진수2.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n = float(input())

    result = []
    counts = 0

    while n > 0:
        if n == 0:
            break
        if n * 2 >= 1:
            result.append('1')
            n = n * 2 - 1
            counts += 1
        else:
            result.append('0')
            n = n * 2
            counts += 1

    if counts >= 13:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {''.join(result)}")

    