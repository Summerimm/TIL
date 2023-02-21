# 연습문제_1: 너비우선탐색
import sys
sys.stdin = open('input.txt', 'r')

def bfs(v, N):
    visited = [0] * (N+1)   # visited 배열 생성
    q = [v]                 # q 생성, 초기지점 인큐
    visited[v] = 1          # 인큐 처리
    while q:                # 큐가 남아있는 동안
        t = q.pop(0)        # 첫 번째 원소 반환
        print(t, end=' ')
        for i in adjL[t]:   # 인접한
            if not visited[i]:  # 방문하지 않은 지점
                q.append(i)     # q에 넣기
                visited[i] = visited[t] + 1 # 인큐 + 1
    print()

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} ', end='')
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1)
    bfs(1, V)