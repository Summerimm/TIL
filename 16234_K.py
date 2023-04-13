# 인구 이동
import sys
sys.stdin = open('input.txt','r')

def move(move_set, num):
    for ti, tj in move_set:
        arr[ti][tj] = each      


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 국경선을 공유하는 두 나라에 대해서
# 차이가 L 이상 R 이하
# 국경선 모두 열고나서 인구 이동 시작
# 이동가능한 칸들은 연합이 되고 각 칸의 인구수는 연합의 총 인구수/칸 개수
# 연합 해체 후 국경선 닫기
# 인구 이동이 없을 때까지 지속

peoplesum = 0
move_set = set()
for i in range(N):
    for j in range(N):
        for di, dj in [(0, 1), (1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if L <= arr[i][j] - arr[ni][nj] <= R:
                    move_set.add((i, j))
                    move_set.add((ni, nj))

for i, j in move_set:
    peoplesum += arr[i][j]
each = peoplesum // len(move_set)
move(move_set, each)
print(arr)