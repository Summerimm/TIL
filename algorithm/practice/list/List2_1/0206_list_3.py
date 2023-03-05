# 2일차 부분집합의 합
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    nums = [x for x in range(1, 13)]
    answer = 0
    
    for i in range(1<<12):
        ans = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                ans += nums[j]
                cnt += 1
        if ans == k and cnt == n:
            answer += 1
        
    print(f'#{t} {answer}')