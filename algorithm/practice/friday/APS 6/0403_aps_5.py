# 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(ci, cj, s):
    if len(s) == 7:
        ans.add(s)
        return
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci+di, cj+dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(ni, nj, s+arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f'#{tc} {len(ans)}')