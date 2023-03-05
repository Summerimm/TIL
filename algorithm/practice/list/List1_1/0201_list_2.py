# [파이썬 S/W 문제해결 기본] 1일차 - 구간합
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    sumvalue = []
    for i in range(n - m + 1):
        sumvalue.append(sum(a[i:i+m]))

    ans = max(sumvalue) - min(sumvalue)
    print(f'#{tc+1} {ans}')