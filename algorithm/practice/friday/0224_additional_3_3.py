# 홈 방범 서비스
import sys
sys.stdin = open('input.txt', 'r')

cost = [(((k*k)+(k-1)*(k-1))) for k in range(40)]
def solve_idea():
    mx = 0
    home = []
    for si in range(N):
        for sj in range(N):     # 집의 모든 위치를 저장
            if arr[si][sj] == 1:
                home.append((si, sj))
    
    # 각 기준위치에서 거리 별 집의 개수 누적하기
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            # 거리 별 집 위치를 누적
            for ti, tj in home:
                t = abs(si-ti) + abs(sj-tj) + 1
                dist[t] += 1

            for k in range(1, 40):
                dist[k] += dist[k-1]
                if cost[k] <= dist[k] * M:
                    mx = max(mx, dist[k])
    return mx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve_idea()
    print(f'#{tc} {ans}')