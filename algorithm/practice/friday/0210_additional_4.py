# 스도쿠 검증
T = int(input())
for t in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sq = [[[] for _ in range(3)] for _ in range(3)]
    ans = 1
    for i in range(9):
        # 가로 줄 Check
        if len(set(sudoku[i])) != 9:
            ans = 0
            break
        # 세로 줄 Check
        if len(set(sudo[i] for sudo in sudoku)) != 9:
            ans = 0
            break
        # 정사각형 Check(3의 배수 활용)
        for j in range(9):
            m = i // 3
            n = j // 3
            sq[m][n].append(sudoku[i][j])
    if ans != 0:
        for k in range(3):
            for l in range(3):
                if len(set(sq[k][l])) != 9:
                    ans = 0
                    break
    print(f'#{t} {ans}')