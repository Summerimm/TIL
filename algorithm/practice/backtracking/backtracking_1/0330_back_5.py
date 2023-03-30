# 최소합
import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, j, sm):
    global mn
    if i == N or j == N:
        return
    if sm >= mn:
        return
    if i == N-1 and j == N-1:
        mn = sm
        return
    
    dfs(i+1, j, sm+arr[i][j])
    dfs(i, j+1, sm+arr[i][j])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = 300

    dfs(0, 0, 0)
    mn += arr[N-1][N-1]
    print(f'#{tc} {mn}')