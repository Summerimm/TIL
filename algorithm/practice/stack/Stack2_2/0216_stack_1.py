# 부분집합
import sys
sys.stdin = open('input.txt', 'r')

def subsetSum(i, k, s, t): 
    # i: 현재 원소, k: 집합의 원소 개수, s: i-1까지의 합, t: target sum
    global ans
    if s == t:    # 남은 원소를 고려할 필요X
        ans += 1
        return
    elif s > t:     # 원소의 합이 target sum보다 큼(남은 원소 고려할 필요X)
        return
    elif i == k:      # 모든 원소 고려됨
        return
    else:
        subsetSum(i+1, k, s+arr[i], t)      # arr[i] 포함
        subsetSum(i+1, k, s, t)             # arr[i] 미포함


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    subsetSum(0, N, 0, K)
    print(f'#{tc} {ans}')