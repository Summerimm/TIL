# 회문
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    slist = []
    for _ in range(n):
        slist.append(list(input()))

    # 가로 회문(s1), 세로 회문(s2)
    ans, s1, s2 = '', '', ''
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m):
                s1 += slist[i][j + k]
                s2 += slist[j + k][i]
            if s1 == s1[::-1]:
                ans = s1
            if s2 == s2[::-1]:
                ans = s2
            s1, s2 = '', ''
    print(f'#{tc} {ans}')