# 당근 포장하기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 10000
    for i in range(1, N-1):
        for j in range(i+1, N):
            if i > N//2 or j-i > N//2 or N-j > N//2:
                continue
            if arr[i-1] == arr[i] or arr[j-1] == arr[j]:
                continue
            a, b, c = i, j-i, N-j
            ans = min(ans, max(a, b, c) - min(a, b, c))
    if ans == 10000:
        ans = -1
    print(f'#{tc} {ans}')