# 그래프
- 그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현한다.
- 그래프는 정점(vertex)들의 집합과 이들을 연결하는 간선(edge)들의 집합으로 구성된 자료 구조
  - |V|: 정점의 개수, |E|: 그래프에 포함된 간선의 개수
  - |V|개의 정점을 가지는 그래프는 최대 |V|(|V|-1)/2간선이 가능
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이함

### 그래프의 종류
- 무향 그래프(Undirected Graph)
- 유향 그래프(Directed Graph)
- 가중치 그래프(Weighted Graph)
- 사이클 없는 방향 그래프(DAG, Directed Acyclic Graph)  
![image](https://user-images.githubusercontent.com/108309396/229397051-0433979a-84e0-4fa3-9cf3-65b7ea5e7fd3.png)

### 그래프 유형
- 완전 그래프: 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프: 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

### 인접(Adjacency)
- 두 개의 정점에 간선이 존재(연결됨)하면 서로 인접해있다고 한다.
- 완전 그래프에 속한 임의의 두 정점들은 모두 인접해있다.

### 그래프 경로
- 경로란 간선들을 순서대로 나열한 것
  - 간선들: (0, 2), (2, 4)
  - 정점들: 0-2-4
- 경로 중 한 정점을 최대한 한 번만 지나는 경로를 **단순경로**라 한다.(0-2-4-6)
- 시작한 정점에서 끝나는 경로를 **사이클(Cycle)**이라 한다.(1-3-5-1)

### 그래프 표현
- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정
- 인접 행렬(Adjacent matrix)
  - |V| * |V| 크기의 2차원 배열을 이용해서 간선 정보를 저장
  - 배열의 배열(포인터 배열)
  - 무향 그래프: i번째 행의 합 = i번째 열의 합 = $V_i$의 차수
  - 유향 그래프
    - 행 i의 합 = $V_i$의 진출 차수
    - 열 i의 합 = $V_i$의 진입 차수
- 인접 리스트(Adjacent List)
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- 간선의 배열
  - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

# DFS(Depth First Search, 깊이 우선 탐색)
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 DFS를 반복해야 하므로 FILO 구조의 스택 사용

### DFS 알고리즘 - 재귀
```python
DFS_recursive(v, k):
  visited[v] = 1  # 중복 방지용
  print(v)
  for w in adjL[v]: # v와 인접하고
    if visited[w] == 0: # 방문한 적 없는 w가 있으면
      DFS_recursive(w, k)
  for w in range(1, k+1):
    if adjM[v][w] == 1 and visited[w] == 0:
      DFS_recursive(w, k)
```

### DFS 알고리즘 - 반복
```python
DFS_iteration(s, k):
  stack = []
  visited = [0] * (k+1)
  v = s
  while True:
    if visited[v] == 0:
      print(v)
      visited[v] = 1
    for w in range(1, k+1):
      if adjM[v][w] and visited[w] == 0:
        stack.append(v)
        v = w
        break
    else:   # 더이상 인접인 정점이 없으면
      if stack:   # 스택이 비어있지 않으면
        v = stack.pop()
      else: # 스택이 비어있으면
        break
```

# BFS(Breadth First Search, BFS)
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 BFS를 진행해야 하므로, FIFO 구조의 큐를 사용

### BFS 알고리즘
```python
def BFS(arr, v):        # 그래프 arr, 탐색 시작점 v
  q = [v]               # 시작점 v를 큐에 삽입
  visited[v] = 1        # 점 v를 방문한 것으로 표시
  while q:              # 큐가 비어있지 않은 경우
    t = q.pop(0)        # 큐의 첫 번째 원소 반환
    for w in arr[t]:    # t와 연결된 모든 선에 대해
      u = w             # u에 t의 이웃점 삽입
      if visited[u] == 0 :  # u가 방문하지 않은 곳이면
        q.append(u)
        visited[u] = 1      # u를 큐에 넣고, 방문한 것으로 표시
```

# 서로소 집합(Disjoint-sets)
- 서로소 또는 상호배타 집합들은 서로 중복 포함된 우너소가 없는 집합들이다. 즉, 교집합X
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분함. 이 특정 멤버를 대표자(representative)라 한다.

### 상호배타 집합을 표현하는 방법
- 연결리스트, 트리

### 상호배타 집합 연산
- Make-Set(x): 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산  
![image](https://user-images.githubusercontent.com/108309396/229671594-dfca8bf3-fb86-4c24-8f67-fb88e2183e2f.png)
- Find-Set(x): x를 포함하는 집합을 찾는 연산
1) 재귀    
![image](https://user-images.githubusercontent.com/108309396/229671610-6f04645c-cbf5-48ea-b42c-01beab7cd42d.png)
2) 반복   
![image](https://user-images.githubusercontent.com/108309396/229671736-f95bea23-57cf-4a3d-807c-84c608dece67.png)  
- Union(x, y): x와 y를 포함하는 두 집합을 통합하는 연산    
![image](https://user-images.githubusercontent.com/108309396/229671621-733cd9ba-c62f-4f53-aace-95d8927cf3c7.png)


## 상호배타 집합 표현 - 연결리스트
- 같은 집합의 원소들은 하나의 연결리스트로 관리한다.
- 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다.
- 각 원소는 집합의 대표원소를 가리키는 링크를 갖는다.  
![image](https://user-images.githubusercontent.com/108309396/229670785-7a14c5f3-9003-4fb8-a4d0-8aa89fe4bcc1.png)
- 연결리스트 연산 예
  - Find-Set(e)   return a
  - Find-Set(f)   return b
  - Unioon(a, b)  
    ![image](https://user-images.githubusercontent.com/108309396/229670891-b0ec03c1-b65c-4baf-8b6f-f466faa53114.png)

## 상호배타 집합 표현 - 트리
- 하나의 집합(a disjoint set)을 하나의 트리로 표현
- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 됨  
![image](https://user-images.githubusercontent.com/108309396/229671048-b9dd955c-029f-46cc-a2d5-f9913c9cb2b1.png)
- 트리 연산 예
  - Make-Set(a) ~ Make-Set(f)  
  ![image](https://user-images.githubusercontent.com/108309396/229671148-5ceb5486-c55a-4c34-bdb1-6f88144729f4.png)  
  - Union(c, d), Union(e, f)  
  ![image](https://user-images.githubusercontent.com/108309396/229671165-a6f204c6-8773-4dd3-adbb-5f111a0c3ce7.png)
  - Union(d, f)  
  ![image](https://user-images.githubusercontent.com/108309396/229671221-9f267f9f-ba99-4c5f-9ba9-cfbeed8ec4a3.png)
  - Find-Set(d)     return c
  - Find-Set(e)     return c

### 상호배타 집합을 표현한 트리 -  배열을 이용해 저장된 모습
![image](https://user-images.githubusercontent.com/108309396/229671389-4f2a6b0c-d61b-4c6a-a1cc-c1e5c4ca5888.png)
- 정점이 부모를 가리킴

### 연산의 효율을 높이는 방법
1. Rank를 이용한 Union
  - 각 노드는 자신을 루트로 하는 subtree의 높이를 rank라는 이름으로 저장한다.
  - 두 집합을 합칠 때 rank가 낮은 집합을 높은 집합에 붙인다.  
![image](https://user-images.githubusercontent.com/108309396/229675990-c4a206fa-867a-4a5a-9617-4bdb25027974.png)    
![image](https://user-images.githubusercontent.com/108309396/229676042-4c9fb2ed-7e25-47c6-a350-068a79f00066.png)
- 연산 방법  
  - Make-Set(x)    
  ![image](https://user-images.githubusercontent.com/108309396/229676370-2e34ae4e-c964-40fa-a6a1-ffd62cbbad11.png)
  - Find-Set(x)  
  ![image](https://user-images.githubusercontent.com/108309396/229676415-22b0b7b2-34e8-4cbe-963c-3284574fd7fa.png)
  - Union(x, y)  
  ![image](https://user-images.githubusercontent.com/108309396/229676471-cab0476b-0b14-4810-87b1-007728018076.png)
1. Path compression  
  - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어준다.    
![image](https://user-images.githubusercontent.com/108309396/229676083-d1655152-bcf1-4572-bc61-ff2d0b2ebefd.png)

# 최소 신장 트리(MST: Minimum Spanning Tree)
- 신장 트리: n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
- MST: 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

## Prim Algorithm
- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어가는 방식
1) 임의 정점을 하나 선택해서 시작
2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3) 모든 정점이 선택될 때까지 1), 2) 반복  
![image](https://user-images.githubusercontent.com/108309396/229678695-f5384ec8-b0bd-4078-82ad-a3141579a0a4.png)  
- 서로소인 2개의 집합 정보를 유지
  - 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
  - 비트리 정점들(nontree vertices) - 선택되지 않은 정점들

## Kruskal Algorithm
- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
1) 최초, 모든 간선을 가중치에 따라 **오름차순**으로 정렬
2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
3) n-1개의 간선이 선택될 때까지 2)를 반복  
![image](https://user-images.githubusercontent.com/108309396/229681313-7fa76cbd-13e8-4c8d-b70e-ad2d1c161278.png)  
![image](https://user-images.githubusercontent.com/108309396/229681337-bb40a54f-6377-4674-b0c8-549eac12a216.png)  
![image](https://user-images.githubusercontent.com/108309396/229681362-ed60c02e-3da9-4a28-8399-a3b49299fe35.png)

# 최단 경로
- 최단 경로란?
  - 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
1) 하나의 시작 정점에서 끝 정점까지의 최단 경로
  - 다익스트라(dijkstra) 알고리즘: 음의 가중치 허용X
  - 벨만-포드(Bellman-Ford) 알고리즘: 음의 가중치 허용
2) 모든 정점들에 대한 최단 경로
  - 플로이드-워샬(Floyd-Warshall) 알고리즘: 음의 가중치 허용

## Dijkstra Algorithm
- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
- 시작정점(s)에서 끝정점(t)까지의 최단 경로에 정점 x가 존재한다.
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성된다.
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사    
![image](https://user-images.githubusercontent.com/108309396/229694293-6923ba8c-2075-498f-ba3a-030621f3d86c.png)  
```python
def dijkstra(s, V):   # s 출발, V 마지막 정점 번호
  U = [0] * (V+1)     # U 최소 비용이 결정된 정점 집합 / visited 배열
  U[s] = 1            # U = {s}
  for i in range(V+1):  # s에서 나머지 정점 i로 가는 비용
    D[i] = adjM[s][i]

  # while U != V: 남은 정점의 비용 결정
  N = V+1   # N개의 정점
  for _ in range(N-1):    # N-1개 정점의 비용 결정
    # D[w]가 최소인 w 결정
    minV = INF
    w = 0
    for i in range(V+1):
      if U[i] == 0 and minV > D[i]:   # 남은 정점 i 중, 최소
        w = i
        minV = D[i]
    U[w] = 1      # 최소인 w는 최소 비용 D[w] 확정
    # w에 인접인 정점에 대해, 기존비용 vs w를 거쳐가는 비용 비교
    for v in range(V+1):
      if 0 < adjM[w][v] < INF:  # w에 인접인 v의 조건
        D[v] = min(D[v], D[w] + adjM[w][v])

INF = 10000   # 문제에 따라
V, E = map(int, input().split())  # 0~V번 정점, E 간선 수
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
  adjM[i][i] = 0    # 자기자신으로 가는 비용
for _ in range(E):
  u, v, w = map(int, input().split())   # u -> v, w: 가중치
  adjM[u][v] = w

D = [0] * (V+1)

```