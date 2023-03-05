# 전위순회
import sys
sys.stdin = open('input.txt', 'r')

def preorder(T):
    try:
        print(T, end=' ')
        preorder(tree[T][0])
        preorder(tree[T][1])
    except:
        return

T = int(input())
for tc in range(1, T+1):
    V = int(input())
    E = V - 1
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(V+1)]

    for i in range(E):
        tree[lst[2*i]].append(lst[2*i+1])
        
    print(f'#{tc}', end=' ')
    preorder(1)
    print()
# 1
# |\
# 2 3
# | | \ 
# 4 5   6
# | |\  | \
# 7 8 9 10 11
# |         |
# 12       13