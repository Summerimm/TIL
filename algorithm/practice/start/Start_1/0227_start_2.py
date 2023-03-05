# 이진수2
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    f = float(input())
    ans = ''
    while f > 0.0:
        f *= 2
        if f >= 1.0:
            ans += '1'
            f -= 1.0
        else:
            ans += '0'
        if len(ans) > 12:
            ans = 'overflow'
            break
    print(f'#{tc} {ans}')