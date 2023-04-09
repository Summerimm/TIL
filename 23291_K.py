# 어항 정리
import sys
sys.stdin = open('input.txt', 'r')
import math
from pprint import pprint
from copy import deepcopy

N, K = map(int, input().split())    # 23 7
arr = list(map(int, input().split()))   # [5, 2, 3, 14, 9, 2, 11, 8]

rt = int(math.sqrt(N))      # 4(정사각형 한 변의 길이)
tmp = N - (rt ** 2 + rt)    # 3(김밥말이 후 남는 칸)
if tmp > 0:     # 김밥말이가 직사각형 모양(가로 4, 세로 5)
    r, c = rt + 1, rt
    tarr2 = arr[-tmp:]   # 남는 칸
elif tmp == 0:
    r, c = rt + 1, rt
    tarr2 = []
else:           # 김밥말이가 정사각형 모양
    r, c = rt, rt
    tarr2 = arr[-(N - rt**2):]
tarr1 = [[0] * c for _ in range(r)]

di = [0, -1, 0, 1]      # 좌 상 우 하
dj = [-1, 0, 1, 0]
k = 0                   # di, dj 인덱스

cnt = N - tmp - 1       # 20 ~ 1 될 때까지
ni, nj = r-1, c-1           # 김밥말이 인덱스
tarr1[ni][nj] = arr[cnt]   # 김밥말이 초기값
cnt -= 1                # arr 인덱스 / while문

while cnt >= 0:
    ni, nj = ni + di[k], nj + dj[k]
    if 0<=ni<r and 0<=nj<c and tarr1[ni][nj] == 0:
        tarr1[ni][nj] = arr[cnt]
        cnt -= 1
    else:
        ni -= di[k]
        nj -= dj[k]
        k += 1
        k = k % 4
pprint(tarr1)
# print(tarr2)

tarr3 = deepcopy(tarr1)

for i in range(r):
    for j in range(c):
        for k in range(2, 4):
            ni, nj = i + di[k], j + dj[k]
            if 0<=ni<r and 0<=nj<c:
                d = abs(tarr1[i][j] - tarr1[ni][nj]) // 5
                if d:
                    if tarr1[i][j] > tarr1[ni][nj]:
                        tarr3[i][j] -= d
                        tarr3[ni][nj] += d
                    else:
                        tarr3[i][j] += d
                        tarr3[ni][nj] -= d

pprint(tarr3)