# [S/W 문제해결 기본] 1일차 - Flatten
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    dump = int(input())
    height = list(map(int, input().split()))

    for i in range(dump):
        max = 0
        min = 101
        for idx, h in enumerate(height):
            if h >= max:
                max = h
                maxidx = idx
            if h <= min:
                min = h
                minidx = idx
        height[maxidx] -= 1
        height[minidx] += 1

    maxv = 0
    minv = 101
    for num in height:
        if num >= maxv:
            maxv = num
        if num <= minv:
            minv = num
    print(f'#{tc+1} {maxv - minv}')