# Stack1_연습문제_2: 깊이우선탐색
import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):
    v = [0] * (V+1)
    stk, ans = [], []
    s = start
    v[s] = 1
    ans.append(s)
    while True:
        for e in range(1, V+1):
            if v[e] == 0 and adjM[s][e]: # 미방문 & 연결되어 있음
                stk.append(s) # 돌아올 지점
                s = e # 새로운 base node
                v[s] = 1 # 방문처리
                ans.append(s) # ans에 추가
                break # 찾았으면 즉시, base노드 변경
        else: # 더 이상 연결된 방문노드 없는 경우
            if stk:
                s = stk.pop() # 이전 노드로 돌아감
            else:
                break # while 탈출
    return ans

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjM[v1][v2] = 1
        adjM[v2][v1] = 1
    ans = dfs(1)
    print(f'#{tc}', *ans)