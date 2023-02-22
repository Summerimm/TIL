# 미로1
import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):
    visited[si][sj] = 1
    q = [(si, sj)]
    while q:
        t = q.pop(0)
        for k in range(4):
            ci, cj = t[0] + di[k], t[1] + dj[k]
            if 0<=ci<N and 0<=cj<N and arr[ci][cj] == '0' and visited[ci][cj] == 0:
                q.append((ci, cj))
                visited[ci][cj] = 1
            if 0<=ci<N and 0<=cj<N and arr[ci][cj] == '3':
                visited[ci][cj] = 1
                break

T = 10
N = 16
for tc in range(1, T+1):
    tc = int(input())
    arr = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            if arr[i][j] == '3':
                ei, ej = i, j
    bfs(si, sj)
    print(f'#{tc} {visited[ei][ej]}')