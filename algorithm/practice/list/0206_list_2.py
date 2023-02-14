# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.

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