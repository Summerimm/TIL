# [S/W 문제해결 기본] 1일차 - View
for tc in range(10):
    n = int(input())
    numlist = list(map(int, input().split()))
    ans = 0
    for i in range(2, len(numlist)-2):
        a = max(numlist[i - 2: i])
        b = max(numlist[i + 1:i + 3])
        if numlist[i] > max(a, b):
            ans += numlist[i] - max(a, b)

    print(f'#{tc+1} {ans}')