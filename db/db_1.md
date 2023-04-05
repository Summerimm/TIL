# Database
## 데이터(Data)
- 저장이나 처리에 효율적인 형태로 변환된 정보(information)
- 전세계 데이터센터 전력 소비량 250TWh로 남아공의 국가 소비전력 추월
- 미국 댈러스시에서 사용하는 물의 30% 냉각수에 사용(구글 댈러스 데이터 센터)

## 데이터베이스(Database)
- organized collection of data

## DBMS(Database Management System)
- 데이터를 수집하고 분석할 수 있게 고안된 프로그램
- SQLite, MySQL, mongoDB, ...

## 데이터베이스의 종류
### 관계형 데이터베이스(Relational Database)
- 수학 > 집합/논리 > 관계
- 표 형식으로 된 데이터 베이스

### 비관계형 데이터베이스(NoSQL Database)
- 관계형 데이터베이스의 한계를 극복하기 위한 조금 더 유연한 데이터베이스
- 실제로 많이 쓰이는 데이터베이스로 서브 데이터베이스로 두고 빠른 처리, 확장이 필요한 기능에서 사용하는 경우가 많음
- 일반적으로 메인 데이터베이스는 전통적으로 관계형 데이터베이스를 사용

# 관계형 데이터베이스(RDB)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 구조화해서 저장하므로 보다 체계적으로 데이터를 저장하고 관리할 수 있음
- 자료를 여러 테이블로 나누어서 관리, 테이블 간 관계를 설정해 여러 데이터를 조작 가능
- 데이터의 무결성(정확성, 일관성) 유지에 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작

## 관계형 데이터베이스의 구조
1. 스키마
2. 테이블
   - 필드, 레코드, 기본 키

### 스키마(Schema)
- 테이블의 구조
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것

### 테이블(Table)
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(relation)이라고도 부름
- 필드: 속성, 컬럼 &rarr; 각 필드에는 고유한 데이터 형식(타입)이 지정됨
- 레코드: 튜플, 행 &rarr; 테이블의 데이터는 레코드에 저장됨
- PK(Primary Key)
  - **기본 키**
  - 각 레코드의 고유한 값: 각각의 레코드를 구분할 수 있는 고윳값
  - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
  - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용
- FK(Foreign Key)
  - **외래 키**
  - 한 테이블의 속성(컬럼) 중 다른 테이블의 레코드를 식별할 수 있는 키
  - 다른 테이블의 기본 키를 참조
  - 참조하는 테이블의 속성 1개의 값은, 참조되는 측 테이블의 레코드 값에 대응됨
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음

# SQL
- Structured Query Language
- 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어
-  == 데이터베이스 관리 + CRUD 하는 언어

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
- Statement(문)
  - 독립적으로 실행할 수 있는 완전한 코드 조각
  - statement는 clause로 구성됨
- Clause(절)
  - statement의 하위 단위

## SQLite Data Types
1. NULL
   - missing information or unknown
2. INTEGER
   - 정수, 크기에 따라 가변 크기를 가짐
3. REAL
   - 실수, 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
   - 문자 데이터
5. BLOB(Binary Large Object)
   - 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
   - 바이너리 등 멀티미디어 파일(ex. 이미지 데이터)
- [참고] Boolean Type
  - SQLite에는 별도의 Boolean 타입이 없음
  - 대신 Boolean 값은 정수 0과 1로 저장됨
- [참고] Date & Time Datatype
  - SQLite에는 날짜 및 시간을 저장하기 위한 타입이 없음
  - 대신 SQLite의 built-in "Date And Time Functions"으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
- [참고] Binary Data
  - 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일
  - 기본적으로 컴퓨터의 모든 데이터는 binary data
    - 다만 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것


### Type Affinity(타입 선호도)
- 특정 컬럼에 저장된 데이터에 권장되는 타입
- 데이터 타입 작성 시 SQLite의 5가지 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC  
![image](https://user-images.githubusercontent.com/108309396/229963696-f7cd0330-fabc-4c76-98f4-8eb3721201e5.png)
- 타입 선호도 존재 이유
  - 다른 데이터베이스 엔진 간의 **호환성**을 최대화
  - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

## Constraints(제약조건)
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약

### 데이터 무결성
- 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
  - 무결성이란 데이터의 정확성, 일관성을 나타앰

### Constraints 종류
1. NOT NULL
   - 컬럼이 NULL 값을 허용하지 않도록 지정
   - 기본적으로 테이블의 모든 컬럼은 NULL 값을 허용함
2. UNIQUE
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함 
3. PRIMARY KEY
   - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
   - 각 테이블에는 하나의 기본 키만 있음
   - 암묵적으로 NOT NULL 제약 조건이 포함됨
   - 주의) INTEGER 타입에만 사용가능
4. AUTOINCREMENT
   - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
   - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
   - Django의 id컬럼에 사용하는 기본 제약조건
5. 기타