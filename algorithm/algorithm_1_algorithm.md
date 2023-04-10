# Algorithm
- 알고리즘이란?
  - 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 
  - 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 알고리즘을 표현하는 방법
  - Pseudocode(의사코드) / 순서도  
  ![순서도](https://user-images.githubusercontent.com/108309396/216204097-242c6129-4aa2-45e6-ab1a-da79ae4559c7.png)
- 좋은 알고리즘의 조건
  - 정확성
  - 작업량
  - 메모리 사용량
  - 단순성
  - 최적성
- 어떤 알고리즘을 사용해야 하는가?
  - 알고리즘의 성능 분석 필요
- 시간복잡도(Time Complexity)
  - 실제 걸리는 시간을 측정
  - 실행되는 명령문의 개수를 계산
  - **Big-O Notation**
    - 가장 큰 영향력을 주는 n에 대한 항만을 표시
    - coefficient는 생략  
![화면 캡처 2023-02-01 091323](https://user-images.githubusercontent.com/108309396/215913409-99f7bdbe-df18-4c25-ab29-427516c568a9.png)

## Brute Force Algorithm 완전검색
- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- 일반적으로 경우의 수가 상대적으로 작을 때 유용
- 수행 속도는 느리지만 해답을 찾아내지 못할 확률이 적다

## Greedy Algorithm 탐욕 알고리즘
- 특정 문제에 대한 해법이라기보단 알고리즘, 접근 방법의 분류
- 최적해를 구하는데 사용되는 근시안적인 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달
- 각 선택의 시점에서 이루어지는 결정은 local에서 최적일지라도 **그것이 최종적으로 최적이라는 보장X**

### 동작 과정
1) 해 선택: 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(solution set)에 추가
2) 실행 가능성 검사: 새로운 부분해 집합이 실행 가능한지를 확인. 문제의 제약 조건을 위반하지 않는지 검사
3) 해 검사: 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1.부터 다시 시작.

### 탐욕 알고리즘의 필수 요소
- Greedy choice property
  - 탐욕적 선택은 최적해로 갈 수 있음을 보여라 &rarr; 즉, 탐욕적 선택은 항상 안전함
- Optimal substructure property
  - 최적화 문제를 정형화하라
  - 하나의 선택을 하면 풀어야 할 하나의 하위 문제가 남는다.
- **원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해**

### Greedy와 DP의 비교
![image](https://user-images.githubusercontent.com/108309396/228117647-1f26694f-92f0-48e6-895a-efb06921d85c.png)

### 대표적인 탐욕 기법의 알고리즘
![image](https://user-images.githubusercontent.com/108309396/228117706-ec87506e-25a2-4a60-9226-2d5cca9e8665.png)

## 재귀적 알고리즘
- 두 부분으로 나뉜다
- 하나 또는 그 이상의 기본 경우(basis case or rule)
  - 집합에 포함되어 있는 원소로 induction을 생성하기 위한 seed 역할
- 하나 또는 그 이상의 유도된 경우(inductive case or rule)
  - 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법
- **입력값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적**

### 재귀 함수(recursive function)
- 함수 내부에서 직접 혹은 간접적으로 자기 자신을 호출하는 함수
- 기본 부분(basis part)와 유도 부분(inductive part)로 구성
- 함수 호출은 프로그램 메모리 구조에서 스택을 사용
  - 따라서 메모리 및 속도에서 성능저하 발생

### 반복 vs 재귀
![image](https://user-images.githubusercontent.com/108309396/227825443-6f51c8ac-e47b-4288-a785-b277d62d9f7f.png)  


# 분할 정복 알고리즘
- 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
- 통합(Combine): (필요하다면) 해결된 해답을 모은다.  
![image](https://user-images.githubusercontent.com/108309396/228403066-081f6c27-f623-4d56-9654-f1156f9677fc.png)  

### 반복 vs 분할 정복
- 반복(iterative) 알고리즘: $O(n)$  
![image](https://user-images.githubusercontent.com/108309396/228403188-65a2e5ae-2ba9-4653-aa12-8970262ca6f1.png)  
- 분할 정복 기반 알고리즘: $O(log_2n)$  
![image](https://user-images.githubusercontent.com/108309396/228403341-96e4b4eb-a5a9-4511-ba58-42ce0333aa3a.png)  
