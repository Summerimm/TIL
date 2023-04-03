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