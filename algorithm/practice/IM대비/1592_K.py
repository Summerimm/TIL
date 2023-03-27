# 영식이와 친구들
import sys
sys.stdin = open('input.txt', 'r')

N, M, L = map(int, input().split())
arr = [0] * (N+1)
arr[1] = 1
s = 1

while M not in arr:
    if arr[s] % 2:
        s -= L % N
        if s < 1:
            s += N
    else:
        s += L % N
        if s > N:
            s -= N
    arr[s] += 1
print(sum(arr) - 1)