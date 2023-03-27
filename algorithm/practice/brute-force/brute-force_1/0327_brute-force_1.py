# 2일차 - 최소합

import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j, value):
    global ans
    if value > ans:
        return
    for di, dj in [(0, 1), (1, 0)]:
        ci, cj = i+di, j+dj
        if ci == N-1 and cj == N-1:
            value += arr[ci][cj]
            ans = min(ans, value)
            return
        elif 0<=ci<N and 0<=cj<N and visited[ci][cj] == 0:
            value += arr[ci][cj]
            visited[ci][cj] = 1
            dfs(ci, cj, value)
            value -= arr[ci][cj]
            visited[ci][cj] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 1000

    visited[0][0] = 1
    value = arr[0][0]
    dfs(0, 0, value)


    print(f'#{tc} {ans}')