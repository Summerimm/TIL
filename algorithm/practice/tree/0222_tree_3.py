# 이진탐색
import sys
sys.stdin = open('input.txt', 'r')

def inorder(n):
    global cnt
    if 1 <=n<= N:
        inorder(n*2)
        tree[n] = cnt
        cnt += 1
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)   
    print(f'#{tc} {tree[1]} {tree[N//2]}')