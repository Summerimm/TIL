# 미로의 거리
import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):
    visited[si][sj] = 0
    q = [(si, sj)]
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ci, cj = i + di[k], j + dj[k]
            if 0<=ci<N and 0<=cj<N and arr[ci][cj] == '0' and visited[ci][cj] == 0:
                q.append((ci, cj))
                visited[ci][cj] = visited[i][j] + 1
            if 0<=ci<N and 0<=cj<N and arr[ci][cj] == '3':
                visited[ci][cj] = visited[i][j]
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            if arr[i][j] == '3':
                ei, ej = i, j
    bfs(si, sj)
    print(f'#{tc} {visited[ei][ej]}')