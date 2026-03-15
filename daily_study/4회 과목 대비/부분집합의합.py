import sys
sys.stdin = open('부분집합의합.txt', 'r')


def dfs_subset(idx, subset):
    global result

    if idx == 12:
        if len(subset) == N and sum(subset) == K:
            result += 1
        return

    # 현재 원소를 포함하는 경우
    dfs_subset(idx + 1, subset + [A[idx]])

    # 현재 원소를 포함하지 않는 경우
    dfs_subset(idx + 1, subset)


T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = []
    for i in range(1, 13):
        A.append(i)

    result = 0
    dfs_subset(0, [])

    print(f'#{tc} {result}')
