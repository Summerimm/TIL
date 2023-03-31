# 최대 상금
import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, num):
    global ans
    real = int(''.join(num))

    # 가지치기
    if (i, real) in check:
        return
    
    check.add((i, real))

    # 종료조건
    if i == K:
        ans = max(ans, real)
        return

    for j in range(len(num)-1):
        for k in range(j+1, len(num)):
            num[j], num[k] = num[k], num[j]
            dfs(i+1, num)
            num[j], num[k] = num[k], num[j]

T = int(input())
for tc in range(1, T+1):
    prize, K = map(int, input().split())
    prize = list(str(prize))
    check = set()
    ans = 0

    dfs(0, prize)
    print(f'#{tc} {ans}')