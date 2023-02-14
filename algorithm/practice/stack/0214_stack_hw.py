# [S/W 문제해결 기본] 4일차 - 길찾기
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    node1 = [0] * 100
    node2 = [0] * 100

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        if node1[v1] == 0:
            node1[v1] = v2
        else:
            node2[v1] = v2
    
    target = 99
    while target > 0:
        for i in range(100):
            if node1[i] == target:
                target = i
                break
    
    target = 99
    while target > 0:
        for i in range(100):
            if node2[i] == target:
                target = i
                break
    if target == 0
    print(f'#{tc}', ans)