# 미로
import sys

sys.stdin = open('input.txt', 'r')

def dfs(si, sj):
    st = []
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    ci, cj = si, sj     # 기준점
    arr[ci][cj] = '1'   # 방문한 위치를 벽으로 처리

    while True:
        for k in range(4):
            vi, vj = ci+di[k], cj+dj[k]
            # 미로 범위 내/0 혹은 3(미방문)
            if 0 <= vi < N and 0 <= vj < N and arr[vi][vj] != '1':
                st.append((ci, cj))   # 부모노드(돌아올 지점) 저장
                ci, cj = vi, vj     # 기준점 변경(자식노드 ni, nj)로
                arr[ci][cj] = '1'   # 자식노드 방문처리
                break               # 이동 경로 찾자마자 실행
        else:
            if st: # 돌아갈 지점 존재
                ci, cj = st.pop()
            else:  # 돌아갈 지점 X
                break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 시작 노드 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    dfs(si, sj)
    ans = arr[ei][ej]
    # 도착지점에 3이 그대로 적혀있으면 방문 실패했다는 의미
    if ans == '3':
        ans = '0'
    print(f'#{tc} {ans}')