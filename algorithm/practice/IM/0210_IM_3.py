# 정사각형 판정
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    sq = [list(map(str, input())) for _ in range(n)]
    idx1, idx2 = [], []
    for i in range(n):
        for j in range(n):
            if sq[i][j] == '#':
                idx1.append([i, j])
                idx2.append([j, i])
    idx2.sort() # #가 적힌 정사각형의 index 전치행렬

    if idx1 == idx2 and len(idx1) == (idx1[-1][0] - idx1[0][0] + 1) ** 2:
        # 원래 행렬과 전치행렬이 같고, 인덱스의 길이가 정사각형의 크기와 같을 때
        ans = 'yes'
    else:
        ans = 'no'
    print(f'#{tc} {ans}')