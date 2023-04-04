# 최단경로(Dijkstra)
import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(s, e):
    # D table, v[] 생성 및 시작위치 방문 표시
    D = adjM[s][::]
    v = [0] * N
    v[s] = 1

    # N-1개 노드에 대해서 반복처리
    for _ in range(N-1):
        # 미방문 노드 중 기준노드(최소 비용으로 연결 가능한 노드) 찾기
        mn, i_min = INF, 0
        for j in range(N):
            if v[j] == 0 and mn > D[j]:
                mn, i_min = D[j], j
        v[i_min] = 1    # 기준 노드 방문처리

        # 모든 노드에 대해서 최소비용 갱신
        for j in range(N):
            D[j] = min(D[j], D[i_min] + adjM[i_min][j])
    
    return D[e]

INF = 500
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[INF] * N for _ in range(N)]
    for i in range(N):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    ans = dijkstra(0, N-1)
    print(f'#{tc} {ans}')