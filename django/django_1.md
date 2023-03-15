# Django
> 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것 = Framework

## 클라이언트-서버 구조
- 클라이언트와 서버 역시 하나의 컴퓨터
![image](https://user-images.githubusercontent.com/108309396/224866882-07ae4ee6-74e6-469e-a7a9-571bf19c5cc4.png)
- 어떠한 resource를 달라고 request하는 쪽을 클라이언트, resource를 제공해주는 쪽을 server라고 함
- 클라이언트
  - 웹 사용자의 인터넷에 연결된 장치(wifi에 연결된 컴퓨터 또는 모바일)
  - Chrome 또는 Firefox와 같은 웹 브라우저
  - 서비스를 요청하는 주체
- 서버
  - 웹 페이지, 사이트, 또는 앱을 저장하는 컴퓨터
  - 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
  - 요청에 대해 서비스를 응답하는 주체

+ 웹 브라우저는 요청을 보내는 역할, html을 해석하는(렌더링) 역할도 함

## 서버 실행 순서
1. 바탕화면에 'django-pjt' 폴더 생성
2. 가상환경 설정(`python -m venv venv`)
3. 가상환경 활성화(`source venv/Scripts/activate`)
4. django 설치(`pip install django==3.2.18`)
5. 프로젝트 생성 `django-admin startproject firstpjt`
6. 서버 실행 `python manage.py runserver`
7. 서버 종료 `Ctrl+c`

## 가상환경 사용
- 가상환경은 프로젝트별 패키지를 독립적으로 관리하기 위한 것
- 가상환경 패키지 목록 저장(`pip freeze > requirements.txt`)
- 파일로부터 패키지 설치(`pip install -r requirements.txt`)

## 프로젝트와 앱
- Prject
  - collections of apps
  - 프로젝트는 앱의 집합
  - 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음
- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등 역할을 담당
  - 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장

### Django Project Structure
![image](https://user-images.githubusercontent.com/108309396/224872728-85848e4b-a8d2-4c2e-84ac-f725cfb3a9ba.png)  
- `__init__.py`
  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - 별도로 추가 코드 작성X
- `asgi.py`
  - Asynchronous Server Gateway Interface
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용
- `settings.py`
  - Django 프로젝트 설정 관리
- `urls.py`
  - 사이트의 url과 적절한 views의 연결 지정
- `wsgi.py`
  - Web Server Gateway Interface
  - Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시 사용
- `manage.py`
  - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
  - `python manage.py <command> [options]`

### Django Application
- 애플리케이션(앱) 생성
- `python manage.py startapp articles`
- 일반적으로 애플리케이션 이름은 '복수형'으로 작성하는 것을 권장
- App == 하나의 큰 기능 단위
- 정해진 규칙X, 개발자가 판단해서 앱 생성
- 단일 앱으로 개발해도 괜찮음

### Django Application Structure
![image](https://user-images.githubusercontent.com/108309396/224872865-7865e48e-ccea-42bf-8faf-4b52a4123d8e.png)  
- `admin.py`
  - 관리자용 페이지를 설정하는 곳
- `app.py`
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드 작성X
- `models.py`
  - 애플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴의 M에 해당
- `texts.py`
  - 프로젝트의 테스트 코드를 작성하는 곳
- `views.py`
  - view 함수들이 정의되는 곳
  - MTV 패턴의 V에 해당
- 애플리케이션 등록
  - **앱을 사용하기 위해서는 settings.py에 반드시 INSTALLED_LAPPS 리스트에 반드시 추가해야함**  
![image](https://user-images.githubusercontent.com/108309396/224872630-1e538796-d5c6-45d3-805b-7d1a27a4584b.png)


## 요청과 응답
- Django의 세 가지 구조: Model(Data), View(Logic), Template(HTML과 같이 보여지는 것)
- URL &rarr; VIEW &rarr; TEMPLATE
- URLs  
![image](https://user-images.githubusercontent.com/108309396/224885250-0a11c5ec-6dcc-40d5-927f-e5c58fa45077.png)
- View: 요청이 들어오면 HTML Page로 응답을 돌려줌
![image](https://user-images.githubusercontent.com/108309396/224885371-f7f4a729-6dfc-4a6f-a91d-fd44ce9c784e.png)
- Templates  
![image](https://user-images.githubusercontent.com/108309396/224885629-986ccae0-b1f7-4058-8e84-7535a8bab08d.png)  
  - 실제 내용을 보여주는데 사용되는 파일
  - 파일의 구조나 레이아웃을 정의
  - Template 파일의 기본 경로
    - app 폴더 안의 templates 폴더
    - `app_name/templates/app_name`
  - 템플릿 폴더 이름은 반드시 `templates`라고 지정해야함
- `render()`
  - `render(request, template_name, context)`
  - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
   1. `request`: 응답을 생성하는데 사용되는 요청 객체
   2. `template_name`: 템플릿의 전체 이름 또는 템플릿 이름의 경로
   3. `context`: 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)  
![image](https://user-images.githubusercontent.com/108309396/224900123-ef067928-3778-4dcb-b974-258a6ba0c156.png)


### 데이터의 흐름 순서
- Django에서의 코드 작성은 `URL - View - Template`순으로 작성
![image](https://user-images.githubusercontent.com/108309396/224894906-4c813178-4ab3-4ed0-9a14-66e03c73d7c4.png)  