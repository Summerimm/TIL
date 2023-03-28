# 화물 도크
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 2 for _ in range(N)]

    for i in range(N):
        arr[i][0], arr[i][1] = map(int, input().split())
    arr = sorted(arr, key=lambda x:x[1])

    cnt = 0
    s, e = 0, 0
    for t in arr:
        if t[0] >= e:
            cnt += 1
            s = t[0]
            e = t[1]
    print(f'#{tc} {cnt}')