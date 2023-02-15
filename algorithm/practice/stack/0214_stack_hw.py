# 길 찾기
import sys
sys.stdin = open('input.txt', 'r')

def dfs(s):
    st = []
    visited[s] = 1
    st.append(s)
    v = s
    while True:
        for n in node[v]: # 연결된
            if visited[n] == 0: # 미방문
                visited[n] = 1
                st.append(n)
                v = n
                break # 조건을 만족하는 정점을 찾자마자 자식노드 실행
        else: # 연결된 정점들 중 방문 가능한 정점이 없을 때
            if st: # 되돌아갈 곳이 있으면
                v = st.pop()
            else: # 올라갈 곳이 더 이상 없으면
                break


T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    node = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(E):
        v1, v2 = arr[2*i], arr[2*i+1]
        node[v1].append(v2)
    dfs(0)
    print(f'#{tc} {visited[99]}')