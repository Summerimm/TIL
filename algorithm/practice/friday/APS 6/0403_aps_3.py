# 수영장
import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, sm):
    global ans
    if sm > ans:
        return
    if i > 11:
        ans = min(ans, sm)
        return
    else:
        if arr[i] >= 1:
            dfs(i + 1, sm + (arr[i]*day))
            dfs(i + 1, sm + month)
            dfs(i + 3, sm + three)
        else:
            dfs(i+1, sm)


T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = year
    dfs(0, 0)
    print(f'#{tc} {ans}')