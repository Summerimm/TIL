# 요리사
import sys
sys.stdin = open('input.txt', 'r')

def dfs(a, cnt):
    global ans
    if cnt == n // 2:
        tmp = comb()
        ans = min(ans, tmp)
        return
    for j in range(a+1, n):
        v[j] = 1
        dfs(j, cnt+1)
        v[j] = 0

def comb():
    afood = []
    bfood = []
    for i in range(n):
        if v[i] == 1:
            afood.append(i)
        else:
            bfood.append(i)
    return abs(calc(afood) - calc(bfood))

def calc(lst):
    sm = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            sm += arr[lst[i]][lst[j]]
    return sm

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    ans = 1e9
    for i in range(n-1):
        for j in range(i, n):
            d = arr[i][j] + arr[j][i]
            arr[i][j], arr[j][i] = d, d
    dfs(-1, 0)
    
    print(f'#{tc} {ans}')