import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        maxI = i
        minI = i
        if i % 2 == 0: # max
            for j in range(i + 1, n):
                if nums[j] > nums[maxI]:
                    maxI = j
            nums[i], nums[maxI] = nums[maxI], nums[i]
        else: # min
            for j in range(i + 1, n):
                if nums[j] < nums[minI]:
                    minI = j
            nums[i], nums[minI] = nums[minI], nums[i]
    print(f'#{tc}',end=' ')
    print(*nums[:10])