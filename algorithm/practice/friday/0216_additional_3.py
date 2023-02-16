# 재미있는 오셀로 게임
import sys
sys.stdin = open('input.txt', 'r')

def colorChange(r, c, color):
    # 열 체크(같은 색 그 열에 있으면 가장 가까운 놈으로다가 )
    # 행 체크

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    m = N//2
    arr[m-1][m-1], arr[m-1][m], arr[m][m-1], arr[m][m] = 2, 1, 1, 2
    print(arr)
    b, w = 0

    for _ in range(M):
        c, r, color = map(int, input().split())
        arr[r-1][c-1] = color
        colorChange(r-1, c-1, color)
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    w += 1
                elif arr[i][j] == 1:
                    b += 1
    print(f'#{tc} {b} {w}')