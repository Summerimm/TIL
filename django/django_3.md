# Form & Data
- 클라이언트가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
- 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공 가능

## Sending form data(Client)
### HTML `<form>` element
- **사용자로부터 할당된 데이터를 서버로 전송**
- "데이터를 어디(action)로 어떤 방식(method)으로 보낼지"
- 핵심 속성: `action`, `method`
  1. `action`
  - 입력 데이터가 전송될 URL을 지정
  - 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐
  2. `method`
  - 데이터를 어떻게 보낼 것인지 정의
  - 입력 데이터의 HTTP request methods를 지정
  - HTML form 데이터는 `GET/POST` 2가지 방법으로만 전송 가능  

### HTML `<form>` element 작성
![image](https://user-images.githubusercontent.com/108309396/225520327-4b8d1659-d557-4e1d-a322-67e6572a8104.png)

### HTML \<input> element 작성
![image](https://user-images.githubusercontent.com/108309396/225524633-9c64edb2-a045-476c-a3ce-298dc6f466a3.png)  
- 사용자로부터 데이터를 입력 받기 위해 사용
- `type` 속성에 따라 동작 방식이 달라짐
  - 지정하지 않은 경우, 기본값은 `text`
- 핵심 속성: `name`
  - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송
  - 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근가능
  - 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것

### HTTP request methods
- HTTP
  - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
- HTTP Method 예시: GET, POST, PUT, DELETE

### GET
- 서버로부터 정보를 조회하는 데 사용
  - 즉, 서버에게 리소스를 요청할 때 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
  - 데이터는 URL에 포함되어 서버로 보내짐
- `Query String Parameters` &rarr; `Query String`이라고도 함
  - url 주소에 데이터를 파라미터를 통해 넘기는 것
  - 파라미터가 여러 개일 경우 `&`로 연결된 `key=value` 쌍으로 구성됨
  - 기본 URL과 물음표(?)로 구분됨: `http://host:port/path?key=value&key=value`

## Retrieving the data(Server)
- "데이터 가져오기(검색하기)"

### catch 작성  
![image](https://user-images.githubusercontent.com/108309396/225531940-a63834ed-b79f-4912-b316-901860ca43ae.png)

### action 작성  
![image](https://user-images.githubusercontent.com/108309396/225532180-f2eeef1a-38de-4aac-b8c9-cc70926c0d19.png)

### 데이터 가져오기
- catch 페이지의 url: `http://127.0.0.1:8000/catch/?message=데이터`
- "모든 요청 데이터는 view 함수의 첫 번째 인자 request에 들어있다."
- request 객체  
![image](https://user-images.githubusercontent.com/108309396/225533740-a97b061c-5ea5-42a7-93e6-403f88bdd0a9.png)

### catch 작성 마무리
![image](https://user-images.githubusercontent.com/108309396/225533957-b95308db-f6f1-4465-b382-04c6287993a0.png)  

### Request and Response objects
1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
2. 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫 번째 인자로 전달
3. 마지막으로 view 함수는 HttpResponse object를 반환


# Database
- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 **조직화된 데이터를 수집하는 저장 시스템**

## Database 기본 구조 
1. **스키마(Schema)**
  - Structure
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조  
![image](https://user-images.githubusercontent.com/108309396/225536143-ff5e684f-dc4c-46a0-9c52-354a543413fc.png)
2. **테이블(Table)**  
![image](https://user-images.githubusercontent.com/108309396/225536479-82fa1456-b4ff-424a-8b98-e26fcdc4bfc8.png)  
  - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  - relation이라고도 부름
    1. 필드(field)
       - 속성, 컬럼(attribute, column)
       - 각 필드에는 고유한데이터 형식이 지정됨(INT, TEXT 등)
    2. 레코드(record)
       - 튜플, 행(Row)
       - 테이블의 데이터는 레코드에 저장됨
    3. PK(Primary Key)  
      ![image](https://user-images.githubusercontent.com/108309396/225537084-84e15dd4-cfd2-4df3-942f-dd5d2f39b2ff.png)
       - 기본 키
       - 각 레코드의 고유한 값(식별자로 사용)
       - unique: 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값
       - 데이터베이스 관리 밈ㅊ 테이블 간 관계 설정 시 주요하게 활용됨
- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어


# Django Model
![image](https://user-images.githubusercontent.com/108309396/225537676-97554c79-c5b5-42e8-905d-b46a6cd1f2db.png)  
- Django는 Model을 통해 데이터에 접근하고 조작
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 일반적으로 각각의 모델은 하나의 DB 테이블에 mapping
  - 모델 클래스 1개 == DB 테이블 1개

### models.py
- 모델 클래스를 작성하는 것은 **DB table의 스키마를 정의하는 것**
- "모델 클래스 == 테이블 스키마"  
![image](https://user-images.githubusercontent.com/108309396/225542666-df6959a7-fb66-4278-9881-894c6277766a.png)  
- Model 이해하기  
![image](https://user-images.githubusercontent.com/108309396/225542798-b18799a4-968f-4bff-86fa-d575acf545fb.png)  
![image](https://user-images.githubusercontent.com/108309396/225542876-a3df3423-48b6-406c-a987-17c3f97279d4.png)  
![image](https://user-images.githubusercontent.com/108309396/225542933-2ab22131-ddba-485f-b2ae-ecc9a4e61706.png)  
![image](https://user-images.githubusercontent.com/108309396/225542967-6dfa3c69-d59a-4b73-ab95-46065ea23802.png)  

### Django Model Field
- Django는 model field를 통해 table의 field(column)에 저장할 데이터 유형(INT, TEXT)을 정의
- 데이터 유형에 따라 다양한 model field를 제공
  - DateField(), CharField(), IntergerField() 등  
![image](https://user-images.githubusercontent.com/108309396/225544892-631d3290-977e-4304-852c-b4c8ddd92bd0.png)  
![image](https://user-images.githubusercontent.com/108309396/225544947-6618c746-cb30-4ecd-acc0-f5fdf5105cc3.png)  

## Migrations
- Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법
- `makemigrations`, `migrate`

### makemigrations
- 모델의 변경사항에 대한 새로운 migration을 만들 때 사용
- `python manage.py makemigrations`
- "파이썬으로 작성된 설계도"  
![image](https://user-images.githubusercontent.com/108309396/225544593-84caea63-f736-41d7-98ad-659c71a0042a.png)

### migrate
- makemigrations로 만든 설계도를 실제 DB에 반영하는 과정(db.sqlite3 파일에 반영)
- 결과적으로 모델의 변경사항과 데이터베이스를 동기화
- `python manage.py migrate`  
![image](https://user-images.githubusercontent.com/108309396/225545653-173090c4-4f94-4fe9-a7c3-5cf7f896f00a.png)

### Migrations 기타 명령어
1. `showmigrations`
  - migrations 파일들이 migrate 됐는지 안 됐는지 여부를 확인하는 용도
  - \[X] 표시가 있으면 migrate가 완료되었음을 의미
  - `python manage.py showmigrations`
1. `sqlmigrate`
  - `python manage.py sqlmigrate articles 0001`
  - 해당 migrations 파일이 SQL문으로 어떻게 해석될 지 미리 확인할 수 있음

### 반드시 기억해야 할 migration 3단계
1. models.py에서 변경사항이 발생하면
2. migration 생성(`makemigration`)
3. DB 반영(모델과 DB의 동기화)(`migrate`)

## ORM(Object-Relational-Mapping)
![image](https://user-images.githubusercontent.com/108309396/225548001-16b5d249-43c3-41dc-9447-85f8c68f312f.png)
- makemigrations로 인해 만들어진 설계도는 파이썬으로 작성되어 있음
- but! DB는 SQL만 알아들을 수 있음 &rarr; 중간에 번역을 담당하는 것이 ORM
- ORM: 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django <-> DB) 데이터를 변환하는 프로그래밍 기술
- Django는 내장 Django ORM을 사용
- "SQL을 사용하지 않고 DB를 조작할 수 있게 만들어주는 매개체"

### ORM 장단점
- 장점
  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
  - 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM만으로 세밀한 DB 조작을 구현하기 어려운 경우가 있음

### ORM을 사용하는 이유
- **생산성**
- DB를 객체(object)로 조작하기 위해 ORM을 사용


# QuerySet API
### 사전준비
- SQLite 설치 후 실행(`db.sqlite3`-우클릭-`Open Database`)
- 좌측 하단 SQLITE EXPLORER 클릭-테이블 선택 후 show table 버튼 클릭 
- 추가 라이브러리 설치 및 설정
  - `pip install ipython`, `pip install django-extensions`
  - `settings.py` `INSTALLED_APPS`에 `'django_extensions',` 추가
  - 패키지 목록 업데이트(`pip freeze > requirements.txt`)
- ORM 구문 연습을 위해 파이썬 쉘 환경 사용(`python manage.py shell_plus`)

## Database API
- Django가 제공하는 ORM을 사용해 DB를 조작하는 방법
- Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API를 제공  
<img width="531" alt="image" src="https://user-images.githubusercontent.com/108309396/225655625-e4e236f8-f301-456d-aead-a6a0d561c29a.png">

### objects manager
- Django 모델이 DB 쿼리 작업을 가능하게 하는 인터페이스
- DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager

### Query
- 데이터베이스에 특정한 데이터를 보여달라는 요청
- "쿼리문을 작성한다" &rarr; 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 파이썬으로 작성한 코드는 ORM에 의해 SQL로 변환되어 DB에 전달, DB의 응답데이터를 ORM이 `QuerySet`이라는 자료 형태로 변환하여 우리에게 전달

### QuerySet
![image](https://user-images.githubusercontent.com/108309396/225657341-5d5f6fb7-af4c-4a4e-b019-132d671ce45f.png)  
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용 가능
- Django ORM을 통해 만들어진 자료형으로 필터를 걸거나 정렬 등을 수행 가능
- objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체
- **단, DB가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨**

## CRUD
- Create / Read / Update / Delete

## Create
1. 첫 번째 방법     
1\) `article = Article()`: 클래스를 통한 인스턴스 생성  
2\) `article.title = 'first'`: 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당  
3\) `article.save()`: 인스턴스로 save 메서드 호출  
<img width="454" alt="image" src="https://user-images.githubusercontent.com/108309396/225658901-59372126-6dd3-47d8-a660-1f86c0de7d4c.png">  
<img width="601" alt="image" src="https://user-images.githubusercontent.com/108309396/225659069-206fe4ed-26f6-4d66-ae1b-63a1ed797e3c.png">  
<img width="537" alt="image" src="https://user-images.githubusercontent.com/108309396/225661174-43f74a6d-52a5-4661-99c8-0bfb466ab61c.png">  

2. 두 번째 방법
- 인스턴스 생성 시 초기 값을 함께 작성하여 생성  
<img width="836" alt="image" src="https://user-images.githubusercontent.com/108309396/225659648-1f7ba07e-345a-4e99-97a4-f93af4eef1d8.png">  

3. 세 번째 방법
- QuerySet API 중 create() 메서드 활용  
<img width="512" alt="image" src="https://user-images.githubusercontent.com/108309396/225660037-3826cf25-3fa7-45ab-8aa6-1f6c276ce175.png">

> `.save()`
> - "Saving object"
> - 데이터 생성 시 save를 호출하기 전까진 객체의 id 값은 None
>   - id 값은 데이터베이스에서 계산되기 때문
> - 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 끼치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨 


## READ
- QuerySet API method를 사용해 데이터를 다양하게 조회
1. Methods that **return new querysets**
2. Methods that **do not return querysets**  
![image](https://user-images.githubusercontent.com/108309396/225841236-51e223af-4c21-4ae1-9626-0b83c0c7aa0f.png)


### all()
- QuerySet return
- 전체 데이터 조회

### get()
- 단일 데이터 조회
- 객체를 찾을 수 없으면 `DoesNotExist` 예외를 발생시킴
- 둘 이상의 객체를 찾으면 `MultipleObjectsReturned` 예외를 발생시킴
- &rarr; primary key와 같이 uniqueness(고유성)을 보장하는 조회에서 사용해야 함   
![image](https://user-images.githubusercontent.com/108309396/225841524-55e4a025-8a4a-4e74-8350-4ec056655c76.png)

### filter()
- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환  
![image](https://user-images.githubusercontent.com/108309396/225841896-a760652e-c973-4b82-9b5e-f9d85fb0143c.png)

### Field lookups
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 `filter(), exclude(), get()`에 대한 키워드 인자로 지정됨  
![image](https://user-images.githubusercontent.com/108309396/225842089-017300ef-a664-497a-876a-d9606abec66b.png)

## UPDATE
### Update 과정
1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
3. save() 인스턴스 메서드 호출  
![image](https://user-images.githubusercontent.com/108309396/225842387-6758a21f-9a79-485f-8847-bfc384cfd326.png)


## DELETE
### Delete 과정
1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. delete() 인스턴스 메서드 호출  
![image](https://user-images.githubusercontent.com/108309396/225842622-4bd9849e-7ef0-4d76-8086-a10a3a50ea7d.png)
