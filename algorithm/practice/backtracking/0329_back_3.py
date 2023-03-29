# 전기버스2
import sys
sys.stdin = open('input.txt', 'r')

def dfs(start, cnt):
    global mn
    if cnt > mn:
        return mn
    if start >= N-1:
        return cnt-1
    else:
        for i in range(arr[start]+1, 0, -1):
            mn = min(mn, dfs(start+i, cnt + 1))
    return mn

T = int(input())
for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    mn = 50

    print(f'#{tc}', dfs(0, 0))