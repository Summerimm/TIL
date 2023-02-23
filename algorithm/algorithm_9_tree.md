# Tree
- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층 관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 나무 모양의 구조

### 트리의 정의
  - 한 개 이상의 노드로 이루어진 유한 집합
    - 노드 중 최상위 노드: 루트(root)
    - 나머지 노드들은 n(>=0)개의 분리 집합 T1, ...,TN으로 분리될 수 있다.
    - 이들은 각각 하나의 트리가 되며(재귀적 정의) 루트의 subtree라 한다.

### 트리 용어 정리
- `node`: 트리의 원소
- `edge`: 노드를 연결하는 선
- `root node`: 트리의 시작 노드
- `sibling node`: 같은 부모노드의 자식노드들
- `ancestor node`: 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- `subtree`: 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- `descendent node`: 서브 트리에 있는 하위 레벨의 노드들
- `degree(차수)`
  - 노드의 degree: 노드에 연결된 자식 노드의 수
  - 트리의 degree: 트리에 있는 노드의 차수 중에서 가장 큰 값
  - `leaf node`: 차수가 0인 노드, 자식노드X
- `level(높이)`
  - 노드의 level: 루트에서 노드에 이르는 간선의 수, 노드의 레벨
  - 트리의 level: 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨

## 이진 트리
- 모든 노드들이 2개의 subtree를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대 2개까지만 가질 수 있음
  - left/right child node
- 특성
  - 레벨 i에서의 노드의 최대 개수는 $2^i$개
  - 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 $(h+1)$개, 최대 개수는 $(2^{h+1}-1)$개가 된다.

### 이진 트리의 종류
- `포화 이진 트리(Full Binary Tree)`
  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
  - 높이가 h일 때 최대 노드 개수인 $(2^{h+1}-1)$개의 노드를 가진 이진 트리
  - 루트를 1번으로 하여  $2^{h+1}-1$까지 정해진 위치에 대한 노드 번호를 가짐
- `완전 이진 트리(Complete Binary Tree)`
  - 높이가 h이고 노드 수가 n개 일 때,(단, $2^h <= n < 2^{h+1}-1$) 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- `편향 이진 트리(Skewed Binary Tree)`
  - 높이 h에 대한 최소 개수의 노드를 가지면서($h+1$) 한쪽 방향의 자식 노드만을 가진 이진 트리
  - 왼쪽 편향/오른쪽 편향 이진 트리

### 이진 트리 - 순회(Traversal)
- 순회(traversal): 트리의 노드들을 체계적으로 방문하는 것
  - 전위순회(preorder traversal): VLR
    - root-left-right
  - 중위순회(inorder traversal): LVR
    - left-root-right
  - 후위순회(postorder traversal): LRV
    - left-right-root

### 전위순회(preorder traversal)
- 현재 노드 n을 방문하여 처리 &rarr; V
- 현재 노드 n의 왼쪽 서브트리로 이동 &rarr; L
- 현재 노드 n의 오른쪽 서브트리로 이동 &rarr; R
```python
def preorder(T):
  if T:   # T is not None
    visit(T)    # print(T.item)
    preorder(T.left)
    preorder(T.right)
```

### 중위순회(inorder traversal)
- 현재 노드 n의 왼쪽 서브트리로 이동 &rarr; L
- 현재 노드 n을 방문하여 처리 &rarr; V
- 현재 노드 n의 오른쪽 서브트리로 이동 &rarr; R
```python
def inorder(T):
  if T:   # T is not None
    preorder(T.left)
    visit(T)    # print(T.item)
    preorder(T.right)
```

### 후위순회(postorder traversal)
- 현재 노드 n의 왼쪽 서브트리로 이동 &rarr; L
- 현재 노드 n의 오른쪽 서브트리로 이동 &rarr; R
- 현재 노드 n을 방문하여 처리 &rarr; V
```python
def inorder(T):
  if T:   # T is not None
    preorder(T.left)
    preorder(T.right)
    visit(T)    # print(T.item)
```

## 이진 트리의 표현
- 배열을 이용한 이진 트리의 표현
  - 이진 트리에 각 노드 번호를 부여
  - 루트의 번호를 1로
  - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 $2^n$부터 $2^{n+1}$까지 번호를 부여
- 노드 번호의 성질
  - 노드 번호가 i인 노드의 부모 노드 번호: ${(floor)} i/2$
  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호: $2\times i$
  - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호: $2\times i + 1$
  - 레벨 n의 노드 번호 시작 번호
![1](https://user-images.githubusercontent.com/108309396/220501477-c0c40c84-26c0-4b5a-87bc-ea39c689eb54.png)  
![2](https://user-images.githubusercontent.com/108309396/220501485-50232edb-195c-4571-abf5-5a716159073e.png)  


## 이진 트리의 저장
![3](https://user-images.githubusercontent.com/108309396/220501488-346f063d-d6e6-46c8-9258-41aed800bfa1.png)  
![4](https://user-images.githubusercontent.com/108309396/220501489-4533eea3-af77-4d11-9d89-40a1c14d0cbc.png)  
![5](https://user-images.githubusercontent.com/108309396/220501490-8298fcc4-c9ee-4af2-94f7-067d13f2dd21.png)  
- 배열을 이용한 이진 트리의 표현의 단점
  - 편향 이진 트리의 경우 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경이 어려워 비효율적
- 연결리스트
  - 연결 자료구조를 이용한 이진트리의 표현
  - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결리스트 노드를 사용하여 구현
![6](https://user-images.githubusercontent.com/108309396/220501494-b974deae-fbdb-42cb-8bc1-ad6b36e811f9.png)  

## 수식 트리
- 수식을 표현하는 이진 트리
- Expression Binary Tree
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드
![1](https://user-images.githubusercontent.com/108309396/220812475-48c49ac5-8f98-4353-92ec-a30411905be6.png)


## 이진탐색 트리
- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖는다.
- key(왼쪽 서브트리) < key(루트노드) < key(오른쪽 서브트리)
- **중위순회**하면 오름차순으로 정렬된 값을 얻을 수 있음
![2](https://user-images.githubusercontent.com/108309396/220812478-702964aa-5d90-45f1-bcab-0803008ea07a.png)  
- 시간복잡도
![3](https://user-images.githubusercontent.com/108309396/220812482-e5137818-ee8f-442d-b32f-91c7e09ecbbd.png)  
![4](https://user-images.githubusercontent.com/108309396/220812485-8b088f20-c655-48db-8150-828bef9ae6f6.png)

## 힙
- `완전 이진 트리`에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대 힙(max heap)
  - 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키값 > 자식 노드의 키값
  - 루트 노드: 키값이 가장 큰 노드
- - 최소 힙(min heap)
  - 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키값 < 자식 노드의 키값
  - 루트 노드: 키값이 가장 작은 노드

### 힙 연산 - 삽입
![5](https://user-images.githubusercontent.com/108309396/220812486-679e5c2f-e59d-41db-900a-0704697870fa.png)  

### 힙 연산 - 삭제
- 힙에서는 루트 노드의 원소만을 삭제할 수 있다.
- 루트 노드의 원소를 삭제하여 반환한다.
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.