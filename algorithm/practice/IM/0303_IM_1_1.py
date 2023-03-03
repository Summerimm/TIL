# 풍선팡
import sys
sys.stdin = open('input.txt', 'r')

def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(M):
            k = arr[si][sj]
            tmp = 0
            for i in range(si-k, si+k+1):
                if 0<=i<N:
                    tmp += arr[i][sj]
            for j in range(sj-k, sj+k+1):
                if 0<=j<M:
                    tmp += arr[si][j]
            tmp -= arr[si][sj]
            mx = max(mx, tmp)
    return mx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solve_loop()
    print(f'#{tc} {ans}')
