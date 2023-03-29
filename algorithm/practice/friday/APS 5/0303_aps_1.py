# 농작물 수확하기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    K = N // 2
    ans = 0
    for i in range(N):
        t = abs(K-i)
        for j in range(t, N-t):
            ans += int(arr[i][j])
    print(f'#{tc} {ans}') 