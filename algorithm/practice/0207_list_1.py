import sys
sys.stdin = open('input.txt', 'r')

def binarySearch(a, N, key):
    start = 0
    end = N
    while start <= end:
        mid = (start + end) //2
        if nums[mid] == D:
            return mid + 1
        elif nums[mid] > D:
            end = mid - 1
        else:
            start = mid + 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N, D = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f'#{tc} {binarySearch(nums, N, D)}')
