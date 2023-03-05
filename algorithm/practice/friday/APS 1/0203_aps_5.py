# 기차 사이의 파리
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    D, A, B, F = map(int, input().split())
    t = D / (A + B)
    ans = F * t
    print(f'#{tc+1}', ans)