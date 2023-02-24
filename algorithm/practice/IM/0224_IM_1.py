# 직사각형과 점
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    incnt, oncnt, outcnt = 0, 0, 0
    for a, b in arr:
        if x1< a < x2 and y1 < b < y2:
            incnt += 1
        elif x1 <= a <= x2 and (b == y1 or b == y2) or y1 <= b <= y2 and (a == x1 or a == x2):
            oncnt += 1
        else:
            outcnt += 1
    print(f'#{tc} {incnt} {oncnt} {outcnt}')