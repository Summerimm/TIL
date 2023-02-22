# 이진탐색
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    root = N // 2 + 1
    tree = [0] * (N+1)
    
    # print(f'#{tc} {root} {ans}')