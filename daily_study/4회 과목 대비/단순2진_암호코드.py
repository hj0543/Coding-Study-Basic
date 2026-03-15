import sys
sys.stdin = open('단순2진_암호코드.txt', 'r')

number_data = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    decode = [input().rstrip() for _ in range(n)]
    # print(decode)

    nums = []
    found = False

    for row in decode:
        if '1' in row:
            end_idx = row.rfind('1')
            target = row[end_idx - 55: end_idx + 1]
            
            for i in range(0, 56, 7):
                number = target[i: i + 7]
                nums.append(number_data[number])
            found = True
            break
        if found:
            break

    # print(nums)
    odd_number = [nums[1], nums[3], nums[5], nums[7]]
    even_number = [nums[0], nums[2], nums[4], nums[6]]

    if (sum(even_number) * 3 + sum(odd_number)) % 10 == 0:
        print(f"#{tc} {sum(nums)}")
    else:
        print(f"#{tc} 0")