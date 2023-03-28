# 베이비진 게임
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    cnt1 = [0] * 12
    cnt2 = [0] * 12

    ans = 0
    for i in range(6):
        cnt1[arr[2*i]] += 1
        cnt2[arr[2*i+1]] += 1
        if i >= 2 and not ans:
            j = 0
            while j < 10:
                if cnt1[j] == 3:
                    ans = 1
                    break
                elif cnt1[j] >= 1 and cnt1[j+1] >= 1 and cnt1[j+2] >= 1:
                    ans = 1
                    break
                j += 1
            j = 0
            while j < 10 and not ans:
                if cnt2[j] == 3:
                    ans = 2
                    break
                elif cnt2[j] >= 1 and cnt2[j+1] >= 1 and cnt2[j+2] >= 1:
                    ans = 2
                    break
                j += 1

    print(f'#{tc} {ans}')