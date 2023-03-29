# 전자카트
import sys
sys.stdin = open('input.txt', 'r')

def dfs(k, cnt):
    global ans  
    if cnt > ans:
        return ans
    for j in range(1, N):
        if 0 not in v:
            return cnt + arr[k][0]
        if not v[j]:
            v[j] = 1
            ans = min(ans, dfs(j, cnt + arr[k][j]))
            v[j] = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 5000
    for i in range(1, N):
        v = [0] * N
        v[0] = 1
        v[i] = 1
        dfs(i, arr[0][i])
        v[i] = 0
    print(f'#{tc} {ans}')