import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if i + di[k] >= 0 and i + di[k] < n and j + dj[k] >= 0 and j + dj[k] < n:
                    s += abs(nums[i+di[k]][j+dj[k]] - nums[i][j])              
    print(f'#{tc+1} {s}')