# 보급로
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    q = [(0, 0)]
    v = [[90000] * N for _ in range(N)]
    v[0][0] = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
                q.append((ni, nj))
    print(f'#{tc} {v[-1][-1]}')