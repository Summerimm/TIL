# 러시아 국기 같은 깃발
import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = 0
    for i in range(M):
        if arr[0][i] != 'W':
            ans += 1
        if arr[-1][i] != 'R':
            ans += 1

    cnt = []
    for j in range(1, N-1):
        wcnt = arr[j].count('B') + arr[j].count('R')    # w를 선택했을 때 채워야 하는 수
        bcnt = arr[j].count('W') + arr[j].count('R')
        rcnt = arr[j].count('W') + arr[j].count('B')
        cnt.append([wcnt, bcnt, rcnt])

    comblst = []
    for i in range(1, N-1):
        for j in range(N-1-i):
            comb = '0' * (N-2-i-j) + '1' * i + '2' * j
            comblst.append(comb)

    alst = []
    for a in comblst:
        tmp = 0
        for i, c in enumerate(a):
            tmp += cnt[i][int(c)]
        alst.append(tmp)

    print(f'#{tc} {min(alst)+ans}')
    
    # 1이 하나일 때
    # 0001 0012 0122 1222
    # 1이 두 개일때
    # 0011 0112 1122
    # 1이 세 개일때
    # 0111 1112
    # 1이 네 개일때
    # 1111

    # 1번째, 마지막번째 빼고
    # 바꾸는 수가 가장 적도록
    # W B R
