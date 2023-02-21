# 노드의 거리
import sys
sys.stdin = open('input.txt', 'r')

def bfs(v):
    q = [v]
    visited[v] = 0
    while q:
        t = q.pop(0)
        for i in adjL[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1)
    S, G = map(int, input().split())
    bfs(S)
    print(f'#{tc} {visited[G]}')