# 낚시왕
import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def fish(j):
    for i in range(R):
        if board[i][j]:
            x = board[i][j][2]  # 크기 더해줌
            return x
    return 0

def move():
    global board
    new_board = [[0 for _ in range(C)] for _ in range(R)]   # 상어들의 새 위치를 담음
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                # 이 상어의 다음 위치
                ni, nj, nd = get_next_loc(i, j, board[i][j][0], board[i][j][1])
                if new_board[ni][nj]:
                    new_board[ni][nj] = max(new_board[ni][nj], (board[i][j][0], nd, board[i][j][2]), key=lambda x: x[2])
                    

def get_next_loc(i, j, speed, dir):
    if dir == UP or dir == DOWN:
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - i
        else:
            speed += i

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())   # 행 / 열 / 속도 / 방향 / 크기
    r, c = r-1, c-1
    board[r][c] = (s, d, z)
    # 0      1      2
    # 속도 / 방향 / 크기

ans = 0
for j in range(C):  # 사람 이동
    ans += fish(j)  # 상어 잡기
    move()          # 상어 이동

print(ans)

