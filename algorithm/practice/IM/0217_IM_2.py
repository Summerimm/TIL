# 오목 판정
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]  # 원래 오목 행렬
    omokt = [''.join(i) for i in zip(*omok)] # 오목 전치행렬

    omokd1 = []     # 오목 좌상우하 대각선 행렬
    for r in range(N-1, -1, -1): # 기준점
        st = ''
        c = 0
        while 0<=r<N and 0<=c<N:
            st += omok[r][c]
            r += 1
            c += 1
        omokd1.append(st)
    for c in range(1, N):
        st = ''
        r = 0
        while 0<=c<N and 0<=c<N:
            st += omok[r][c]
            r += 1
            c += 1
        omokd1.append(st)

    omokd2 = []     # 오목 우상좌하 대각선 행렬
    for r in range(N): # 기준점
        st = ''
        c = N-1
        while 0<=r<N and 0<=c<N:
            st += omok[r][c]
            r += 1
            c -= 1
        omokd2.append(st)
    for c in range(N-2, -1, -1):
        st = ''
        r = 0
        while 0<=c<N and 0<=c<N:
            st += omok[r][c]
            r += 1
            c -= 1
        omokd2.append(st)

    ans = 'NO'
    if 'o' * 5 in omok + omokt:
        ans = 'YES'
    if 'o' * 5 in omokd1 + omokd2 :
        ans = 'YES'

    print(f'#{tc} {ans}')