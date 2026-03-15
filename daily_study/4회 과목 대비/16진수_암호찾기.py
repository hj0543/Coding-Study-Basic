import sys
sys.stdin = open('16진수_암호찾기.txt', 'r')

number_data = {
    '001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
    '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9
}

T = int(input())
for tc in range(1, T + 1):
    data = input().rstrip()

    bin_num = ''
    for i in data:
        bin_num += f'{int(i, 16):04b}'

    result = []
    idx = 0
    while idx <= len(bin_num) - 6:
        chunk = bin_num[idx:idx + 6]

        if chunk in number_data:
            result.append(number_data[chunk])
            idx += 6
        else:
            idx += 1

    print(f'#{tc}', *result)





