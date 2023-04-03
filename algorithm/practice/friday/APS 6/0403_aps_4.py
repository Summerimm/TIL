# 장훈이의 높은 선반
import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, sm):
    global mn
    if sm >= B:
        mn = min(mn, sm)
        return
    if i == N:
        return
    dfs(i+1, sm+arr[i])
    dfs(i+1, sm)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    mn = 200000
    dfs(0, 0)
    print(f'#{tc} {mn-B}')