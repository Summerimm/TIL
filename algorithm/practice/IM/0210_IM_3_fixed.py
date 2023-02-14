# 정사각형 판정
import sys

sys.stdin = open('input.txt', 'r')

def sqcheck(idx, sq):
    ans = 'yes'
    l = len(idx) ** 0.5
    if l % 1 != 0: # 추정한 정사각형 길이가 무리수(제곱수가 아님)
        return 'no'
    k1, k2 = idx[0][0], idx[0][1] # 좌상단 index
    for i in range(k1, k1 + int(l)): # 정사각형 한 변의 길이만큼 loop
        for j in range(k2, k2 + int(l)):
            if sq[i][j] != '#': # 하나라도 #이 아니면 no
                ans = 'no'
                return ans
    return ans

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    sq = [list(input()) for _ in range(n)]
    candidx = []
    for i in range(n):
        for j in range(n):
            if sq[i][j] == '#':
                candidx.append((i, j)) # 정사각형 후보 index 모두 넣기
    ans = sqcheck(candidx, sq)    
    print(f'#{tc} {ans}')