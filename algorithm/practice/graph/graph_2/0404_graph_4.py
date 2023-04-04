# 그룹 나누기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)]
    arr = list(map(int, input().split()))
    for i in range(len(arr)//2):
        rep[arr[2*i]] = arr[2*i+1]
    print(rep)
    # print(f'#{tc} {ans}')