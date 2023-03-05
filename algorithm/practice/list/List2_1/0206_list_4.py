# 색칠하기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cnt = [[0] * 10 for _ in range(10)]
    ans = 0
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                cnt[r][c] += 1
                if cnt[r][c] == 2:
                    ans += 1
    print(f'#{t} {ans}')