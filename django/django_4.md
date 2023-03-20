# Admin Site
- automatic admin interface &rarr; **관리자 페이지**
- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- 모델 class를 admin.py에 등록하고 관리
- 레코드 생성 여부 확인에 매우 유용하며 직접 레코드 삽입도 가능

1. admin 계정 생성 - `python manage.py createsuperuser`
2. admin site 로그인 
   - 계정만 만든 경우 관리자 화면에서 모델 클래스는 보이지 않음
3. admin에 모델 클래스 등록
   - 모델의 record를 보기 위해서는 admin.py에 등록 필요
   - ![image](https://user-images.githubusercontent.com/108309396/226227870-13242d3d-1e4e-4a8f-92bf-2686fb1c45bb.png)

# CRUD with view functions
- QuerySet API를 통해 view 함수에서 직접 CRUD 구현

## READ1 (index page)
- 전체 게시글 조회
  - index 페이지에서는 전체 게시글을 조회해서 출력  
  - ![image](https://user-images.githubusercontent.com/108309396/226279343-cc59eb54-7f68-44c4-a0a5-a330734592f7.png)

## READ2 (detail page)
- 개별 게시글 상세 페이지 제작
- 모든 게시글마다 view function과 template 파일을 만들 수는 없음
  - 글의 번호(pk)를 활용해서 하나의 뷰 함수와 템플릿 파일로 대응
  - Variable Routing
- `articles/urls.py`
  - url로 특정 게시글을 조회할 수 있는 번호를 받음
  - ![image](https://user-images.githubusercontent.com/108309396/226279795-33a86f70-4242-451a-ab75-4419c85a30f8.png)
- `articles/views.py`
  - `Article.objects.get(pk=pk)`에서 오른쪽 `pk`는 variable routing을 통해 받은 pk, 왼쪽 pk는 DB에 저장된 레코드의 id column
  - ![image](https://user-images.githubusercontent.com/108309396/226280031-5bcd16f2-08f2-42fc-b269-f5712b61fc13.png)
- `templates/articles/detail.html`
  - ![image](https://user-images.githubusercontent.com/108309396/226280226-d60e8011-6f00-4429-9f16-4c67a8e97e02.png)
- `templates/articles/index.html`
  - 제목을 누르면 상세 페이지로 이동
  - ![image](https://user-images.githubusercontent.com/108309396/226280844-1aaafcdb-1bdb-4ea7-80af-24ee48b478e1.png)


## CREATE
- CREATE logic 구현을 위해서는 2개의 view 함수 필요
- **"new"** view function: 사용자의 입력을 받을 페이지를 렌더링 하는 함수
- **"create"** view function: 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수

### 1. `new`   
![image](https://user-images.githubusercontent.com/108309396/226282236-cdaaeb7e-4219-40db-bccd-6ed0fd786eeb.png)

### 2. `index.html`
- new 페이지로 이동할 수 있는 하이퍼 링크 작성    
![image](https://user-images.githubusercontent.com/108309396/226282499-9676693c-8ac4-4922-8f41-aa0ad27d56e1.png)

### 3. `create`
- ![image](https://user-images.githubusercontent.com/108309396/226282677-9e33219f-d00f-4eb7-99d3-c63b65f1bfa5.png)
- ![image](https://user-images.githubusercontent.com/108309396/226282833-3763c08d-1386-48b3-96a1-086e507fbb23.png)
- 1 또는 2번째 생성 방식을 사용하는 이유
  - create 메서드가 더 간단해 보이지만 추후 데이터가 저장되기 전에 **유효성 검사 과정**을 거치게 될 예정
  - 유효성 검사가 진행된 후에 save 메서드가 호출되는 구조를 택하기 위함

> ### Django shortcut function - "redirect()"
> - 인자에 작성된 곳으로 다시 요청을 보냄
> - 사용 가능한 인자
>   - view name(URL pattern name): `return redirect('articles:index')`
>   - absolute or relative URL: `return redirect('/articles/')`

### 4. `new.html` 마무리
![image](https://user-images.githubusercontent.com/108309396/226284802-7c7c448d-2320-492b-8d57-3d99b0da14b1.png)

## HTTP Method
- `GET`: 어떠한 데이터(리소스)를 조회하는 요청, Query String 형식으로 전달
  - 특정 리소스를 가져오도록 요청할 때 사용
  - 반드시 데이터를 가져올 때만 사용해야 함
  - DB에 변화X
  - CRUD에서 `R` 담당
- `POST`: 어떠한 데이터(리소스)를 생성(변경)하는 요청, Query String이 아닌 Body에 담겨서 보내짐
  - 서버로 데이터를 전송할 때 사용
  - 서버에 변경사항을 만듦
  - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
  - GET과 다르게 URL로 데이터 전송X
  - CRUD에서 `C/U/D` 담당

### `new.html`에 POST method 적용
![image](https://user-images.githubusercontent.com/108309396/226286082-70aea81f-12e0-4eee-a6c7-fe2fb5b06aab.png)  
![image](https://user-images.githubusercontent.com/108309396/226286169-3d2a4944-c94c-45ac-8c13-03254c0e84d0.png)  

&rarr; 403 Forbidden 발생
- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
- 서버가 접근을 거부할 때 반환되는 상태코드(HTTP Status Code)
- 모델(DB)를 조작하는 것은 단순 조회와 달리 신원확인이 필요하기 때문

### CSRF
- Cross-Site-Request-Forgery
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- "Security Token 사용 방식(CSRF Token)"
  - 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
  - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
  - 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE method 등에 적용
  - Django는 DTL에서 csrf_token 템플릿 태그 제공
- `{% csrf_token %}`: 해당 태그가 없으면 Django 서버는 요청에 대해 403 forbidden으로 응답
  - 내부 URL로 향하는 POST form을 사용하는 경우에 사용  
![image](https://user-images.githubusercontent.com/108309396/226287103-56fd22bf-e1a3-463c-8399-ddecd055d6b3.png)


## DELETE
### 1. `urls`
- 삭제하고자 하는 특정 글을 조회 후 삭제해야 함  
![image](https://user-images.githubusercontent.com/108309396/226287262-cd4b2a6a-d859-4463-91c8-10eaea97d2a9.png)

### 2. `views`
![image](https://user-images.githubusercontent.com/108309396/226287367-39850658-17a5-42a4-9f80-3678449db37d.png)

### 3. templates(`detail.html`)
- DB에 영향을 미치기 때문에 POST method를 사용  
![image](https://user-images.githubusercontent.com/108309396/226287567-62519b0d-0262-4b5f-b8fe-ef32bcf4278d.png)

## UPDATE
- CREATE와 마찬가지로 2개의 view 함수 필요
- **"edit"** view function: 사용자의 입력을 받을 페이지를 렌더링하는 함수
- **"update"** view function: 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수  

## edit function
### 1. urls & views
- 기존에 입력되어 있던 데이터 조회
![image](https://user-images.githubusercontent.com/108309396/226289135-a82b95f2-fbd0-43d5-b969-1a35f95651b6.png)

### 2. templates(`edit.html`)
- 기존 데이터 출력
- `textarea` 태그는 value 속성이 없으므로 태그 내부 값으로 작성해야 함
![image](https://user-images.githubusercontent.com/108309396/226289390-b8952d0c-e3f1-4bb0-a25a-7999d6c76e6d.png)

### 3. templates(`detail.html`)
- Edit 페이지로 이동하기 위한 하이퍼 링크 작성
![image](https://user-images.githubusercontent.com/108309396/226290000-ee75f002-19fe-44f2-8cdb-a6480ed653d8.png)

## update function
### 1. urls & views & edit  
![image](https://user-images.githubusercontent.com/108309396/226290536-7b3bc265-dfec-4323-ab05-0114923f9076.png)


# Handling HTTP requests 
- HTTP requests 처리에 따른 view 함수 구조 변화
- new-create, edit-update의 view 함수 역할의 공통점과 차이점
  - 공통점
    - new-create는 모두 CREATE 로직 구현이 목적
    - edit-update는 모두 UPDATE 로직 구현이 목적
  - 차이점
    - new와 edit은 GET 요청에 대한 처리만을,
    - create와 update은 POST 요청에 대한 처리만을 진행  
  - &rarr; 하나의 view 함수에서 method에 따라 로직이 분리되도록 변경

## CREATE
- new와 create view 함수를 합침
- 각각의 역할은 `request.method` 값을 기준으로 나눔    
![image](https://user-images.githubusercontent.com/108309396/226291200-4bea2a35-88eb-4ef6-9a3c-e1d5d04ac287.png)
- 불필요해진 new의 view 함수와 url path를 삭제  
![image](https://user-images.githubusercontent.com/108309396/226291344-07124daf-b7d1-43bd-b563-d0639405ea11.png)