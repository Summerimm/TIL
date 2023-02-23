# 이진 힙
import sys
sys.stdin = open('input.txt', 'r')

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T =  int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    for i in range(N):
        enq(arr[i])
    idx = N
    cnt = 0
    while idx > 0:
        idx //= 2
        cnt += heap[idx]
    print(f'#{tc} {cnt}')