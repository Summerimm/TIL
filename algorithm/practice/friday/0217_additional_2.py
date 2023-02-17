# 우주선착륙2
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 행, 열
    arr = [[100] * (M+2)] + [[100] + list(map(int, input().split())) + [100] for _ in range(N)] + [[100] * (M+2)]   # padding

    di = [-1, -1, -1, 0, 1, 1, 1, 0] # 좌상단 부터 시계방향
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]

    ans = 0     # 후보지 개수
    for i in range(1, N+1):
        for j in range(1, M+1):
            mid = arr[i][j] # 착륙지점
            cnt = 0         # 착륙지점 높이보다 낮은 주변 지점 개수
            for k in range(8):
                if arr[i+di[k]][j+dj[k]] < mid:
                    cnt += 1
            if cnt >= 4:    # 후보지 조건 충족
                ans += 1
    print(f'#{tc} {ans}')