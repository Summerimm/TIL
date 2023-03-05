# 현주의 상자 바꾸기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    n, q = map(int, input().split())
    ans = [0] * n
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            ans[j] = i + 1
    print(f'#{tc+1}', *ans)
