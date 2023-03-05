# [파이썬 S/W 문제해결 기본] 1일차 - min max
T = int(input())
for tc in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    print(f'#{tc+1} {max(a)-min(a)}')