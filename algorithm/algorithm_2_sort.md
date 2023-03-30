# Sort
## 정렬
- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(ascending) 혹은 그 반대의 순서대로(descending) 재배열하는 것
- 정렬 방식의 종류
  - Bubble Sort
  - Counting Sort
  - Selection Sort
  - Quick Sort
  - Insertion Sort
  - Merge Sort

# 버블 정렬(Bubble Sort)
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
for i in range(N-1, 0, -1): # 각 구간의 끝(78부터 확정됨)
    for j in range(i): # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] # 큰 원소 오른쪽으로

print(*arr)
7 12 42 55 78
```

# 카운팅 정렬(Counting Sort)
## 카운팅 정렬 과정
![count1](https://user-images.githubusercontent.com/108309396/216209161-8da8d33a-48f7-46d3-84eb-a0741b9ce214.png)
![cnt2](https://user-images.githubusercontent.com/108309396/216209163-915e5098-3be8-44a1-be0d-bcf7e3c212a3.png)
![cnt3](https://user-images.githubusercontent.com/108309396/216209166-14964c75-47ec-435e-b554-8a856497e9db.png)
![cnt4](https://user-images.githubusercontent.com/108309396/216209170-82079505-5c6d-466a-923d-4678e7bd4b78.png)  
- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한 사항
  - **정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능**: 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  - 카운트들을 위한 충분한 공간을 할당하려면 **집합 내의 가장 큰 정수를 알아야 한다.**
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

# 선택 정렬(Selection Sort)
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 과정
  - 주어진 리스트 중에서 최솟값을 찾는다
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다
- 시간복잡도 $O(n^2)$ 
```python
def selectionSort(arr, N):
  for i in range(N-1):
    minIdx = i
    for j in range(i+1, N):
      if arr[minIdx] > arr[j]:
        minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
``` 

## Selection Algorithm
- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 최댓값, 최솟값 혹은 중간값을 찾는 알고리즘을 의미하기 도 함
- 과정
  - 정렬하기
  - 원하는 순서에 있는 원소 가져오기
- k가 비교적 작을 때 유용 
- $O(kn)$  
```python
def select(arr, k):
  for i in range(k):
    minIdx = i
    for j in range(i+1, len(arr)):
      if arr[minIdx] > arr[j]:
        minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
  return arr[k-1]
``` 

# 퀵 정렬
## 퀵 정렬 요약
- 주어진 배열을 두 개로 분할하고, 각각을 정렬
- 병합 정렬과의 차이점
  - 병합정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할 시 pivot item을 중심으로 작은 것은 왼편으로 큰 것은 오른편에 위치시킴
  - 각 부분 정렬이 끝난 후 병합정렬은 병합(후처리) 필요, 퀵 정렬은 필요X

## 알고리즘
![image](https://user-images.githubusercontent.com/108309396/228694260-3455b1a8-d58d-41b2-af99-0179059b820c.png)  
1. Hoare-Partition 알고리즘
![image](https://user-images.githubusercontent.com/108309396/228694362-cc779300-8083-4d35-92d9-fba6ff5e4eb9.png)
2. Lomuto-Partition 알고리즘
![image](https://user-images.githubusercontent.com/108309396/228694795-eaa33ace-d590-4e4b-ad0a-c5e29eaf892d.png)


## Hoare-Partition 알고리즘 수행과정
![image](https://user-images.githubusercontent.com/108309396/228694401-a6c12482-413b-4425-a40f-d0bf3aa31329.png)  
![image](https://user-images.githubusercontent.com/108309396/228694426-3d4b21d0-48dd-489d-ae7f-75a08e037d51.png)  
![image](https://user-images.githubusercontent.com/108309396/228694564-5a7ca1d6-a905-4bc5-9197-3f3a2ce391fb.png)    
![image](https://user-images.githubusercontent.com/108309396/228694618-d4e5ba48-af0b-430b-b7a8-d62090402cd4.png)  
![image](https://user-images.githubusercontent.com/108309396/228694653-7f410165-6bab-4f0e-a3b9-de03106f1e48.png)  
![image](https://user-images.githubusercontent.com/108309396/228694681-9e8d5a01-bbfc-4df1-98aa-33bb92809dd8.png)  
![image](https://user-images.githubusercontent.com/108309396/228694719-2bb0a358-f20b-4907-8d27-9c804101ffdb.png)  

## Lomuto-Partition 알고리즘 수행과정
![image](https://user-images.githubusercontent.com/108309396/228694831-f6b88f94-cf18-4bc2-9a4b-6adae2e52883.png)  

## 퀵 정렬의 시간복잡도
- In worst case, $O(n^2)$ &rarr; 병합정렬에 비해 좋지 않음
- In average, $O(nlogn)$


# 시간복잡도 비교
![image](https://user-images.githubusercontent.com/108309396/216209392-a2834b9b-be09-47c4-be08-e23cb3f8f049.png)


# 병합 정렬(Merge Sort)
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- top-down 방식
- $O(nlogn)$
![image](https://user-images.githubusercontent.com/108309396/228403475-e49ff7a0-2dab-4d6d-9e08-eaf037083457.png)  
![image](https://user-images.githubusercontent.com/108309396/228403510-b50f4ad7-49db-4630-853b-a71b3eb216f7.png)  

## 구현
### 분할과정
![image](https://user-images.githubusercontent.com/108309396/228403742-d63bdb54-9345-40f7-a5e4-177d281eff93.png)  

### 병합 과정
![image](https://user-images.githubusercontent.com/108309396/228701942-a1f8d8d2-48c9-4a23-8bc0-a5442cabb827.png)