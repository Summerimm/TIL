import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            si, sj = i, j
            tmp = arr[si][sj]
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                for k in range(1, P+1):
                    ti, tj = si+di*k, sj+dj*k
                    if 0<=ti<N and 0<=tj<N:
                        tmp += arr[ti][tj]
            ans = max(ans, tmp)

    print(f'#{tc} {ans}')