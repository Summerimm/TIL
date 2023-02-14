# 간단한 압축풀기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    n = int(input())
    alpha = {}
    for i in range(n):
        c, cnt = map(str, input().split())
        cnt = int(cnt)
        alpha[c] = cnt
    ten = 0
    for k, v in alpha.items():
        ten += v
        if ten > 10:
            print(k * (10 - ten + v))
            q = (ten - 10) // 10
            r = (ten - 10) % 10
            for _ in range(q):
                print(k * 10)
            print(k * r, end='')
            ten = r
        elif ten == 10:
            print(k * v)
            ten = 0
        else:
            print(k * v, end='')
    print()