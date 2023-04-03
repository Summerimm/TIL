# 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(ci, cj, sm):
    global ans

    pass

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    ans = ''
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    # print(f'#{tc} {ans}')