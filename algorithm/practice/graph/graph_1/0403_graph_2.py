# 너비우선탐색
import sys
sys.stdin = open('input.txt', 'r')

def bfs(v):
    q = [v]
    visited = [0] * E
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in range(2, E):
            if adjM[v][w] == 1 and visited[w] == 0:
                print(w, end=' ')
                visited[w] = 1
                q.append(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] * E for _ in range(E)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
    print(f'#{tc} 1', end=' ')
    bfs(1)
    print()
