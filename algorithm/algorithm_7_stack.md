# Stack
- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 선형구조임
  - 선형구조: 자료 간의 관계가 1대1의 관계를 갖는다
  - 비선형구조: 자료 간의 관계가 1대N의 관계를 갖는다(ex. 트리)
- 스택에 자료를 삽입하거나 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 
- **LIFO(Last-In-First-Out)**

## 스택의 구현
- 배열 사용 가능
- 저장소 자체를 스택이라 부르기도 한다
- 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.
- 연산
  - 삽입: `push` &rarr; `append`(느림..)
  - 삭제: `pop`
  - 스택이 공백인지 아닌지를 확인하는 연산: `isEmpty`
  - 스택의 top에 있는 item(원소)을 반환하는 연산: `peek`  
![1](https://user-images.githubusercontent.com/108309396/218358919-3b755e3c-4613-44fd-9c0b-aa08338a540a.png)
```python
def push(item, size):
  global top
  top += 1
  if top == size:
    print('overflow!')
  else:
    stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1        # push(20)
stack[top] = 20
```
```python 
def pop():
  if len(s) == 0:
    # underflow
    return
  else:
    return s.pop()

print(pop())

if top > -1:       # pop()
  top -= 1
  print(stack[top + 1])
```

## 스택 구현 고려 사항
- 1차원 배열을 사용하여 구현할 경우 구현에 용이하지만 스택의 크기를 변경하기가 어려움
- Solution: 저장소를 동적으로 할당하면 됨 &rarr; 동적 연결리스트를 이용하여 구현
  - 단점: 구현이 복잡함
  - 장점: 메모리를 효율적으로 사용

# Function call
- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 LIFO 구조이므로, 스택을 이용하여 수행순서 관리
  - 함수 호출 발생 시, 호출한 함수 수행에 필요한 local variable, parameter 및 수행 후 복귀할 주소 등의 정보를 stack frame에 저장하여 시스템 스택에 삽입
  - 함수의 실행이 끝나면 시스템 스택의 top 원소(스택 프레임)를 pop하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.    
  - Program Counter(PC)가 프로그램의 수행 순서 및 주소를 관리함
  - stack의 내용은 pop되면서 삭제되는 것이 아닌  Stack Pointer가 top을 찍는 위치에 따라 pop된다고 보는 것  
![2](https://user-images.githubusercontent.com/108309396/218360971-ededd3c4-c04f-4c28-baff-34040d42ec5f.png)

## 재귀호출
- 자기 자신을 호출하여 순환 수행되는 것
- 프로그램의 크기를 줄이고 간단하게 작성 가능
- factorial, fibonacci

# Memoization
- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법(DP)의 핵심이 됨   
![11](https://user-images.githubusercontent.com/108309396/218609313-04d3ab5a-c019-4459-9002-3ff38d8623e0.png)

# DP(Dynamic Programming)
- 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
- 동적 계획법은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.
- 피보나치 수 DP 적용 알고리즘
```python
def fibo2(n):
  f = [0] * (n + 1)
  f[0] = 0
  f[1] = 1
  for i in range(2, n + 1):
    f[i] = f[i-1] + f[i-2]
  return f[n]
```

## DP의 구현 방식
- recursive 방식: fibo1()
- iterative 방식: fibo2()
- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 효율적
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.

# 계산기
- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산 가능
- stack을 이용한 계산기 요약
  - 중위 표기법을 후위 표기법으로 변경(스택 이용)
  - 후위 표기법의 수식을 스택을 이용하여 계산
1. 중위표기법(infix notation): `A + B`
2. 후위표기법(postfix notation): `AB+`

### 중위표기법을 후위표기법으로 변환하는 알고리즘
- 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높고, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음  
![1](https://user-images.githubusercontent.com/108309396/218896453-3751b191-5c6d-423a-a7ea-b2643979efe8.png)  
![2](https://user-images.githubusercontent.com/108309396/218896456-19d6b141-1787-4799-8fb4-f7e0683435e1.png)
![3](https://user-images.githubusercontent.com/108309396/218896458-253c8406-bb47-4ae1-8a7b-4de6cbc632e0.png)  
![4](https://user-images.githubusercontent.com/108309396/218896459-13bb6da5-b216-412b-96a9-f4a3204c047e.png)
![5](https://user-images.githubusercontent.com/108309396/218896460-bdd8ea0d-1f3b-4309-aea7-7c0aa5d4034c.png)  
![6](https://user-images.githubusercontent.com/108309396/218896461-b8462795-e351-4210-a82a-feec751f8c8b.png)
![7](https://user-images.githubusercontent.com/108309396/218896463-59731795-1c26-4172-93ef-da6fa2e5d7a1.png)  
![8](https://user-images.githubusercontent.com/108309396/218896465-a4cfeaa9-083e-416c-9b84-fa58f03f9f0e.png)
![9](https://user-images.githubusercontent.com/108309396/218896468-2a4dab25-aaad-4592-b6f2-25cb55e5003e.png)  
![10](https://user-images.githubusercontent.com/108309396/218896470-57194570-0f89-489a-9385-9a145c94de2e.png)
![11](https://user-images.githubusercontent.com/108309396/218896473-b6cb15b4-4369-43cc-9971-d964fe326022.png)


### 후위표기법을 계산하는 알고리즘
![1](https://user-images.githubusercontent.com/108309396/218897077-4d1e1bc9-b641-473b-890d-6d6eec6db9c0.png)
![2](https://user-images.githubusercontent.com/108309396/218897080-ba1cf446-5f9e-4ca2-9401-764506e2cb0c.png)  
![3](https://user-images.githubusercontent.com/108309396/218897081-afc26242-b406-487c-8ef6-b575f0e54fef.png)
![4](https://user-images.githubusercontent.com/108309396/218897082-d858166b-94a1-4bb4-9497-8dfc85d3dcc4.png)  
![5](https://user-images.githubusercontent.com/108309396/218897083-80fbb49d-1d9c-46e3-a5cd-d2fbf43cce9f.png)
![6](https://user-images.githubusercontent.com/108309396/218897085-6c17db60-b1b6-4cc2-ba7b-aa19b235ad87.png)

# 백트래킹(Backtracking)
- 해를 찾는 도중에 '막히면' 되돌아가서 다시 해를 찾아가는 기법
- optimization, decision 문제를 해결할 수 있다
- decision 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes'또는 'no'로 답하는 문제

## 백트래킹과 DFS의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 나아가지 않음으로써 시도의 횟수를 줄임 &rarr; **Pruning 가지치기**
- DFS가 모든 경로를 추적하는 반면 백트래킹은 불필요한 경로를 조기에 차단
- DFS는 경우의 수가 너무 많음
- 백트래킹의 경우 DFS보다 일반적으로 경우의 수가 줄어들지만 최악의 경우에는 여전히 Exponential time을 요함

## 백트래킹 과정
1. 상태 공간 트리의 DFS를 실시
2. 각 노드가 유망한지(promising) 점검
3. 만약 그 노드가 유망하지 않다면, 부모노드로 돌아가 다음 자식 노드를 통해 검색을 계속함
- 유망성: 어떤 노드를 방문하였을 떄 그 노드를 포함한 경로가 해답이 될 수 없으면 유망하지 않다고 하고, 반대로 해답의 가능성이 있으면 유망하다고 한다.

## 미로찾기 알고리즘
![1](https://user-images.githubusercontent.com/108309396/218905982-c5ca2630-2751-49e2-9c21-ae3b283a96b4.png)  
![2](https://user-images.githubusercontent.com/108309396/218905984-9dff117e-98ad-4408-b464-7a7bdf8bb998.png)  
![3](https://user-images.githubusercontent.com/108309396/218905987-41cdd451-d66a-4219-9cff-5cdb1d15241d.png)  

## 일반적인 백트래킹 코드
![4](https://user-images.githubusercontent.com/108309396/218905988-5eae6dad-7324-4862-99a7-3803c86a9e13.png)

## 부분집합 구하기
- 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 powerset이라고 하며 집합의 원소 개수가 n일 때 부분집합의 개수는 $2^n$개이다.
- 백트래킹 기법으로 powerset 구하기
  - True 또는 False값을 가지는 항목들로 구성된 n개의 배열을 만든다.
  - 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타냄  
![1313](https://user-images.githubusercontent.com/108309396/218907476-d75ec497-eebd-4d77-ba7f-a3b1ecee4577.png)    
![134134](https://user-images.githubusercontent.com/108309396/218908166-ef4e4d74-9398-4ea4-ade0-a86cd29bfbd2.png)  
![1414](https://user-images.githubusercontent.com/108309396/218907837-b561add3-dd48-484f-96dc-b842d65f1799.png)

### 부분집합의 합
- 부분집합을 모두 생성하고 구하는 방법
```python
def f(i, k, key):
  if i == k:    # 하나의 부분집합 완성
    s = 0

    for j in range(k):
      if bit[j]:
        s += A[j]   # 부분집합의 합

    if s == key:  # 합이 key와 같은 부분집합을 출력
      for j in range(k):
        if bit[j]:
          print(A[j], end=' ')
      print()

  else:
    bit[i] = 1
    f(i+1, k, key)
    bit[i] = 0
    f(i+1, k, key)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
bit = [0] * N
f(0, N)
```
- 백트래킹
```python
def f(i, k, s, t):  # i 원소, k 집합의 크기, s i-1까지 고려된 합, t 찾고자 하는 합(목표)
  global cnt
  if s > t:         # 고려한 원소의 합이 찾는 합보다 큰 경우
    return
  elif s == t:      # 남은 원소를 고려할 필요가 없는 경우
    cnt += 1
    return
  elif i == k:      # 모든 원소 고려됨
    return
  else:
    f(i+1, k, s+A[i], t)  # A[i] 포함
    f(i+1, k, s, t)       # A[i] 미포함

N = 10
A = [i for i in range(1, N+1)]
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 10
cnt = 0
bit = [0] * N
f(0, N, 0, key)
print(cnt)    # 합이 key인 부분집합의 수
```


## 순열 구하기 
![33333](https://user-images.githubusercontent.com/108309396/218908177-de0e2d60-2a4f-469f-8e3c-75bb245e92ba.png)   
![111](https://user-images.githubusercontent.com/108309396/218908172-cd2684c1-06d9-4efe-90f4-24d472f0a276.png)  
![222](https://user-images.githubusercontent.com/108309396/218908174-73b017d1-b2fc-4225-ac76-8dc7e9de4682.png)  

## 순열 생성
```python
def f(i, k):
  if i == k:
    print(p)
  else:
    for j in range(i, k): # 자기자신의 오른쪽과 교환해 감
      p[i], p[j] = p[j], p[i]
      # p[i] 결정, p[i]와 관련된 작업 가능
      f(i+1, k)
      p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = len(p)
f(0, N)
```