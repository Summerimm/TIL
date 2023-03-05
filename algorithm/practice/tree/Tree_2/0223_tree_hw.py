# 사칙연산
import sys
sys.stdin = open('input.txt', 'r')

T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)

    for i in range(N-1, -1, -1):
        if len(arr[i]) == 2: # 숫자
            a, b = map(int, arr[i])
            tree[a] = b
        else: # 연산자 포함
            a, b, c, d = arr[i]
            a, c, d = int(a), int(c), int(d)
            C, D = tree[c], tree[d]
            if b == '+':
                tree[a] = C + D
            if b == '-':
                tree[a] = C - D
            if b == '*':
                tree[a] = C * D
            if b == '/':
                tree[a] = C / D
    print(f'#{tc} {int(tree[1])}')