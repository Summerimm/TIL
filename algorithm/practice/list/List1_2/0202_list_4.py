# [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    cnt = [0] * 10
    maxnum, maxcnt = 0, 0
    numlist = []
    # 입력 받은 숫자 배열에 넣기
    for c in input():
        numlist.append(int(c))
    # 빈도수 배열 cnt
    for num in numlist:
        cnt[num] += 1
    # maxcnt, maxcnt보다 크거나 같으면 교체
    for idx, c in enumerate(cnt):
        if c >= maxcnt:
            maxnum = idx
            maxcnt = c
    print(f'#{tc+1} {maxnum} {maxcnt}')