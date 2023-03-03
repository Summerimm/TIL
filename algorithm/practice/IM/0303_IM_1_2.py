# 풍선팡
import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N):
        for j in range(M):
            tmp = a = arr[i][j]
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for k in range(1, a+1):
                    ni, nj = i+di*k, j+dj*k
                    if 0<=ni<N and 0<=nj<M:
                        tmp += arr[ni][nj]
            mx = max(mx, tmp)
    print(f'#{tc} {mx}')