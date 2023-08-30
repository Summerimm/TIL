# ACM Craft
import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def topologySort():
    result = []
    q = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, V+1):
        if inDegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 -1
        for i in graph[now]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)

    return result

T = int(input())
for _ in range(T):    
    V, E = map(int, input().split())
    delay = list(map(int, input().split()))
    
    inDegree = [0] * (V+1)
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    result = topologySort()
    print(result)
    print(graph)
    W = int(input())
