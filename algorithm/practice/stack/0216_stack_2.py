# 부분집합의 합
import sys
sys.stdin = open('input.txt', 'r')

def subsetSum(i, k, s, t, l):
    # l: 부분집합의 크기
    global ans
    if s > t:
        return
    elif s == t:        # 합이 target sum과 동일
        if l == N:      # 부분집합의 크기도 N과 같음
            ans += 1
            return
        else:           # 부분집합의 크기가 N이 아님
            return
    elif i == k:
        return
    else:
        subsetSum(i+1, k, s+A[i], t, l+1)
        subsetSum(i+1, k, s, t, l)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [n for n in range(1, 13)]
    ans = 0
    l = 0
    subsetSum(0, 12, 0, K, 0)
    print(f'#{tc} {ans}')