# 점점 커지는 당근의 개수
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    ans = 1
    anslist = []
    for idx in range(1, n):
        if seq[idx] > seq[idx-1]: # 내가 내 전의 당근보다 클 경우
            ans += 1
        else: # 내가 내 전의 당근보다 작거나 같은 경우
            anslist.append(ans)
            ans = 1
    anslist.append(ans)

    mx = 0
    for a in anslist:
        if a > mx:
            mx = a
    print(f'#{tc+1} {mx}')