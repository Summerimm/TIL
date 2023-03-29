# 전자카트
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pl, mi, mul, div = map(int, input().split())
    arr = list(map(int, input().split()))

    st = ['+'] * pl + ['-'] * mi + ['*'] * mul + ['/'] * div
    print(st)

    used = [0] * len(st)
    perm(st)