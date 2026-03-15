T = int(input())
for tc in range(1, T + 1):
    data = input()
    bin_num = ''
    for i in data:
        bin_num += f'{int(i, 16):04b}'

    result = []

    idx = 0
    while idx < len(bin_num):
        n = bin_num[idx:idx + 7]
        result.append(int(n,2))
        idx += 7
    print(f'#{tc}', *result)