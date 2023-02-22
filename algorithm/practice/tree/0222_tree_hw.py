# 중위순회
import sys
sys.stdin = open('input.txt', 'r')

def inorder(T):
    if T:
        inorder(ch1[T])
        print(char[T], end='')
        inorder(ch2[T])

T = 10
for tc in range(1, T+1):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    char = [[] for _ in range(N+1)]

    for i in range(N):
        p, c, *nodes = map(str, input().split())
        p = int(p)
        char[p] = c
        if nodes:
            for node in nodes:
                if ch1[p] == 0:
                    ch1[p] = int(node)
                else:
                    ch2[p] = int(node)
    print(f'#{tc} ', end='')
    inorder(1)
    print()