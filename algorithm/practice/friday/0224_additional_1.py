# Contact
import sys
sys.stdin = open('input.txt', 'r')

def bfs(s):
    visited[s] = 1
    q = [s]
    while q:
        t = q.pop(0)
        for c in ctc[t]:
            if visited[c] == 0:
                visited[c] = visited[t] + 1
                q.append(c)

T = 10
for tc in range(1, T+1):
    N, s = map(int, input().split())
    ctc = [[] for _ in range(101)]
    lst = list(map(int, input().split()))
    visited = [0] * 101
    for i in range(N//2):
        ctc[lst[2*i]].append(lst[2*i+1])
    bfs(s)
    for idx, v in enumerate(visited):
        if v == max(visited):
            ans = idx
    print(f'#{tc} {ans}')