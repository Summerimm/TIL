# 컨테이너 운반
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    used = [0] * N      # 실었는지 여부

    ans = 0
    for i in range(M):
        for j in range(N):
            if t[i] >= w[j] and not used[j]:
                ans += w[j]
                used[j] = 1
                break
        
    print(f'#{tc} {ans}')