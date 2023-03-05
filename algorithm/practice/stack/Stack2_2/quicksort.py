# 퀵 정렬
import sys
sys.stdin = open('input.txt', 'r')

def quickSort(begin, end):
    if begin < end:
        pivot = (begin + end) // 2
        L = begin
        R = end
        while L < R:
            while (L < R and a[L] < a[pivot]): 
                L += 1
            while (L < R and a[R] >= a[pivot]): 
                R -= 1
            if L < R:
                if L == pivot:
                    pivot = R
            a[L], a[R] = a[R], a[L]
        a[pivot], a[R] = a[R], a[pivot]
        quickSort(begin, R-1)
        quickSort(R+1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    quickSort(0, N-1)
    print(f'#{tc}', *a)