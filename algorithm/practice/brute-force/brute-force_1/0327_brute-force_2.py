# 2일차 - 부분집합의 합
import sys
sys.stdin = open('input.txt', 'r')

def perm(idx, m, cur):     # i: 선택된 원소의 수, m: 현재 가장 큰 수
    global ans
    if cur > K:
        return
    elif idx == N:
        if cur == K:
            ans += 1
            return
        else:
            return
    else:
        for j in range(m+1, 13):
            if not used[j]:
                arr[idx] = j
                used[j] = 1
                cur += j
                perm(idx+1, j, cur)
                used[j] = 0
                cur -= j

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [0] * N
    used = [0] * 13
    ans = 0
    perm(0, 0, 0)

    print(f'#{tc} {ans}')