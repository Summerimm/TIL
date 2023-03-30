# N-Queen
import sys
sys.stdin = open('input.txt', 'r')

def promising(i, j):
    for di, dj in [(-1, -1), (-1, 0), (-1, 1)]: # 왼쪽 위 대각, 같은 행, 오른쪽 위 대각
        ni, nj = i+di, j+dj
        while 0<=ni<N and 0<=nj<N:
            if board[ni][nj]:       # 다른 퀸이 있으면
                return 0            # 실패
            ni, nj = ni+di, nj+dj   # 위로 올라가며 각 부분 계속 체크
    return 1

def dfs(i):
    global cnt
    if i == N:
        cnt += 1    # 마지막 퀸을 놓음
    else:
        for j in range(N):
            if promising(i, j): # 가능하면
                board[i][j] = 1
                dfs(i+1)
                board[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    board = [[0] * N for _ in range(N)]
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')