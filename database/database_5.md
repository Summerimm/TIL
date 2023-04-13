# M:N (User-User)
- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현

## Profile 구현
1. url 및 view 함수 작성  
![image](https://user-images.githubusercontent.com/108309396/231400207-eb8eb55e-b6ac-4246-aed3-ddee485ecb91.png)
2. profile 템플릿 작성  
![image](https://user-images.githubusercontent.com/108309396/231400314-3b481574-7ce3-4f77-908e-c1f346ebeb96.png)
3. profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성  
![image](https://user-images.githubusercontent.com/108309396/231400464-255438a8-5775-414c-8ee4-64b8c44c64a1.png)

## Follow 구현
- 모델 관계 설정: ManyToManyField 작성 및 Migration 작성  
![image](https://user-images.githubusercontent.com/108309396/231400972-3c00f363-a1c9-461c-874a-a18ac4a297aa.png)
- url 및 view 함수 작성  
![image](https://user-images.githubusercontent.com/108309396/231401116-e80a6d26-a9c1-4571-b130-5ce86015f059.png)
- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성  
![image](https://user-images.githubusercontent.com/108309396/231401275-34e647da-b3e2-437a-a5ed-14e898474f44.png)
- 데코레이터 및 is_authenticated 추가   
![image](https://user-images.githubusercontent.com/108309396/231401481-83d4a61c-fdf0-4577-90c0-228361752451.png)


# Fixtures
- Fixtures를 사용해 모델에 초기 데이터 제공하는 방법
- Django 프로젝트의 앱을 처음 설정할 떄 동일하게 준비된 데이터로 데이터베이스를 미리 채우는 것이 필요한 상황이 있음
- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음

## fixtures 생성 및 로드
- 생성(데이터 추출): `dumpdata`
  - 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력함
  - 여러 모델을 하나의 json 파일로 만들 수 있음  
  ![image](https://user-images.githubusercontent.com/108309396/231402424-60f2382c-f6a9-48b5-b2c1-36ed50bb2012.png)
  - `dumpdata`의 출력 결과물은 `loaddata`의 입력으로 사용됨
  - `--indent 4` &rarr; Prettify
  - [참고] 모든 모델을 한 번에 dump하기  
  ![image](https://user-images.githubusercontent.com/108309396/231404263-fec1e4b5-afdf-4a3d-af02-ff5a640d5c15.png)
- 로드(데이터 입력): `loaddata`
  - fixtures의 내용을 검색하여 데이터베이스로 로드  
  ![image](https://user-images.githubusercontent.com/108309396/231611661-718303f9-8ffe-4f6b-93db-2a337331a8eb.png)
  - `app_name/fixtures/`
  - Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾음
  - fixtures의 내용을 검색하여 데이터베이스로 로드  
  ![image](https://user-images.githubusercontent.com/108309396/231618137-a3a5ede1-37b3-47ef-8a25-76491e4a2cdd.png)
  - db.sqlite3 파일 삭제 후 migrate 작업 진행
  - fixtures load하기  
  ![image](https://user-images.githubusercontent.com/108309396/231618239-9bb83bd3-e83f-4938-a2bb-b0b00e1d9760.png)

### [참고] loaddata를 하는 순서
- 한 번에 loaddata를 하지 않고 하나씩 실행할 경우 모델 관계에 따라 순서가 중요
  - comment는 article에 대한 key, user에 대한 key가 필요 &rarr; user-article-comment 순이 되어야 함  
  ![image](https://user-images.githubusercontent.com/108309396/231618466-7fd8ab23-ce82-4830-911f-82f437e58559.png)

### [참고] loaddata 시 encoding codec 관련 에러 발생하는 경우
1. `dumpdata` 시 추가옵션 작성  
![image](https://user-images.githubusercontent.com/108309396/231618553-034a17d3-3204-4d28-87db-ff666df1f7bd.png)
2. 메모장 활용
   - 메모장으로 json 파일 열고 다른 이름으로 저장 클릭 후 인코딩을 UTF-8로 선택


# Improve Query
###  모든 Pet의 집사 이름을 출력하고 싶을 경우
1. ORM  
![image](https://user-images.githubusercontent.com/108309396/231618783-079b458d-7edb-4e31-b15f-97879e441444.png)
2. SQL  
![image](https://user-images.githubusercontent.com/108309396/231618842-86d10f1b-428b-4d28-b313-946c012b613c.png)

### ORM이 DB를 조회한 횟수
![image](https://user-images.githubusercontent.com/108309396/231619032-05ec2f31-54d4-4e3a-983f-8dc67904b9c5.png)
- Django shell 이용해서 함수 실행 시 반복해서 Petsitter DB에 접근하는 것을 알 수 있음 &rarr; **N+1 problem**  
![image](https://user-images.githubusercontent.com/108309396/231619153-9e84b2c2-41d9-436c-b05e-a82cdfb0fc58.png) 

## Django ORM 특징
1. 기본적으로 **Lazy Loading**(지연 로딩) 전략 사용
2. 똑같은 데이터 사용 시 **캐싱**을 내부적으로 해둠

## Lazy Loading
- ORM 함수를 호출할 때 DB에 query를 날리는 것이 아니라 미루다가 실제로 데이터를 사용 시 query를 날림
- 객체와 RDB를 연결하는 ORM 입장에서는 모든 경우에 호출하는 것은 매우 비용&uarr;
- 따라서 성능개선을 위해 해당 데이터가 필요한 시점에 DB 호출  
![image](https://user-images.githubusercontent.com/108309396/231619491-4f8c79a5-f1f7-405e-b75b-1b00b75a2d54.png)
- 해결방법: **Eager Loading**(즉시 로딩)
  - 보통 여러 테이블의 데이터를 한번에 가져올 때 사용 
  - `selected_related`(정참조)와 `prefetch_related`(역참조) 사용  
  ![image](https://user-images.githubusercontent.com/108309396/231619702-272de186-34d6-44a8-afe6-63c386ca20f4.png)

### `selected_related`(정참조)
- 1:1 또는 N:1 참조 관계에서 사용
- SQL에서 INNER JOIN절을 활용해 참조하는 테이블의 일부를 가져오고 SELECT FROM을 통해 관련된 필드를 가져옴

### `prefetch_related`(역참조)
- M:N 또는 N:1 역참조 관계에서 사용
- SQL이 아닌 Python을 통한 JOIN 진행

## Caching
- 특정 데이터를 불러온 후 재사용할 경우 캐싱 사용
- 불러온 데이터에 변화를 일으키는 쿼리가 아니라면 저장해둔 데이터 사용  
![image](https://user-images.githubusercontent.com/108309396/231620302-0108ae30-ded6-49a5-b3f2-0f97bff325e5.png)