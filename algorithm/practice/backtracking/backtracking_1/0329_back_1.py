# 퀵 정렬
import sys
sys.stdin = open('input.txt','r')

def quicksort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s-1)
        quicksort(arr, s+1, r)

def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p: 
            i += 1
        while i <=j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[l], arr[j] = arr[j], arr[l]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)

    print(f'#{tc}', arr[N//2])