# 자기 방으로 돌아가기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 200 # 카운트 배열(복도번호 공유)
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:   # 역으로 돌아갈 때
            a, b = b, a
        for j in range((a-1)//2, (b-1)//2+1):
            cnt[j] += 1
    print(f'#{tc} {max(cnt)}')
