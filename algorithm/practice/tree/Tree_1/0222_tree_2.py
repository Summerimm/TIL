# subtree
import sys
sys.stdin = open('input.txt', 'r')

def subtree(t):
    global ans
    if tree[t]:
        for c in tree[t]:
            subtree(c)
    ans += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    ans = 0
    for i in range(E):
        tree[lst[2*i]].append(lst[2*i+1])
    subtree(N)
    print(f'#{tc} {ans}')