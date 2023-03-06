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
- 각 선택의 시점에서 이루어지는 결정은 local에서 최적일지라도 그것이 최종적으로 최적이라는 보장X

### 동작 과정
1) 해 선택: 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(solution set)에 추가
2) 실행 가능성 검사: 새로운 부분해 집합이 실행 가능한지를 확인. 문제의 제약 조건을 위반하지 않는지 검사
3) 해 검사: 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1.부터 다시 시작.