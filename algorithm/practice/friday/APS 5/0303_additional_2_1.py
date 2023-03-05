# 파리퇴치 3
import sys
sys.stdin = open('input.txt', 'r')

def solve_x():
    mx = 0
    for si in range(N):
        for sj in range(N):
            tmp = arr[si][sj]
            for i in range(si-M+1, si+M):
                t = abs(si-i)
                if 0<=i<N and 0<=sj-t<N and si != i:
                    tmp += arr[i][sj-t]
                if 0<=i<N and 0<=sj+t<N and si != i:
                    tmp += arr[i][sj+t]
            mx = max(mx, tmp)
    return mx

def solve_plus():
    mx = 0
    for si in range(N):
        for sj in range(N):
            tmp = 0
            for i in range(si-M+1, si+M):
                if 0<=i<N:
                    tmp += arr[i][sj]
            for j in range(sj-M+1, sj+M):
                if 0<=j<N:
                    tmp += arr[si][j]
            tmp -= arr[si][sj]
            mx = max(mx, tmp)
    return mx


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = max(solve_plus(), solve_x())
    print(f'#{tc} {ans}')