# 이진 탐색
import sys
sys.stdin = open('input.txt','r')

def binarySearch(k, l, r):
    prev = 0
    cur = -1
    while l <= r and prev != cur:
        m = (l + r) // 2
        if k == blst[m]:
            return 1
        elif k > blst[m]:
            l = m + 1
            prev = cur
            cur = 1
        elif k < blst[m]:
            r = m - 1
            prev = cur
            cur = 0
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))
    alst.sort()
    blst.sort()

    ans = 0
    for a in alst:
        ans += binarySearch(a, 0, N)
    print(f'#{tc} {ans}')