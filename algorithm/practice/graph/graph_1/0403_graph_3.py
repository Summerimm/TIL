# 연산
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    cnt[v] = 1
    while q:
        v = q.popleft()
        for i in [v+1, v-1, 2*v, v-10]:
            if 0<= i <= 2*M and cnt[i] == 0:
                q.append(i)
                cnt[i] = cnt[v] + 1
                if i == M:
                    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = [0]*2*M
    bfs(N)

    print(f'#{tc} {cnt[M]-1}')