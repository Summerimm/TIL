# 전자카트
import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, sm, cnt):
    global ans
    # 가지치기
    if sm >= ans:
        return
    # 종료조건
    if cnt == N-1:
        ans = min(ans, sm + arr[i][0])
        return
    # 매번 실행
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(j, sm+arr[i][j], cnt+1)
            v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        arr[i][i] = 5000
    
    ans = 5000
    v = [0] * N
    v[0] = 1
    dfs(0, 0, 0)

    print(f'#{tc} {ans}')