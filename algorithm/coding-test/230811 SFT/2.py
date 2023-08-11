import sys
sys.stdin = open('input2.txt', 'r')

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def dfs(r, c):
    # print("r, c = ", r, c)
    global ans
    # r, c가 끝점이고, 모두 지나갔을 때
    if r == order[-1][0] and c == order[-1][1] and check.count(0) == 0:
        # print("r, c가 끝점이고, 모두 지나갔을 때")
        ans += 1
        return
    # r, c가 끝점이고, 어느 한 지점이라도 지나지 않았을 때
    if r == order[-1][0] and c == order[-1][1] and check.count(0) != 0:
        # print("r, c가 끝점이고, 어느 한 지점이라도 지나지 않았을 때")
        return
    # r, c가 끝점은 아니지만, 지나야 하는 지점임
    if [r, c] in order:
        # print("r, c가 끝점은 아니지만, 지나야 하는 지점임")
        # r, c가 시작점
        if order.index([r, c]) - 1 == -1:
            # print("r, c가 시작점")
            # 무조건 순서상 지나갔다고 체크, 방문배열 체크
            check[order.index([r, c])] = 1
            arr[r][c] = 1
            # dfs 진행
            for k in range(4):
                ni, nj = r + di[k], c + dj[k]
                if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    dfs(ni, nj)
                    arr[ni][nj] = 0
        # r, c가 지나야 하는 지점이지만, 앞 순서를 지나지 않았음
        elif check[order.index([r, c]) - 1] == 0:
            # print("r, c가 지나야 하는 지점이지만, 앞 순서를 지나지 않았음")
            return
        # r, c가 지나야 하는 지점이고, 앞 순서를 지났음
        else:
            # print("r, c가 지나야 하는 지점이고, 앞 순서를 지났음")
            check[order.index([r, c])] = 1
            for k in range(4):
                ni, nj = r + di[k], c + dj[k]
                if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    dfs(ni, nj)
                    arr[ni][nj] = 0
            check[order.index([r, c])] = 0
    # r, c는 끝점도 아니고, 지나야 하는 지점도 아닌 경우
    else:
        # print("r, c는 끝점도 아니고, 지나야 하는 지점도 아닌 경우")
        for k in range(4):
            ni, nj = r + di[k], c + dj[k]
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                dfs(ni, nj)
                arr[ni][nj] = 0

# n: 격자 가로, 세로 길이
# m: 지나야 하는 지점 개수
n, m = map(int, input().split())

# arr배열: 주어진 격자 그래프, 0은 빈 칸, 1은 벽
arr = [list(map(int, input().split())) for _ in range(n)]

# order배열: 지나야 하는 순서
order = []
for _ in range(m):
    r, c = map(int, input().split())
    order.append([r-1, c-1])

# check배열: 지나갔는지 안 지나갔는지 체크
check = [0] * (m-1)

# r_s, c_s: 시작 지점
r_s, c_s = order[0]

# r_e, c_e: 끝 지점
r_e, c_e = order[-1]

ans = 0
# dfs로 개수 세기
dfs(r_s, c_s)
print(ans)
