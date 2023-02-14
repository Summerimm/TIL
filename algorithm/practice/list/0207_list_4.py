import sys
sys.stdin = open('input.txt', 'r')

def binarySearch(n, target):
    start = 1
    end = n
    cnt = 1
    while start <= end:
        mid = (start + end) // 2
        if mid == target:
            return cnt
        elif mid < target:
            start = mid
            cnt += 1
        elif mid > target:
            end = mid
            cnt += 1
        
T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    cnta = binarySearch(P, A)
    cntb = binarySearch(P, B)

    if cnta > cntb:
        win = 'B'
    elif cnta < cntb:
        win = 'A'
    else:
        win = 0
    print(f'#{tc} {win}')