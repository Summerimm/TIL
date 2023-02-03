import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    cnt = [1] * (n)
    index = 0
    for idx in range(1, n):
        if seq[idx] > seq[idx-1]: # 내가 내 전의 당근보다 클 경우
            cnt[index] += 1
        else: # 내가 내 전의 당근보다 작거나 같은 경우
            index += 1
    print(f'#{tc+1} {max(cnt)}')