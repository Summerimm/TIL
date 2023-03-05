# 미로2
import sys
sys.stdin = open('input.txt', 'r')

def bfs(si, sj):
    q = [(si, sj)]
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1

    while q:
        ti, tj = q.pop(0)
        for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
            ni, nj = ti + di, tj + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] != '1':
                if arr[ni][nj] == '3':
                    return 1
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 0

T = 10
for tc in range(1, T+1):
    _ = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            if arr[i][j] == '3':
                ei, ej = i, j
    ans = bfs(si, sj)
    print(f'#{tc} {ans}')