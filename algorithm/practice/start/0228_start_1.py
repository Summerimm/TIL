# 이진수의 십진수 출력
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    hex = input()
    for i in range(len(hex) // 7):
        tmp = hex[7*i:7*i+7]
        print(int(tmp, 2), end=' ')
    print()