# 방 배정
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = [0] * 14
for i in range(N):
    s, y = map(int, input().split())
    arr[2*y+s] += 1

ans = 0
for cnt in arr:
    if 0 < cnt <= K:
        ans += 1
    else:
        ans += cnt // K
        if cnt % K != 0:
            ans += 1
print(ans)