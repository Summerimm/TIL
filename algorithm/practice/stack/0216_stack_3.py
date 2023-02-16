# 배열 최소 합
import sys
sys.stdin = open('input.txt', 'r')

def back(r, cs):
    global ms
    # r = 행, N = 전체 크기, cs = 현재까지의 합
    if r == N:
        if cs < ms:
            ms = cs
        return
    elif cs >= ms: # 현재까지의 합이 최소합보다 큼
        return
    else:
        for c in range(N):
            if v[c] == 0: # 미방문
                v[c] = 1 # 방문처리
                back(r+1, cs + arr[r][c])
                v[c] = 0 # 초기화
    return ms

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0] * N
    ms = 10000
    print(f'#{tc} {back(0, 0)}')