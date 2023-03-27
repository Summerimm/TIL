# 파이프 옮기기1
import sys
sys.stdin = open('input.txt', 'r')

def dfs(pi, pj, si, sj):
    global cnt
    if si == N-1 and sj == N-1:
        cnt += 1
        return 
    
    if pi == si:    # 가로
        if sj == N-1:   # 가로인데 이미 열은 도착해버림(방법X)
            return
        elif sj+1<N and arr[si][sj+1] != 1:
            dfs(si, sj, si, sj+1)           # 가로
        elif si+1<N and si+1<N and arr[si][sj+1] != 1 and arr[si+1][sj+1] != 1 and arr[si+1][sj] != 1:
            dfs(si, sj, si+1, sj+1)         # 대각선
    elif pj == sj:  # 세로
        if si == N-1:   # 세로인데 이미 행은 도착해버림(방법X) 
            return
        if sj+1<N and arr[si+1][sj] != 1:
            dfs(si, sj, si+1, sj)           # 세로
        if si+1<N and si+1<N and arr[si][sj+1] != 1 and arr[si+1][sj+1] != 1 and arr[si+1][sj] != 1:
            dfs(si, sj, si+1, sj+1)         # 대각선
    elif si - pi == 1 and sj - pj == 1:           # 대각선
        if sj+1<N and arr[si][sj+1] != 1:
            dfs(si, sj, si, sj+1)           # 가로
        if sj+1<N and arr[si+1][sj] != 1:
            dfs(si, sj, si+1, sj)           # 세로
        if si+1<N and si+1<N and arr[si][sj+1] != 1 and arr[si+1][sj+1] != 1 and arr[si+1][sj] != 1:
            dfs(si, sj, si+1, sj+1)         # 대각선
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
pi, pj, si, sj = 0, 0, 0, 1
ans = dfs(pi, pj, si, sj)
print(cnt)