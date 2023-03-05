# 그래프 경로
import sys
sys.stdin = open('input.txt', 'r')

def dfs(s):
    st = []
    visited[s] = 1
    st.append(s)
    v = s # 방문 중인 기준 노드
    while True:
        for n in node[v]: # 연결된
            if visited[n] == 0: # 미방문
                visited[n] = 1 # 방문처리
                st.append(n) # 스택에 저장
                v = n # 기준 노드 변경
                break
        else: # 미방문한 노드가 없음
            if st: # 올라갈 지점이 남아있으면
                v = st.pop()
            else: # 스택이 비어있으면 종료
                break

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # vertex, edge
    node = [[] for _ in range(V+1)] # idx = 기준노드, []내부 = 이동가능한 노드
    visited = [0] * (V+1) # global에 생성하고 visited[G](정답)을 바로 가져옴

    # graph 생성 (using adjacent list)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        node[v1].append(v2)
    
    S, G = map(int, input().split())    # 출발, 도착 노드
    dfs(S)
    print(f'#{tc} {visited[G]}')