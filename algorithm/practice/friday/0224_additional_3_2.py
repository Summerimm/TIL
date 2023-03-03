# 홈 방범 서비스
import sys
sys.stdin = open('input.txt', 'r')

cost = [(((k*k)+(k-1)*(k-1))) for k in range(40)]
def bfs(si, sj):
    q = []
    v = [[0]*N for _ in range(N)]
    old = 0
    mx = 0
    
    q.append((si, sj))
    v[si][sj] = 1
    cnt = arr[si][sj]

    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]:    # k값이 달라진 경우
            old = v[ci][cj]
            if cost[v[ci][cj]] <= cnt * M:
                mx = max(mx, cnt)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += arr[ni][nj]
    return mx

def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N):     # 가능한 모든 시작 위치
            mx = max(mx, bfs(si, sj))
    return mx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve_bfs()
    print(f'#{tc} {ans}')