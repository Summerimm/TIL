# [Array 1]
## 알고리즘
- 알고리즘이란?
  - 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 알고리즘을 표현하는 방법
  - Pseudocode(의사코드) / 순서도
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
## 완전검색
## 그리디()