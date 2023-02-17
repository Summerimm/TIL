# 베이비진 게임
import sys
sys.stdin = open('input.txt', 'r')

# Counting Sort
T = int(input())
for tc in range(T):
    num = int(input())
    cnt = [0] * 10
    tri, runn = 0, 0

    for i in range(6):
        cnt[num % 10] += 1
        num //= 10

    i = 0
    while(i < 10): # for문으로 한정지으면 한 cnt 인덱스에 2번의 tri 발생 시 잡아내지 못 함
        if cnt[i] >= 3: # triplet
            cnt[i] -= 3
            tri += 1
            continue
        if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1
            runn += 1
            continue
        i += 1
        
    if tri + runn == 2:
        ans = 1
    else:
        ans = 0
    print(f'#{tc+1} {ans}')