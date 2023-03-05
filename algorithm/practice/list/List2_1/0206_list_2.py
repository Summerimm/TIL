# 부분집합 합

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    flag = 0
    for i in range(1, 1<<10):
        ans = 0
        for j in range(10):
            if i & (1<<j):
                ans += nums[j]
        if ans == 0:
            flag = 1
        if flag:
            break
    print(f'#{t} {flag}')