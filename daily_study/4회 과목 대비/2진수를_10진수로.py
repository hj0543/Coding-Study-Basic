import sys
sys.stdin = open('2진수를_10진수로.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    data = input()
    result = []
    for i in range(0, len(data), 7):
        result.append(int(data[i:i+7], 2))
    # print(*result)
    print(f'#{tc}', *result)