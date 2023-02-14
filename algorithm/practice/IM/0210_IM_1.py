# 파리퇴치
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    mx = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            tmp = 0
            for k in range(m):
                for l in range(m):
                    tmp += nums[i + k][j + l]
            if tmp > mx:
                mx = tmp
    print(f'#{tc} {mx}')