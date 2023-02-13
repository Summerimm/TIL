# 거듭제곱
import sys
sys.stdin = open('input.txt.', 'r')

def ex(n, t):
    if t == 1:
        return n
    else:
        return n * ex(n, t-1)

for _ in range(10):
    tc = int(input())
    n, t = map(int, input().split())
    ans = ex(n, t)
    print(f'#{tc} {ans}')