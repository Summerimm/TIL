# 정사각형 방
import sys
sys.stdin = open('input.txt', 'r')

def bfs(si, sj):
    q = [(si, sj)]
    roomlst = [arr[si][sj]]
    visited[si][sj] = 1
    while q:
        ti, tj = q.pop(0)
        for di, dj in  [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<N and 0<=nj<N and abs(arr[ti][tj] - arr[ni][nj]) == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                roomlst.append(arr[ni][nj])
                visited[ni][nj] = 1         # 방문 처리
    return min(roomlst), len(roomlst)       # 루트를 하나 찾고 그 루트에서 가장 작은 값, 길이 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    cnt, num = 0, N*N
    for i in range(N):
        for j in range(N):
            tnum, tcnt = bfs(i, j)
            if tcnt > cnt or (tcnt == cnt and tnum < num):
                cnt, num = tcnt, tnum
    print(f'#{tc} {num} {cnt}')