import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    anslist = []

    if len(A) >= len(B):
        maxlist = A
        minlist = B
    else:
        maxlist = B
        minlist = A
    q = len(maxlist) - len(minlist) + 1

    for i in range(q): # 0 1
        ans = 0
        for j in range(len(minlist)): # 00 01 02 03 04 05 06 / 10 11 12 13 14 15
            ans += maxlist[j+i] * minlist[j]
        anslist.append(ans)
    print(f'#{tc+1} {max(anslist)}')
