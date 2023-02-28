# 16진수의 십진수 출력
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    hex = input()
    ans = ''
    for h in hex:
        ans += bin(int(h, 16)).replace('0b', '').zfill(4)
    res = [int(ans[i:i+7], 2) for i in range(0, len(ans), 7)]
    print(f'#{tc}', *res)