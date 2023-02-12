# Pattern Matching
## Brute Force
- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식  
![1](https://user-images.githubusercontent.com/108309396/217691479-eff9689f-1eeb-4fbc-89a2-76ad0eb13859.png)

```python
p = "is" # 찾을 패턴
t = "This is a book~!"
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
  i = 0 # t의 인덱스
  j = 0 # p의 인덱스
  while j < M and i < N:
    if t[i] != p[j]:
      i = i - j
      j -= 1
    i = i + 1
    j = j + 1
  if j == M: return i - M # 검색 성공
  else: return -1 # 검색 실패
```
### 시간복잡도
- Worst Case: 텍스트의 모든 위치에서 비교해야 하므로 $O(MN)$

## KMP 알고리즘
- 불일치가 발생한 text string의 앞부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함
  - next[M]: 불일치가 발생했을 경우 이동할 다음 위치
- 시간복잡도: $O(M+N)$  
![2](https://user-images.githubusercontent.com/108309396/217695889-cdfacaa0-6f12-449c-9da5-6d6934c67001.png)

## 보이어-무어 알고리즘
- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 패턴에 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이 만큼이 된다.  
![3](https://user-images.githubusercontent.com/108309396/217696434-2843b69b-97a8-408c-b7f0-37d11fe65765.png)
- 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재할 경우  
![4](https://user-images.githubusercontent.com/108309396/217696679-1dd15a3c-67c7-4441-9773-6a0cc0358438.png)
- 예시
![5](https://user-images.githubusercontent.com/108309396/217696685-ea0298ec-7b05-4051-bcbb-93ba3d16b677.png)

### 문자열 매칭 알고리즘 비교
- 찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
- Brute Force algorithm: $O(mn)$
- 카프-라빈 algorithm: $theta(n)$
- KMP algorithm: $theta(n)$
- 보이어-무어 algorithm
  - 위의 매칭 알고리즘들은 최선의 경우에도 $omega(n)$
  - 보이어-무어는 텍스트 문자를 다 보지 않아도 된다
  - 발상의 전환: 패턴의 오른쪽부터 비교
  - 최악의 경우: $theta(mn)$
  - 입력에 따라 다르지만 일반적으로 $theta(mn)$보다 시간이 덜 든다

## 문자열 암호화
### Caesar cipher
- 평문에서 사용되고 있는 알파벳을 일정한 문자 수만큼 **평행이동**시킴으로써 암호화
- 5만큼 평행이동했을 때 5를 키 값이라고 한다.
- 카이사르 암호문에 대한 전사 공격이 가능  
<img width="70%" alt="스크린샷 2023-02-13 오전 12 22 46" src="https://user-images.githubusercontent.com/108309396/218319960-16ecdfea-2289-4dae-8234-8ab935779cf1.png">


### 문자 변환표를 이용한 암호화(단일 치환 암호)
- 단순한 카이사르 암호화보다 훨씬 강력
- 복호화하기 위해서는 모든 키의 조합이 필요(`26!`)  
![7](https://user-images.githubusercontent.com/108309396/217698685-b50c2f57-5282-4e3d-b5cf-867da2d7ee9b.png)

### bit열의 암호화
- XOR(exclusive-or) 연산 사용  
![8](https://user-images.githubusercontent.com/108309396/217698681-e647d9c8-42e6-447b-96a9-3688c44ed37a.png)


## 문자열 압축
- Run-length encoding algorithm
- 같은 값이 몇 번 반복되는가를 나타냄으로써 압축
- BMP 파일 포맷의 압축 방법
- 압축에 더 많이 사용하는 알고리즘으로 허프만 코딩 알고리즘이 있다.  
![9](https://user-images.githubusercontent.com/108309396/217698680-cbb545aa-7e75-47b8-92f9-a6c2805873b2.png)