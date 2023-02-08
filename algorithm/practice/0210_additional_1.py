import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    numlist = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if numlist[i][j] == 1:
                cnt += 1
                if j == n-1 and cnt == k:
                    ans += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
    
    for j in range(n):
        cnt = 0
        for i in range(n):
            if numlist[i][j] == 1:
                cnt += 1
                if i == n-1 and cnt == k:
                    ans += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0

    print(f'#{t} {ans}')