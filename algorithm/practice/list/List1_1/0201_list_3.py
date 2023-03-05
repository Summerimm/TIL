# Gravity
T = int(input())
for tc in range(T):
    n = int(input())
    boxes = list(map(int, input().split()))

    anslist = []
    for i in range(n):
        ans = 0
        for j in range(i, n):
            if boxes[i] > boxes[j]:
                ans += 1
        anslist.append(ans)

    if anslist == []:
        ans = 0
    else:
        ans = max(anslist)
    print(f'#{tc+1} {ans}')