# 전자카트
import sys
sys.stdin = open('input.txt', 'r')

def perm(idx):
    global ans
    if idx == N:
        tmp = 0
        for i in range(N-1):
            tmp += arr[order[i]][order[i+1]]
        tmp += arr[order[N-1]][0]
        ans = min(ans, tmp)
        return
    else:
        for j in range(idx, N):
            order[idx], order[j] = order[j], order[idx]
            perm(idx+1)
            order[idx], order[j] = order[j], order[idx]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = [0] * (N)
    for i in range(N):
        order[i] = i
    ans = 1000
    perm(1)

    print(f'#{tc} {ans}')