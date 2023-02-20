# Queue
- 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만 하고, 앞에서는 삭제만 이루어지는 구조
- FIFO(First in First Out), 선입선출구조
- 기본 연산: 삽입(enQueue), 삭제(deQueue)  
![1](https://user-images.githubusercontent.com/108309396/219995789-a79c99df-e199-4ff1-8d5c-0f5c05cf0502.png)
![2](https://user-images.githubusercontent.com/108309396/219995795-a78e0bd5-7cae-4980-ab51-9c1d27c4080c.png)

## 큐의 연산 과정  
![3](https://user-images.githubusercontent.com/108309396/219995798-9c4c1c64-bc3e-434b-a064-e494460315e6.png)
![4](https://user-images.githubusercontent.com/108309396/219995802-fbb708dd-0160-4f05-aafe-9b9d9aa4ab4f.png)

## 선형 큐
- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front: 마지막으로 삭제된 원소의 인덱스
  - rear: 저장된 마지막 원소의 인덱스
- 상태 표현
  - 초기 상태: `front = rear = -1`
  - 공백 상태: `front == rear`
  - 포화 상태: `rear == n - 1`(n: 배열의 크기, n-1: 배열의 마지막 인덱스)

## 선형 큐의 구현
- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front와 rear를 -1로 초기화
- 삽입: enQueue(item)
  - rear값을 하나 증가
  - 그 인덱스에 해당하는 배열 원소 Q[rear]에 item 저장
```python
def enQueue(item):
  global rear
  if isFull():
    print('Queue_Full')
  else:
    rear += 1
    Q[rear] = item
```
- 삭제: deQueue()
  - front값을 하나 증가
  - 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능 수행
```python
def deQueue():
  if isEmpty():
    print('Queue_Empty')
  else:
    front += 1
    return Q[front]
```
- 공백상태 및 포화상태 검사: isEmpty(), isFull()
```python
def isEmpty():
  return front == rear

def isFull():
  return rear == len(Q) - 1
```
- 검색: Qpeek()
  - 가장 앞에 있는 원소를 검색하여 반환하는 연산
  - 현재 front의 바로 뒤에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환
```python
def Qpeek():
  if isEmpty():
    print('Queue_Empty')
  else:
    return Q[front+1]
```

- 선형 큐 이용시의 문제점
  - 잘못된 포화상태 인식
  - 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 rear=n-1인 포화상태로 인식하여 더 이상의 삽입 수행X   
![1](https://user-images.githubusercontent.com/108309396/219999259-e66eda83-b42c-473c-b8cb-939e1be80633.png)
- 해결방법 1
  - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 이동
  - 원소 이동에 많은 시간이 소요되어 큐의 효율성 &darr;  
![2](https://user-images.githubusercontent.com/108309396/219999265-72656664-09dc-4718-89ab-15d7653ee3ee.png)
- 해결방법 2
  - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형의 큐를 이룬다고 가정하고 사용

## 원형 큐
- 초기 공백 상태
  - front = rear = 0
- Index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 0으로 이동해야 함.
  - mod 사용
- front 변수
  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용X, 빈 자리로 둠  
![3](https://user-images.githubusercontent.com/108309396/219999269-53b844e3-6611-4cc2-a4ff-fb445a4b2c8f.png)

## 원형 큐의 구현
- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front와 rear를 0으로 초기화
- 삽입: enQueue(item)
  - rear = (rear + 1)mod n
  - 그 인덱스에 해당하는 배열 원소 cQ[rear]에 item 저장
```python
def enQueue(item):
  global rear
  if isFull():
    print('Queue_Full')
  else:
    rear = (rear + 1) % len(cQ)
    cQ[rear] = item
```
- 삭제: deQueue()
  - front값을 하나 증가
  - 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능 수행
```python
def deQueue():
  global front
  if isEmpty():
    print('Queue_Empty')
  else:
    front = (front + 1) % len(cQ)
    return cQ[front]
```
- 공백상태 및 포화상태 검사: isEmpty(), isFull()
  - 공백상태: `front == rear`
  - 포화상태: 삽입할 rear의 다음 위치 == 현재 front &rarr; `(rear + 1)mod n == front`
```python
def isEmpty():
  return front == rear

def isFull():
  return (rear + 1) % len(cQ) == front
```

# 우선순위 큐
- 우선순위를 가진 항목들을 저장하는 큐
- 우선순위가 높은 순서대로 먼저 나감
# 큐의 활용: 버퍼
# BFS