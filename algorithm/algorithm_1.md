# [Array 1]
## 알고리즘
- 알고리즘이란?
  - 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
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
  - Big-O Notation
    - 가장 큰 영향력을 주는 n에 대한 항만을 표시
    - coefficient는 생략  
![화면 캡처 2023-02-01 091323](https://user-images.githubusercontent.com/108309396/215913409-99f7bdbe-df18-4c25-ab29-427516c568a9.png)

## 배열
- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

## 정렬
- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(ascending) 혹은 그 반대의 순서대로(descending) 재배열하는 것
- 정렬 방식의 종류
  - Bubble Sort
  - Counting Sort
  - Selection Sort
  - Quick Sort
  - Insertion Sort
  - Merge Sort

## 버블 정렬(Bubble Sort)
![버블정렬](https://user-images.githubusercontent.com/108309396/216204091-3d5a0582-01bf-4e5d-98be-dbf5f8589be9.png)
- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 정렬과정
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
  - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 함
- 시간 복잡도: $O(n^2)$  
```python
'''
5
55 7 78 12 42
for i: N-1 -> 1 # 각 구간의 끝
    for j: 0 -> i-1 # 비교할 왼쪽
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1] # 큰 원소 오른쪽으로
7 12 42 55 78
'''
N = int(input())
arr = list(map(int, input().split()))
for i in range(N-1, 0, -1): # 각 구간의 끝
    for j in range(i): # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] # 큰 원소  오른쪽으로

print(*arr)
7 12 42 55 78
```
## 카운팅 정렬(Counting Sort)
### 카운팅 정렬 과정
![count1](https://user-images.githubusercontent.com/108309396/216209161-8da8d33a-48f7-46d3-84eb-a0741b9ce214.png)
![cnt2](https://user-images.githubusercontent.com/108309396/216209163-915e5098-3be8-44a1-be0d-bcf7e3c212a3.png)
![cnt3](https://user-images.githubusercontent.com/108309396/216209166-14964c75-47ec-435e-b554-8a856497e9db.png)
![cnt4](https://user-images.githubusercontent.com/108309396/216209170-82079505-5c6d-466a-923d-4678e7bd4b78.png)  
- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한 사항
  - **정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능**: 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
- 시간 복잡도
  - $O(n+k)$: n은 리스트 길이, k는 정수의 최댓값
```python
def CountingSort(A, B, k):
# A[] -- 입력 배열(0 to k)
# B[] -- 정렬된 배열
# C[] -- 카운트 배열
  C = [0] * (k + 1)

  for i in range(len(A)):
    C[A[i]] += 1 # count 배열에 넣기
  
  for i in range(len(C)):
    C[i] += C[i-1] # count 배열을 누적합 저장 배열로
  
  for i in range(len(B)-1, -1, -1): # 뒤에서부터 정렬
    C[A[i]] -= 1 # 해당 인덱스 카운트를 하나씩 줄여감 
    B[C[A[i]]] = A[i] # 정렬 배열 해당 인덱스에 넣음
```

# 시간복잡도 비교
<img src="https://user-images.githubusercontent.com/108309396/216209392-a2834b9b-be09-47c4-be08-e23cb3f8f049.png" width="80%" height="50%"/>

## Brute Force Algorithm 완전검색
- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- Brute-force
- 일반적으로 경우의 수가 상대적으로 작을 때 유용
- 수행 속도는 느리지만 해답을 찾아내지 못할 확률이 적다
- 
## Greedy Algorithm 탐욕 알고리즘
- 특정 문제에 대한 해법이라기보단 알고리즘, 접근 방법의 분류
- 최적해를 구하는데 사용되는 근시안적인 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달
- 각 선택의 시점에서 이루어지는 결정은 local에서 최적일지라도 그것이 최종적으로 최적이라는 보장X

### 동작 과정
1) 해 선택: 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(solution set)에 추가
2) 실행 가능성 검사: 새로운 부분해 집합이 실행 가능한지를 확인. 문제의 제약 조건을 위반하지 않는지 검사
3) 해 검사: 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1.부터 다시 시작.