# Magnetic
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    arrt = list(zip(*arr))

    ans = 0
    for c in arrt:
        ans += ''.join(c).replace('0', '').count('12')
    print(f'#{tc} {ans}')