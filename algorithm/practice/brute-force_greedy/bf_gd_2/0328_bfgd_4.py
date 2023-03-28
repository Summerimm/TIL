# 최소 생산 비용
import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, cnt):
    global m
    if r == N:
        if cnt < m:
            m = cnt
        return
    elif cnt >= m:
        return
    else:
        for c in range(N):
            if not v[c]:
                v[c] = 1
                dfs(r + 1, cnt + arr[r][c])
                v[c] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    m = 99 * 15
    v = [0] * N
    dfs(0, 0)
    print(f'#{tc} {m}')