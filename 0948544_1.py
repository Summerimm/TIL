import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    apple = [(0, 0)] + [0] * 11
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                apple[arr[i][j]] = (i, j)

    req = [(3, 3, 2, 1), (1, 3, 3, 2), (2, 1, 3, 3), (3, 2, 1, 3)]
    dr = 0   # 현재 화살표
    prev = 0        # 이전 사과 좌표
    cur = 1         # 앞으로의 사과 좌표
    # 우상/우하/좌하/좌상 4가지 경우를 나누어 방향 바꿀 때마다 +1
    while apple[cur] != 0:
        pi, pj = apple[prev][0], apple[prev][1]
        ci, cj = apple[cur][0], apple[cur][1]
        if ci < pi and cj > pj:     # 우상
            # 우, 상(0, 3)
            ans += req[0][dr]
            if dr == 0:
                dr = 3
            else:
                dr = 0
        elif ci > pi and cj > pj:   # 우하
            # 우, 하(0, 1)
            ans += req[1][dr]
            if dr == 1:
                dr = 0
            else:
                dr = 1
        elif ci > pi and cj < pj:   # 좌하
            # 좌, 하(2, 1)
            ans += req[2][dr]
            if dr == 2:
                dr = 1
            else:
                dr = 2
        elif ci < pi and cj < pj:   # 좌상
            # 좌, 상(2, 3)
            ans += req[3][dr]
            if dr == 3:
                dr = 2
            else:
                dr = 3
        prev += 1
        cur += 1


    print(f'#{tc} {ans}')