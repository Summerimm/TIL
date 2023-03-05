# 홈 방범 서비스
import sys
sys.stdin = open('input.txt', 'r')

cost = [(k*k+(k-1)*(k-1)) for k in range(40)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    home = []
    for si in range(N):
        for sj in range(N):
            if arr[si][sj] == 1:
                home.append((si, sj))
    
    ans = 0
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            for di, dj in home:
                t = abs(si - di) + abs(sj - dj) + 1
                dist[t] += 1
            
            for k in range(1, 40):
                dist[k] += dist[k-1]
                if cost[k] <= dist[k]*M:
                    ans = max(ans, dist[k])
    print(f'#{tc} {ans}')