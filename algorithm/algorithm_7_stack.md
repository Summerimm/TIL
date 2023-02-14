# Stack
- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 선형구조임
  - 선형구조: 자료 간의 관계가 1대1의 관계를 갖는다
  - 비선형구조: 자료 간의 관계가 1대N의 관계를 갖는다(ex. 트리)
- 스택에 자료를 삽입하거나 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 
- **LIFO(Last-In-First-Out)**

### 스택의 구현
- 배열 사용 가능
- 저장소 자체를 스택이라 부르기도 한다
- 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.
- 연산
  - 삽입: `push` &rarr; append(느림..)
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

### 스택 구현 고려 사항
- 1차원 배열을 사용하여 구현할 경우 구현에 용이하지만 스택의 크기를 변경하기가 어려움
- Solution: 저장소를 동적으로 할당하면 됨 &rarr; 동적 연결리스트를 이용하여 구현
  - 단점: 구현이 복잡함
  - 장점: 메모리를 효율적으로 사용

### Function call
- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 LIFO 구조이므로, 스택을 이용하여 수행순서 관리
  - 함수 호출 발생 시, 호출한 함수 수행에 필요한 local variable, parameter 및 수행 후 복귀할 주소 등의 정보를 stack frame에 저장하여 시스템 스택에 삽입
  - 함수의 실행이 끝나면 시스템 스택의 top 원소(스택 프레임)를 pop하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.    
  - Program Counter(PC)가 프로그램의 수행 순서 및 주소를 관리함
  - stack의 내용은 pop되면서 삭제되는 것이 아닌  Stack Pointer가 top을 찍는 위치에 따라 pop된다고 보는 것
![2](https://user-images.githubusercontent.com/108309396/218360971-ededd3c4-c04f-4c28-baff-34040d42ec5f.png)

### 재귀호출
- 자기 자신을 호출하여 순환 수행되는 것
- 프로그램의 크기를 줄이고 간단하게 작성 가능
- factorial, fibonacci

### Memoization
- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법(DP)의 핵심이 됨  
![11](https://user-images.githubusercontent.com/108309396/218609313-04d3ab5a-c019-4459-9002-3ff38d8623e0.png)

## DP(Dynamic Programming)
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

### DP의 구현 방식
- recursive 방식: fib1()
- iterative 방식: fib2()
- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 효율적
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.
