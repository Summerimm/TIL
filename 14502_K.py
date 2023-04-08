# 연구소
import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint
from collections import deque
from copy import deepcopy

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

def bfs():
    global ans
    q = deque()
    tarr = deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if tarr[i][j] == 2:
                q.append((i, j))
    
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and tarr[ni][nj] == 0:
                tarr[ni][nj] = 2
                q.append((ni, nj))
    
    tmp = 0
    for i in range(N):
        tmp += tarr[i].count(0)
    ans = max(ans, tmp)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 브루트포스로 벽 세우기
# bfs로 안전지역 확인
ans = 0
wall(0)
print(ans)