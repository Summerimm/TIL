# 깊이우선탐색
import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    for w in range(2, E):
        if adjM[v][w] == 1 and visited[w] == 0:
            visited[w] = 1
            print(w, end=' ')
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] * E for _ in range(E)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
    visited = [0] * E
    visited[1] = 1

    print(f'#{tc} 1', end=' ')
    dfs(1)
    print()
