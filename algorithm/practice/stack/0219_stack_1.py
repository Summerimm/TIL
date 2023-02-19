# 퀵 정렬
import sys
sys.stdin = open('input.txt', 'r')

def qsort(lst):
    if len(lst) <= 1:
        return lst
    
    p = lst.pop()
    left, right = [], []
    for n in lst:
        if n < p:
            left.append(n)
        else:
            right.append(n)
    return qsort(left) + [p] + qsort(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qarr = qsort(arr)
    ans = qarr[N//2]
    print(f'#{tc} {ans}')