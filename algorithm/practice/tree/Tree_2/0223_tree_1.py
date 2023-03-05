# 노드의 합
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+2)

    for _ in range(M):
        i, v = map(int, input().split())
        arr[i] = v
    
    for i in range(N, 1, -2):
        if i % 2:
            arr[i//2] = arr[i] + arr[i-1]
        else:
            arr[i//2] = arr[i] + arr[i+1]
    print(f'#{tc} {arr[L]}')