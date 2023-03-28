# 배열 최소 합
import sys
sys.stdin = open('input.txt', 'r')

def dfs(s, cnt):
    global m
    if cnt > m:
        return m
    if s == N - 1:
        return cnt
    for k in range(N):
        if visited[k] == 0:
            cnt += arr[s + 1][k]
            visited[k] = 1
            m = min(m, dfs(s + 1, cnt))
            cnt -= arr[s + 1][k]
            visited[k] = 0
    return m

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    m = 100

    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        dfs(0, arr[0][i])

    print(f'#{tc} {m}')