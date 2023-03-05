# 토너먼트 카드게임
import sys
sys.stdin = open('input.txt', 'r')

def tournament(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        a = tournament(s, mid)
        b = tournament(mid+1, e)
        if (arr[a] % 3) + 1 == arr[b]:
            return b
        else:
            return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    ans = tournament(1, N)
    print(f'#{tc} {ans}')