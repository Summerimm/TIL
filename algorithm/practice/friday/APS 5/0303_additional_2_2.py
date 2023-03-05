# 파리퇴치3
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [[(-1, 0), (1, 0), (0, -1), (0, 1)], [(-1, -1), (-1, 1), (1, 1), (1, -1)]]
    # dr[0]: plus, dr[1]: x
    ans = 0
    for p in range(2):
        for i in range(N):
            for j in range(N):
                tmp = arr[i][j]
                for di, dj in dr[p]:
                    for m in range(1, M):
                        if 0<=i+di*m<N and 0<=j+dj*m<N:
                            tmp += arr[i+di*m][j+dj*m]
                ans = max(tmp, ans)
    print(f'#{tc} {ans}')