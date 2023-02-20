# 피자 굽기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wait = list(enumerate(map(int, input().split()), 1))
    q = []
    cnt = 0

    for i in range(N):
        q.append(wait.pop(0))    # 화덕 초기화
    
    while q:    # 화덕이 빌 때까지
        if wait and len(q) < N: # 대기가 있고 화덕에 있는 피자가 꽉 안 채워졌을 때
            q.append(wait.pop(0))
        num, pizza = q.pop(0)
        pizza //= 2
        if pizza:       # 0이 아닐 때
            q.append((num, pizza))  # 도로 넣기

    print(f'#{tc} {num}')