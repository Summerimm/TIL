# 재미있는 오셀로 게임
import sys
sys.stdin = open('input.txt', 'r')


def colorChange(r, c, color):
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    for k in range(8):
        st = []
        tmpi, tmpj = r, c
        flag = 1

        while flag and 0 <= tmpi + di[k] < N and 0 <= tmpj + dj[k] < N: # 범위 내
            tmpi += di[k]
            tmpj += dj[k] # 그 방향으로 1칸씩 나아가기
            if arr[tmpi][tmpj] == 0: # 빈 칸 발견
                flag = 0
                break
            elif arr[tmpi][tmpj] == color: # 같은 색깔 발견
                while st: # 스택이 빌 때까지
                    x = st.pop() # tmpi, tmpj를 꺼내서
                    arr[x[0]][x[1]] = color # 색을 바꿈
                    flag = 0
                break
            else:
                st.append((tmpi, tmpj)) # 다른 색이면 스택에 넣어둠

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    m = N // 2
    arr[m - 1][m - 1], arr[m - 1][m], arr[m][m - 1], arr[m][m] = 2, 1, 1, 2

    for _ in range(M):
        c, r, color = map(int, input().split())
        arr[r - 1][c - 1] = color
        colorChange(r - 1, c - 1, color)

    b, w = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                w += 1
            elif arr[i][j] == 1:
                b += 1
    print(f'#{tc} {b} {w}')