# 암호생성기
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    _ = input()
    q = list(map(int, input().split()))
    flag = 1
    while flag:
        for i in range(1, 6):
            v = q.pop(0) - i
            if v <= 0:
                ans = q + [0]
                flag = 0
                break
            q.append(v)
    print(f'#{tc}', end=' ')
    print(*ans)