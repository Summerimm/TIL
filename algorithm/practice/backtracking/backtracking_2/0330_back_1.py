# 병합정렬
import sys
sys.stdin = open('input.txt', 'r')

# 분할과정
def partition(arr):
    if len(arr) == 1:
        return arr
    m = len(arr)//2
    left = arr[:m]
    right = arr[m:]
    left = partition(left)
    right = partition(right)
    return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    l, r = 0, 0
    if left[-1] > right[-1]:
        cnt += 1
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    arr = partition(nums)
    print(f'#{tc} {arr[N//2]} {cnt}')