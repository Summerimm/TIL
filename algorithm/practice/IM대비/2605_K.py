# 줄 세우기
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
ans = [0] * (N-1) + [1]

for i in range(1, N):
    k = arr[i]
    if k == 0:
        ans.append(i+1)
    else:
        ans[-i-1:-k-1] = ans[-i:-k]
        ans[-k-1] = i+1
for a in ans:
    if a != 0:
        print(a, end=' ')
print()