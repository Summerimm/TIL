# 숫자 만들기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(cnt, sm):
    global mx, mn
    if cnt == N-1:
        if mx < sm:
            mx = sm
        if mn > sm:
            mn = sm
        return
    for j in range(4):
        if card[j] > 0:
            card[j] -= 1
            if j == 0:
                ans = sm + arr[cnt+1]
            elif j == 1:
                ans = sm - arr[cnt+1]
            elif j == 2:
                ans = sm * arr[cnt+1]
            else:
                ans = int(sm / arr[cnt+1])
            dfs(cnt+1, ans)
            card[j] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mx, mn = -1e9, 1e9

    dfs(0, arr[0])
    print(f'#{tc} {mx-mn}')
    