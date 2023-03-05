# 탈주범 검거
import sys
sys.stdin = open('input.txt', 'r')

dct = {0:[], 1:[(-1, 0), (1, 0), (0, -1), (0, 1)], 2:[(-1, 0), (1, 0)], 3:[(0, -1), (0, 1)],
        4:[(-1, 0), (0, 1)], 5:[(1, 0), (0, 1)], 6:[(1, 0), (0, -1)], 7:[(-1, 0), (0, -1)]}
def bfs(si, sj):
    visited[si][sj] = 1
    q = [(si, sj)]
    cnt = 1
    while q:
        ti, tj = q.pop(0)
        for di, dj in dct[arr[ti][tj]]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 0 and visited[ni][nj] == 0 and (-di, -dj) in dct[arr[ni][nj]]:
                if visited[ti][tj] + 1 > L:
                    return cnt
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, si, sj, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = bfs(si, sj)
    print(f'#{tc} {ans}')