import sys

sys.stdin = open('input.txt', 'r')

def backtracking(s):
    st = [] # 되돌아갈 지점 저장
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    v = [0, 0] # 기준 노드
    t = [0, 0] # s값 바뀌지 않게 하기 위해서
    t[0], t[1] = s[0], s[1]
    st.append(s)
    flag = 1
    while flag:
        for k in range(4):
            v[0] = t[0] + di[k] # 기준노드
            v[1] = t[1] + dj[k]
            if 0 <= v[0] < N and 0 <= v[1] < N:
                if arr[v[0]][v[1]] == '3':
                    ans = 1
                    flag = 0
                    break
                elif arr[v[0]][v[1]] == '0':
                    arr[v[0]][v[1]] = '2'
                    st.append([v[0], v[1]])
                    t[0], t[1] = v[0], v[1]
                    break
            else: # 미로 범위 밖
                continue
        else: # 미로범위 밖에 잡히거나, 주변이 모두 1 혹은 2일 때
            if st: # 돌아갈 곳 존재
                x = st.pop()
                t[0], t[1] = x[0], x[1]
            else: # 돌아갈 곳 없음
                ans = 0
                flag = 0
                break
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 시작 노드 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                s = [i, j]
                break

    a = backtracking(s)
    print(f'#{tc} {a}')