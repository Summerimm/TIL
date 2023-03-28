# 베이비진
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    cnt = [0] * 10
    t, r = 0, 0

    for i in range(6):
        cnt[num % 10] += 1
        num //= 10

    i = 0
    while (i < 10):
        if cnt[i] >= 3:
            cnt[i] -= 3
            t += 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >=1 and cnt[i+2] >= 1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            r += 1
            continue
        i += 1
    
    if t + r == 2:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')