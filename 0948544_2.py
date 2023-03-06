import sys
sys.stdin = open('input2.txt', 'r')

def jump(si, sj, di, dj):
    ni = si + di
    nj = sj + dj
    while 0<=ni<N and 0<=nj<N:
        if arr[ni][nj] == 1:
            return ni, nj
        ni += di
        nj += dj
    return 0

def dfs(si, sj, cnt):
    global ans
    st = [(si, sj)]
    ni, nj = si, sj
    visited = [[0] * N for _ in range(N)]
    # visited[si][sj] = 1

    while True:
        if cnt == 3 or ni < 0 or ni >= N or nj < 0 or nj >= N:
            if st:
                ni, nj = st.pop()
                cnt -= 1
            else:
                return
        else:
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp = jump(ni, nj, di, dj)
                if tmp != 0:
                    jumpi, jumpj = tmp[0], tmp[1]     # 포가 넘어갈 좌표
                else:
                    continue
                ni, nj = jumpi + di, jumpj + dj               # 포가 이동할 좌표
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0: # 이동할 좌표가 1
                    cnt += 1
                    ans += 1
                    st.append((ni, nj))
                    visited[ni][nj] = 1
                    break
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == 0:   # 이동할 좌표가 0
                    cnt += 1
                    st.append((ni, nj))
                    visited[ni][nj] = 1
                    break
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break
    ans = 0
    cnt = 0
    ans = dfs(si, sj, 0)
    print(f'#{tc} {ans}')