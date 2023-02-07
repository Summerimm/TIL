import sys
sys.stdin = open('input.txt', 'r')

def outer(arr, n, k, num): # arr는 list, n은 정사각형 한 변의 길이, k는 시작점
    for i in range(k, n-1-k): # 윗 행 오른쪽 방향으로 증가
        arr[k][i] = num
        num += 1
    for i in range(k, n-1-k): # 오른쪽 행 아래 방향으로 증가
        arr[i][n-1-k] = num
        num += 1
    for i in range(n-1-k, k, -1): # 아래 행 왼쪽 방향으로 증가
        arr[n-1-k][i] = num
        num += 1
    for i in range(n-1-k, k, -1): # 왼쪽 행 위 방향으로 증가
        arr[i][k] = num
        num += 1
    return num

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    num = 1
    k = 0
    while k < n // 2:
        num = outer(snail, n, k, num)
        k += 1
    if n % 2:
        snail[n//2][n//2] = num
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()
