# 최소 신장 트리
import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    rep = [i for i in range(V+1)]
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append([w, n1, n2])
    graph.sort()

    cnt, ans = 0, 0
    for w, n1, n2 in graph:
        if find_set(n1) != find_set(n2):
            cnt += 1
            ans += w
            union(n1, n2)
            if cnt == V:
                break
    print(f'#{tc} {ans}')