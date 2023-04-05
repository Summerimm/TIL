# Database
## 데이터(Data)
- **저장**이나 **처리**에 효율적인 형태로 변환된 정보(information)
- 전세계 데이터센터 전력 소비량 250TWh로 남아공의 국가 소비전력 추월
- 미국 댈러스시에서 사용하는 물의 30% 냉각수에 사용(구글 댈러스 데이터 센터)

## 데이터베이스(Database)
- organized collection of data

## DBMS(Database Management System)
- 데이터를 수집하고 분석할 수 있게 고안된 프로그램
- SQLite, MySQL, mongoDB, ...

## 데이터베이스의 종류(SQL vs NoSQL)
### 1) 관계형 데이터베이스(Relational Database)
- 수학 > 집합/논리 > 관계
- 표 형식으로 된 데이터 베이스  
![image](https://user-images.githubusercontent.com/108309396/230006659-56a435a3-79af-476c-ba51-ed934829b3c1.png)


### 2) 비관계형 데이터베이스(NoSQL Database)
- 관계형 데이터베이스의 한계를 극복하기 위한 조금 더 유연한 데이터베이스
- 서브 데이터베이스로 두고 빠른 처리, 확장이 필요한 기능에서 사용하는 경우가 많음
- 일반적으로 메인 데이터베이스는 전통적으로 관계형 데이터베이스를 사용  
![image](https://user-images.githubusercontent.com/108309396/230006905-c311ecf8-a92e-4487-89f1-7c7125da345c.png)

# 관계형 데이터베이스(RDB)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 구조화해서 저장하므로 보다 체계적으로 데이터를 저장하고 관리할 수 있음
- 자료를 여러 테이블로 나누어서 관리하고, 테이블 간 관계를 설정해 여러 데이터를 조작 가능
- 데이터의 무결성(정확성, 일관성) 유지에 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작

## 관계형 데이터베이스의 구조
1. 스키마
2. 테이블
   - 필드, 레코드, 기본 키

### 스키마(Schema)
- 테이블의 구조
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 **명세**를 기술한 것  
![image](https://user-images.githubusercontent.com/108309396/230007256-2009162d-0602-4b5d-8013-6e73c4fd4953.png)

### 테이블(Table)
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(relation)이라고도 부름
1. 필드: 속성, 컬럼 &rarr; 각 필드에는 **고유한 데이터 형식(타입)**이 지정됨
2. 레코드: 튜플, 행 &rarr; 테이블의 데이터는 **레코드에 저장**됨  
![image](https://user-images.githubusercontent.com/108309396/230007491-6c976ce1-368c-45ad-9a8b-8368a00c0d72.png)
3. PK(Primary Key)
   - **기본 키**
   - 각 레코드의 고유한 값: **각각의 레코드를 구분할 수 있는 고윳값**
   - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
   - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용
![image](https://user-images.githubusercontent.com/108309396/230007751-4946cf5f-b60d-402c-ba7d-0d176b1ca7bf.png)
4. FK(Foreign Key)
   - **외래 키**
   - 한 테이블의 속성(컬럼) 중 다른 테이블의 레코드를 식별할 수 있는 키
   - **다른 테이블의 기본 키를 참조**
   - 참조하는 테이블의 속성 1개의 값은, 참조되는 측 테이블의 레코드 값에 대응됨
   - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음


# SQL
- Structured Query Language
- 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어
-  == 데이터베이스 관리 + **CRUD** 하는 언어

## SQL Commands 종류
- DDL(Data Definition Language)
- DML(Data Manipulation Language)
- DCL(Data Control Language)  
![image](https://user-images.githubusercontent.com/108309396/229959233-573ce79d-ed5a-4c83-93f8-692bf70cb31a.png)

## SQL Syntax
![image](https://user-images.githubusercontent.com/108309396/229962690-532e34da-f752-43a7-b0ff-acd5abc034a0.png)  
- 모든 SQL문(statement)는 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작
- 하나의 statement는 `;`으로 끝남 &rarr; 각 SQL문을 구분하는 표준 방법
- SQL 키워드는 대소문자를 구분하지 않으나 **대문자로 작성**하는 것을 권장

### Statement & Clause
![image](https://user-images.githubusercontent.com/108309396/230011170-47371eec-d3d6-4bde-9709-8e96fbb5f9e6.png)  
- Statement(문)
  - 독립적으로 실행할 수 있는 완전한 코드 조각
  - statement는 clause로 구성됨
- Clause(절)
  - statement의 하위 단위
- SELECT statement라고 부르고 2개의 clause로 구성됨 &rarr; SELECT column_name, FROM table_name

# DDL
- SQL 데이터 정의 언어(DDL)을 사용하여 테이블 DB 개체를 만드는 방법을 학습
- CREATE, ALTER, DROP

### 사전준비
- 데이터베이스 `mydb.sqlite3` 파일 생성
- `DDL.sql` 파일 생성
- vscode 실행 후 DDL.sql 화면에서 마우스 우측 버튼 클릭 &rarr; `Use Database`
- 데이터 베이스 목록에서 `mydb.sqlite3` 선택

## `CREATE TABLE`
- 데이터베이스에 새 테이블을 만듦
- contacts 테이블 생성  
![image](https://user-images.githubusercontent.com/108309396/230012335-fcf54b08-599a-4a90-803a-215dc7aac88e.png)
- Query 실행하기
  - 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼 &rarr; 'Run Selected Query` 선택
- Query 실행 후 `mydb.sqlite`를 `Open Database`해서 테이블 및 스키마 확인

### SQLite Data Types
1. `NULL`
   - missing information or unknown
2. `INTEGER`
   - 정수, 크기에 따라 가변 크기를 가짐
3. `REAL`
   - 실수, 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. `TEXT`
   - 문자 데이터
5. `BLOB(Binary Large Object)`
   - 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
   - 바이너리 등 멀티미디어 파일(ex. 이미지 데이터)
- [참고] `Boolean Type`
  - SQLite에는 별도의 Boolean 타입이 없음
  - 대신 Boolean 값은 정수 0과 1로 저장됨
- [참고] `Date & Time Datatype`
  - SQLite에는 날짜 및 시간을 저장하기 위한 타입이 없음
  - 대신 SQLite의 built-in "Date And Time Functions"으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
- [참고] `Binary Data`
  - 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일
  - 기본적으로 컴퓨터의 모든 데이터는 binary data
    - 다만 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것


### Type Affinity(타입 선호도)
- 특정 컬럼에 저장된 데이터에 권장되는 타입
- 데이터 타입 작성 시 SQLite의 5가지 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
1. `INTEGER`
2. `TEXT`
3. `BLOB`
4. `REAL`
5. `NUMERIC`  
![image](https://user-images.githubusercontent.com/108309396/229963696-f7cd0330-fabc-4c76-98f4-8eb3721201e5.png)
- 타입 선호도 존재 이유
  - 다른 데이터베이스 엔진 간의 **호환성**을 최대화
  - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

## Constraints(제약조건)
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약

### 데이터 무결성
- 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 둠
  - 무결성 == 데이터의 정확성, 일관성

### Constraints 종류
1. `NOT NULL`
   - 컬럼이 NULL 값을 허용하지 않도록 지정
   - 기본적으로 테이블의 모든 컬럼은 NULL 값을 허용함
2. `UNIQUE`
   - 컬럼의 모든 값이 고유한 값이 되도록 함 
3. `PRIMARY KEY`
   - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
   - 각 테이블에는 하나의 기본 키만 있음
   - 암묵적으로 NOT NULL 제약 조건이 포함됨
   - 주의) INTEGER 타입에만 사용가능  
![image](https://user-images.githubusercontent.com/108309396/230025317-3630f831-088c-47b6-a3a9-aa71b456e3eb.png)
4. `AUTOINCREMENT`
   - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
   - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 재사용하지 못하도록 함  
    ![image](https://user-images.githubusercontent.com/108309396/230025654-b07760fb-e80c-453a-b013-4164ef3287c9.png)
   - Django의 id컬럼에 사용하는 기본 제약조건
5. 기타

## ALTER TABLE
- 기존 테이블의 구조를 수정(변경)  
![image](https://user-images.githubusercontent.com/108309396/230026008-bd38a090-7653-4726-97d9-4c07a12e4935.png)

### 1. `ALTER TABLE RENAME`
- 테이블명 변경  
![image](https://user-images.githubusercontent.com/108309396/230026128-53ed5cb7-4342-498b-8f54-e98ee3299a92.png)

### 2. `ALTER TABLE RENAME COLUMN`
- 컬럼명 변경  
![image](https://user-images.githubusercontent.com/108309396/230026320-2f1e48d6-df68-4e64-9af3-2394ea8067c3.png)

### 3. `ALTER TABLE ADD COLUMN`
- 새 컬럼 추가  
![image](https://user-images.githubusercontent.com/108309396/230026466-03d6bb56-d403-426b-9bde-903ab85415af.png)
- 만약 테이블에 기존 데이터가 있을 경우 `Cannot add NOT NULL column with default value NULL`이라는 에러 발생
- 이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성됨
- 그런데 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에 에러가 발생한 것
- DEFAULT 제약 조건을 사용하여 해결 가능  
- `DEFAULT`: column 제약조건 중 하나로, 데이터를 추가할 때 값을 생략할 시에 기본 값을 설정함  
![image](https://user-images.githubusercontent.com/108309396/230026917-99d9d036-e206-44df-b7f2-6c49c2e085d2.png)

### 4. `ALTER TABLE DROP COLUMN`
- 컬럼 삭제  
- SQLite3 3.55 이상부터 가능  
![image](https://user-images.githubusercontent.com/108309396/230027186-1c4a08fd-fe84-4160-add1-f5d37ee720d6.png)
- 삭제 불가능한 경우
  - 컬럼이 다른 부분에서 참조되는 경우: FK가 제약조건에서 사용되는 경우
  - PK인 경우
  - UNIQUE 제약 조건이 있는 경우

## DROP TABLE
- 데이터베이스에서 테이블을 제거
- 존재하지 않는 테이블을 제거하면 SQLite에서 에러 발생  
![image](https://user-images.githubusercontent.com/108309396/230027898-c00950a5-7d61-4a9a-acc7-e597967fed12.png)

### 특징
- 한 번에 하나의 테이블만 삭제 가능
- 여러 테이블을 삭제하려면 여러 DROP TABLE문을 실행해야 ㅎ마
- DROP TABLE문은 실행 취소하거나 복구 불가

### DDL 정리
- Data Definition Language
- `CREATE TABLE`: 데이터 타입과 제약조건
- `ALTER TABLE`
  - `RENAME`
  - `RENAME COLUMN`
  - `ADD COLUMN`
  - `DROP COLUMN`
- `DROP TABLE`

# SQL 실행 순서
1. FROM / JOIN (재료 들고오기)
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. DISTINCT
7. ORDER BY
8. LIMIT / LIMIT OFFSET


# DML
### 사전 준비
1. 시작하기
![image](https://user-images.githubusercontent.com/108309396/230029003-02e6cee9-f5d0-4567-9e42-ffb4bc637093.png)

2. 데이터베이스 파일 열기
- 시작과 동시에 데이터베이스를 열 수도 있음  
![image](https://user-images.githubusercontent.com/108309396/230029336-b8beff6f-b4d3-4782-889e-ee8b7e1fb53a.png)

3. sqlite3 종료하기
- `sqlite> .exit`

### CSV 파일을 SQLite 테이블로 가져오기
1. DML.sql 파일 생성 후 테이블 생성 완료
2. 데이터 베이스 파일 열기 `sqlite3 mydb.sqlite3`
3. 모드를 csv로 설정 `.mode csv`
4. .import 명령어를 사용하여 csv 데이터를 테이블로 가져오기 `.import users.csv users`

## Simple query
### SELECT statement
![image](https://user-images.githubusercontent.com/108309396/230030085-5bd99715-ef31-4a31-a70a-f57342848862.png)
- 특정 테이블에서 데이터를 조회하기 위해 사용
- 문법 규칙
  - SELECT절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
  - FROM절(clause)에서 데이터를 가져올 테이블을 지정
- 전체 데이터 조회는 `*`(asterisk)를 사용할 수 있음
- rowid 컬럼은 다음과 같이 조회 가능  
![image](https://user-images.githubusercontent.com/108309396/230030729-79a0a6a5-2b4e-468d-9e33-7da574e1eb61.png)

## Sorting rows
### ORDER BY clause
![image](https://user-images.githubusercontent.com/108309396/230030919-710366ec-5923-4a29-b0f8-ed4454d98fa8.png)  
- SELECT문에 추가하여 결과를 정렬
- 하나 이상의 컬럼을 기준으로 결과를 오름차순(`ASC`-기본값), 내림차순(`DESC`)로 정렬 가능
- 하나 이상의 컬럼을 정렬할 경우 첫 번째 열을 사용하여 정렬하고, 그 다음 두 번째 컬럼을 사용하여 정렬.  
![image](https://user-images.githubusercontent.com/108309396/230031266-18016595-7d89-4152-be98-0e54d1ef6b7f.png)

### [참고] Sorting NULLs
- 정렬과 관련하여 SQLite는 NULL을 다른 값보다 작은 것으로 간주

## Filtering data
- 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
- Clause
  - `SELECT DISTINCT`
  - `WHERE`
  - `LIMIT`
- Operator
  - `LIKE`
  - `IN`
  - `BETWEEN`

