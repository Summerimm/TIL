# 진기의 최고급 붕어빵
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    wait = list(map(int, input().split()))
    wait.sort()
    ans = 'Possible'
    for i in range(N):
        if (wait[i]//M)*K < i+1:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')