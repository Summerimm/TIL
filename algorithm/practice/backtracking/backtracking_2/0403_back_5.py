# 동철이의 일 분배
import sys
sys.stdin = open('input.txt', 'r')

def dfs(cnt, tmp):
    global ans
    if tmp <= ans:
        return
    if cnt == N:
        ans = max(ans, tmp)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(cnt+1, tmp * (arr[cnt][i] / 100))
            v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N+1)
    ans = 0
    dfs(0, 1)
    print(f'#{tc} {ans * 100:.6f}')