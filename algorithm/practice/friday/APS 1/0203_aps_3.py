# 연속한 1의 개수
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    seq = input().split('0')
    ans = 0
    for s in seq:
        if len(s) > ans:
            ans = len(s)
    print(f'#{tc+1} {ans}')
