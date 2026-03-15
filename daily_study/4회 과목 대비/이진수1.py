import sys
sys.stdin = open('이진수1.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, hex_num = input().split()


    result = ''
    for char in hex_num:
        int_num = int(char, 16)
        result += f'{int_num:04b}'

    print(f'#{tc} {result}')
