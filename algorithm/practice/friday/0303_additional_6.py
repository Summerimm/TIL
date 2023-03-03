# 오목판정
import sys
sys.stdin = open('input.txt', 'r')

def diagonal(arr):
    for i in range(N-4):
        for j in range(N-4):
            tmp1 = ''.join((arr[i][j], arr[i+1][j+1], arr[i+2][j+2], arr[i+3][j+3], arr[i+4][j+4]))
            if tmp1 == 'o' * 5:
                return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    arrt = [''.join(c) for c in zip(*arr)]

    ans = 'NO'
    for st in arr + arrt:
        if 'o'*5 in st:
            ans = 'YES'
            break 
    else:
        if diagonal(arr) or diagonal(arrt[::-1]):
            ans = 'YES'
    print(f'#{tc} {ans}')