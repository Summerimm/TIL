# 2차원 배열
- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언
- 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

## 배열 순회
- $n\times m$ 배열의 n * m개의 모든 원소를 빠짐없이 조사하는 방법
- 행 우선 순회
```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
  for j in range(m):
    Array[i][j] # 필요한 연산 수행
```
- 열 우선 순회
```python
for j in range(m):
  for i in range(n):
    Array[i][j]
```
- 지그재그 순회
```python
for i in range(n):
  for j in range(m):
    Array[i][j + (m-1-2*j) * (i%2)]
```
- **델타를 이용한 2차 배열 탐색**
  - 2차 배열의 한 좌표에서 4방향의 인접 요소를 탐색하는 방법
  - ![화면 캡처 2023-02-06 104700](https://user-images.githubusercontent.com/108309396/216863342-161f9715-b99a-4b26-ab05-904b74844f25.png)

- 전치 행렬
```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
  for j in range(3):
    if i < j:
      arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# arr = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### 비트 연산자
- `&`: 비트 단위로 AND 연산을 한다.
- `|`: 비트 단위로 OR 연산을 한다.
- `<<`: 피연산자의 비트 열을 왼쪽으로 이동
- `>>`: 피연산자의 비트 열을 오른쪽으로 이동

### << 연산자
- `1 << n`: $2^n$ 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미

### & 연산자
- `i & (1 << j)`: i의 j번째 비트가 1인지 아닌지를 검사  
- 부분집합을 생성하는 방법  
![화면 캡처 2023-02-06 143255](https://user-images.githubusercontent.com/108309396/216891496-01014c76-95fd-4797-b278-1f3080a97be3.png)
