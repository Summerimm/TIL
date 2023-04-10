# Grouping Data
## Aggregate function
- 집계 함수
- 값 집합의 최댓값, 최솟값, 평균, 합계 및 개수를 계산
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결과값을 반환하는 함수
- SELECT문의 GROUP BY절과 함께 종종 사용됨
- 제공하는 함수 목록
  - AVG(), COUNT(), MAX(), MIN(), SUM()
  - COUNT()를 제외하고 나머지는 숫자를 기준으로 계산이 되어져야 하기 때문에 반드시 컬럼의 데이터 타입이 INTEGER일 때만 사용 가능

### `COUNT` 
- users 테이블의 전체 행 수 조회하기  
![image](https://user-images.githubusercontent.com/108309396/230295669-905ce901-4fa8-4f3d-8152-0227a2008400.png)  

### `GROUP BY` clause
![image](https://user-images.githubusercontent.com/108309396/230296853-afdf1092-e0d3-48ad-846c-1b94e0e736a7.png)  
- 특정 그룹으로 묶인 결과를 생성
- 선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로 나타냄
- FROM 절 뒤에 작성
  - WHERE 절이 포함된 경우 WHERE절 뒤에 작성해야 함
- 각 그룹에 대해 aggregate function을 적용하여 추가적인 정보 제공가능

### `COUNT` 참고사항
- COUNT(), COUNT(age), COUNT(last_name) 등 어떤 컬럼을 넣어도 결과는 동일
- 그룹화된 country를 기준으로 카운트 할 경우 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문

# Changing Data
- INSERT, UPDATE, DELETE

## `INSERT` statement
![image](https://user-images.githubusercontent.com/108309396/230301740-eba57d37-8b40-4b2c-b8b5-971b385fa74a.png)    
![image](https://user-images.githubusercontent.com/108309396/230302352-e3ca7422-76a4-4d56-9664-dad2cbc30b1b.png)    
![image](https://user-images.githubusercontent.com/108309396/230302454-aa0e5e9b-3218-46d0-bd85-feb8c5b51b56.png)  
- 새 행을 테이블에 삽입
- 문법 규칙
  1. 먼저 `INSERT INTO` 뒤에 데이터를 삽입할 테이블의 이름을 지정
  2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록 추가
     - 컬럼 목록은 선택 사항이지만 컬럼 목록을 포함하는 것이 권장됨
  3. `VALUES` 키워드 뒤에 쉼표로 구분된 값 목록을 추가
     - **만약 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함**
     - 값 목록의 값 개수는 컬럼 목록의 컬럼 개수와 같아야 함

## `UPDATE` statement
![image](https://user-images.githubusercontent.com/108309396/230302546-c2451267-fdcf-4043-ab85-05568b75db11.png)  
![image](https://user-images.githubusercontent.com/108309396/230302791-6dc1e2c0-49e4-463a-ada8-833b814b747c.png)  
- WHERE절은 선택 사항. 생략하면 테이블의 모든 행에 있는 데이터를 업데이트함
- 선택적으로 `ORDER BY` 및 `LIMIT` 절을 사용하여 업데이트 할 행 수를 지정할 수도 있음

## `DELETE` statement
![image](https://user-images.githubusercontent.com/108309396/230302870-c0059904-734e-4f15-b5c4-14716703033a.png)  
- 테이블에서 행을 제거
- 한 행, 여러 행 및 모든 행을 삭제 가능
- WHERE절은 선택사항이며, 생략하면 테이블의 모든 행을 삭제
- 선택적으로 `ORDER BY` 및 `LIMIT` 절을 사용하여 삭제할 행 수를 지정할 수도 있음  
![image](https://user-images.githubusercontent.com/108309396/230303071-08c6a5cf-37f8-4467-8632-fbb7e2842253.png)  
![image](https://user-images.githubusercontent.com/108309396/230303141-c4623f64-01a8-4f2c-97b8-cf4cbd2c4daf.png)  

# 정규형
## 데이터베이스 정규형
- 데이터베이스를 구조화 하는 방법론
- 데이터의 중복을 최소화하고 일관성과 무결성을 보장하기 위함
- 데이터의 구조를 더 좋은 구조로 바꾸는 것을 **정규화**라고 함
- 관계형 데이터베이스의 경우 6개의 정규형이 있음

## 제 1정규형
- 하나의 속성값이 복수형을 가지면 안 됨
- == 하나의 속성에는 값이 하나만 들어가야 한다.  
![image](https://user-images.githubusercontent.com/108309396/230308956-3030cfa8-9393-485a-85aa-ea2de1ec4a71.png)

## 제 2정규형
- 테이블의 테마와 관련 없는 컬럼은 다른 테이블로 분리하는 것
- 테이블에서 부분 함수적 종속성을 제거한 것
  - 부분 함수적 종속성(Partial Functional Dependency)
  - 키가 아닌 속성이 기본키의 일부분에 종속되는 것  
![image](https://user-images.githubusercontent.com/108309396/230309162-ba1aef0b-f535-41d3-bdb4-70f1f6cc8482.png)

## 제 3정규형
- 다른 속성에 의존(종속)하는 속성은 따로 분리할 것  
![image](https://user-images.githubusercontent.com/108309396/230309386-feffd92f-c1f9-4116-b936-0acef9a8b4c9.png)  
![image](https://user-images.githubusercontent.com/108309396/230309445-e7bc2b1a-c9f5-478a-bca0-7d7c1b18078d.png)



# JOIN
- 두 개 이상의 테이블에서 데이터를 가져와 결합하는 것
- 결국 우리가 조회하려면 모아서 테이블 1개로 만들어야 함
- &rarr; 테이블을 연결하는 것이 필요

## CROSS JOIN
- 모든 조합 출력  
![image](https://user-images.githubusercontent.com/108309396/230311678-fff7dd69-b00b-4cb7-930e-e5742d091f0f.png)

## INNER JOIN
- 두 테이블에서 일치하는 데이터만 결과 출력  
![image](https://user-images.githubusercontent.com/108309396/230311881-e8968d4e-8d03-4f81-8b8d-3cfc40cc3831.png)  
- 아래 방식을 더 권장

## LEFT (OUTER) JOIN
- 왼쪽 테이블의 데이터를 기준으로 오른쪽 데이터 결합, 없으면 NULL  
![image](https://user-images.githubusercontent.com/108309396/230312100-019bb769-55aa-4ca1-a933-3bf8dd3573da.png)

## RIGHT (OUTER) JOIN
- LEFT 반대  
![image](https://user-images.githubusercontent.com/108309396/230312239-b8e56ec3-ca12-4735-be03-d3b61cd93ead.png)

## FULL OUTER JOIN
- FULL OUTER JOIN한 것 중에서 둘 다 모두 있는 데이터를 제외한, 각각에만 존재하는 데이터를 추출한 것  
![image](https://user-images.githubusercontent.com/108309396/230312447-6113cb3b-3552-417e-81f2-feb5c3df4faa.png)