# 홈 방범 서비스
import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    homes = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    if N % 2:
        K = (N + 1) // 2
    else:
        K = N // 2
    
    for si in range(N):
        for sj in range(N):
            for i in range(si, si+K):                  # 아래쪽 절반
                for j in range(sj, sj+K-i):            # 제 4사분면
                    if 0<=i<N and 0<=j<N:
                        print(si, sj, 'i, j', i, j)
                for k in range(sj-1, sj-K+i, -1):   # 제 3사분면
                    if 0<=i<N and 0<=k<N:
                        print(si, sj, 'i, k', i, k)

            for i in range(si-1, si-K, -1):         # 위쪽 절반
                for j in range(sj, sj+K+i):             # 제 1사분면 
                    if 0<=i<N and 0<=j<N:
                        print(si, sj, 'i, j', i, j)
                for k in range(sj-1, sj-K-i, -1):   # 제 2사분면
                    if 0<=i<N and 0<=k<N:
                        print(si, sj, 'i, k', i, k)
    

    # pprint(homes)
    # print(f'#{tc} {ans}')