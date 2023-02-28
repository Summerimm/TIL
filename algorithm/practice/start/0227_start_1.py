# 이진수
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    _, st = input().split()
    ans = ''
    for c in st:
        if c.isdigit():
            n = int(c)
        else:
            n = ord(c) - ord('A') + 10
        for pos in (3, 2, 1, 0):
            ans += str(1 & (n>>pos))
    print(f'#{tc} {ans}')