# 중앙값 구하기
import sys
sys.stdin = open('input1.txt', 'r')

n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(q):
    m = int(input())
    if n == 1 or n == 2:
        print(0)
        continue
    if m <= arr[0] or m >= arr[-1] or m not in arr:
        print(0)
    else:
        idx = arr.index(m)
        pre = len(arr[:idx])
        post = len(arr[idx+1:])
        print(pre * post)