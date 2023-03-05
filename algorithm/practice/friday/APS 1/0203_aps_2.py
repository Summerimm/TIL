# 간단한 소인수분해
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while(n != 1):
        if n % 11 == 0:
            e += 1
            n //= 11
        elif n % 7 == 0:
            d += 1
            n //= 7
        elif n % 5 == 0:
            c += 1
            n //= 5
        elif n % 3 == 0:
            b += 1
            n //= 3
        elif n % 2 == 0:
            a += 1
            n //= 2

    print(f'#{tc+1} {a} {b} {c} {d} {e}')