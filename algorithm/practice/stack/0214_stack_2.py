# 종이붙이기
import sys
sys.stdin = open('input.txt', 'r')

# DP로 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N //= 10
    lst = [0] * (N+1)
    lst[1], lst[2] = 1, 3
    for i in range(3, N+1):
        lst[i] = lst[i-2] * 2 + lst[i-1]
    print(f'#{tc} {lst[N]}')