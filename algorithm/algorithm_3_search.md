# Search
- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
  - search key: 자료를 구별하여 인식할 수 있는 키

## Sequential Search(순차 검색)
- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 **순차구조로 구현된 자료구조**에서 원하는 항목을 찾을 때 유용
  - 알고리즘이 단순하여 구현이 쉬움
  - but 검색 대상의 수가 많은 경우에는 수행 시간이 급격히 증가하여 비효율적
- 과정
  - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾음
  - 키 값이 동일한 원소를 찾으면 index 반환
  - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
- 정렬되어 있지 않은 경우
  - 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨
  - 정렬되어 있지 않은 자료에서의 순차 검색의 평균 비교 회수
    - $(1/n)*(1+2+3+...+n) = (n+1)/2$
  - $O(n)$  
![화면 캡처 2023-02-07 101848](https://user-images.githubusercontent.com/108309396/217123639-c569a0b4-43e3-432d-b3e2-f3915a9b6837.png)
- 정렬되어 있는 경우(오름차순)
  - 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색대상의 키 값보다 크면 찾는 원소가 없다는 뜻. 따라서 더 이상 검색하지 않고 종료한다.
  - 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨
    - 정렬되어 있으므로, 검색 실패를 반환하는 경우 평균 비교횟수가 반으로 줄어듦
    - $O(n)$    
![화면 캡처 2023-02-07 102434](https://user-images.githubusercontent.com/108309396/217124339-79c7c210-bc64-486b-a6a8-29d4180472a1.png)

## Binary Search(이진 검색)
- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
- 이진 검색을 하기 위해서는 자료가 정렬되어야 함
- 과정
1. 자료의 중앙에 있는 원소를 고른다
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서, 크다면 오른쪽 반에 대해서 새로 검색을 수행
- 구현
  - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다  
  - 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬상태로 유지하는 추가 작업 필요   
1. 반복구조  
![image](https://user-images.githubusercontent.com/108309396/228705047-e2d7d94d-3487-4ada-9657-076c9a07d7f2.png)
2. 재귀구조(실제로 이진탐색 시에 좋진 않음)  
![image](https://user-images.githubusercontent.com/108309396/228705105-3dee61d3-baf9-4788-976d-d7860fdc73a7.png)

## DFS(Depth First Search, 깊이 우선 탐색)
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 LIFO 구조의 `Stack` 사용 
- 알고리즘
  1. 시작 노드 v를 결정하여 방문
  2. 노드 v에 인접한 노드 중에서
    - 방문하지 않은 노드 w가 있으면, 노드 v를 스택에 push하고 노드 w를 방문한다.
    - 방문하지 않은 노드가 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 노드를 v로 하여 다시 2를 반복
  3. 스택이 공백이 될 때까지 2를 반복  
![2122](https://user-images.githubusercontent.com/108309396/218618059-48828a3e-27e5-4ddd-9fa0-554d6ab4de57.png)

### Adjacent Array(인접행렬)
```python
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)] # 인접리스트
adjM = [[0]*(V+1) for _ in range(V+1)] # 인접행렬

for i in range(E):
  v1, v2 = arr[i*2], arr[i*2+1]
  adjM[v1][v2] = 1
  adjM[v2][v1] = 1

  adjL[v1].append(v2)
  adjL[v2].append(v1)
```

## Backtracking(백트래킹)
- 여러 가지 선택지들이 존재하는 상황에서 한 가지를 선택한다.
- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
- 이런 선택을 반복하면서 최종 상태에 도달한다.
  - 올바른 선택을 계속하면 goal state에 도달  
![image](https://user-images.githubusercontent.com/108309396/228709758-cf2d6d7a-8833-4cd6-963a-061d6057fbb0.png)

## BFS(Breadth First Search, 너비 우선 탐색)
- 탐색 시작점의 인접한 정점들을 먼저 차례로 방문한 뒤에 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- Queue 활용
```python
def BFS(G, v):  # 그래프 G, 탐색 시작점 v
  visited = [0] * (n+1)   # n: 정점의 개수
  queue = []              # 큐 생성
  queue.append(v)         # 시작점 v를 큐에 삽입
  while queue:            # 큐가 비어있지 않은 경우
    t = queue.pop(0)      # 큐의 첫 번째 원소 반환
    if not visited[t]:    # 방문되지 않은 곳이라면
      visited[t] = True   # 방문한 것으로 표시
      visit(t)            # 정점 t에서 할 일
      for i in G[t]:      # t와 연결된 모든 정점에 대해
        if not visited[i]:  # 방문되지 않은 곳이라면
          queue.append(i)   # 큐에 넣기
```

### BFS 구현
![1](https://user-images.githubusercontent.com/108309396/220223708-34a088e8-dcfc-4b04-bbc6-9456e2bb8bd9.png)  
![2](https://user-images.githubusercontent.com/108309396/220223713-5794449d-68a3-4ad6-ba21-e25693ec451c.png)  
![3](https://user-images.githubusercontent.com/108309396/220223714-2dd75378-cf16-43da-9d90-080e412f4d3e.png)  
![4](https://user-images.githubusercontent.com/108309396/220223716-cd161134-4680-4742-98ac-36938e214134.png)  
![5](https://user-images.githubusercontent.com/108309396/220223719-32bec32f-2c5d-43c6-b4e2-7653363e6785.png)  
![6](https://user-images.githubusercontent.com/108309396/220223720-cec5688f-d2f6-4f6e-9ce2-0aa798089bb4.png)  
![7](https://user-images.githubusercontent.com/108309396/220223723-7f3c0a35-344b-407e-bfba-bcf7feb40c5a.png)  
![8](https://user-images.githubusercontent.com/108309396/220223724-f9560a58-528e-4d19-92a5-f99dff88ac0b.png)  
![9](https://user-images.githubusercontent.com/108309396/220223727-af3b64b2-81fa-400e-8fee-f396d64aa491.png)  
![10](https://user-images.githubusercontent.com/108309396/220223729-2b6fa9f6-519f-43ce-ab19-3b6ad1ecf70b.png)  
![11](https://user-images.githubusercontent.com/108309396/220223731-d92bf7c5-a73c-474e-9126-bc67d405f0c3.png)  


# BFS 참고
```python
def BFS(G, v):  # 그래프 G, 탐색 시작점 v
  visited = [0] * (n+1)   # n: 정점의 개수
  queue = []              # 큐 생성
  queue.append(v)         # 시작점 v를 큐에 삽입
  visited[v] = 1        # 시작점 enqueue되었음을 표시
  while queue:            # 큐가 비어있지 않은 경우
    t = queue.pop(0)      # 큐의 첫 번째 원소 반환
    visit(t)              # 정점 t에서 할 일
      for i in G[t]:      # t와 연결된 모든 정점에 대해
        if not visited[i]:  # 방문되지 않은 곳이라면
          queue.append(i)   # 큐에 넣기
          visited[i] = visited[t] + 1   # n으로부터 1만큼
```