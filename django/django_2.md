# Design Pattern
- 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 **공통적인 설계 문제**가 존재
- 이를 처리하는 해결책 사이에도 공통점이 있다는 것을 발견 &rarr; 이러한 유사점을 **패턴**이라고 함
- 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
- 자주 사용되는 소프트웨어의 구조를 일반적인 구조화를 해둔 것 &rarr; 디자인 패턴
- 커뮤니케이션의 효율성 &uarr;

## Django MTV Design Pattern
- `MTV Pattern` &rarr; MVC 디자인 패턴을 기반으로 조금 변형된 패턴이다.
- MVC 디자인 패턴
  - Model-View-Controller의 준말
  - 데이터 및 논리 제어를 구현하는 데 널리 사용됨
  - `Model`: 데이터와 관련된 로직 관리
  - `View`: 레이아웃과 화면을 처리
  - `Controller`: 명령을 model과 view부분으로 연결
  - 각 부분을 독립적으로 개발 가능 &rarr; 개발 효율성 및 유지보수 쉬워짐, 다수의 멤버로 개발하기 용이
- MTV 디자인 패턴
  - `Model`: 데이터 관련 로직 관리(응용 프로그램의 데이터 구조 정의 및 데이터베이스의 기록 관리)
  - `Template`: 레이아웃과 화면 처리 &rarr; **MVC에서의 View에 해당**
  - `View`: Model & Template 중간 처리 및 응답 반환(클라이언트의 요청에 대해 처리를 분기하는 역할) &rarr; **MVC에서의 Controller에 해당**  
![image](https://user-images.githubusercontent.com/108309396/225492462-c5990270-6598-4bff-a42e-124a1c40b511.png)  
![image](https://user-images.githubusercontent.com/108309396/225243875-ba86e172-bb44-4530-b4b3-6c932d585eea.png)

# Django Template
- Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입
- Django Template System: 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당

## Django Template Language(DTL)
- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능 제공
  - Python처럼 일부 구조를 사용할 수 있지만 **Python 코드로 실행되는 것X**
  - Python이 HTML에 포함된 것X
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심

## DTL Syntax
### 1. Variable: 변수
- `{{ variable }}`
- 변수명은 영어, 숫자와 언더바의 조합으로 구성 가능하나 언더바로 시작 불가
- 공백, 구두점 문자 사용 불가능
- dot(.)을 사용하여 변수 속성에 접근 가능
- render()의 세번째 인자로 `{'key': value}`와 같이 딕셔너리 형태로 넘겨주며, 
- 여기서 정의한 **key**에 해당하는 문자열이 **template에서 사용 가능한 변수명**이 됨
### 2. Filters: 표시할 변수를 수정할 때 사용
- `{{ variable|filter }}`
- ex) name 변수를 모두 소문자로 출력 &rarr; `{{ name|lower }}`
- chained가 가능하며, 일부 필터는 인자를 받기도 함 `{{ name|truncatewords:30 }}`
### 3. Tags: 기능 수행
- `{% tag %}`
- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 기능 수행
- 일부 태그는 시작과 종료 태그 필요 `{% if %}{% endif %}`
### 4. Comments: 주석
- `{# #}`
- 한 줄 주석만 사용가능(줄바꿈 불가)
- 여러 줄 주석은 `{% comment %}{% endcomment %}` 사이에 입력 &rarr; tag임

# Template Inheritance
- 코드의 재사용성을 위해
- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음
- `{% extends 'base.html' %}`
  - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
  - 반드시 템플릿 최상단에 작성 되어야 함(2개 이상 사용불가)
- `{% block content %}{% endblock content %}`
  - 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
  - 즉, 하위 템플릿이 채울 수 있는 공간을 의미
  - 가독성을 높이기 위해 선택적으로 endblock 태그에 이름 지정 가능(여기서는 content)  
![image](https://user-images.githubusercontent.com/108309396/225488319-7376c24e-3a21-4d59-9ba8-6037345253fb.png)  

## Django의 Template 처리 방식
![image](https://user-images.githubusercontent.com/108309396/226818955-18f4f4f1-2d23-4b8b-a378-07fe58c496d8.png)
- `'APP_DIRS': TRUE` &rarr; 앱 별로 templates 디렉토리를 확인
- `DIRS`에 `[BASE_DIR / 'templates']` 추가 시 모든 앱에서 사용 가능

# Django URLs
## Trailing URL Slahses
- Django는 URL 끝에 /가 없다면 자동으로 붙여주는 것이 기본 설정
  - 그래서 모든 주소가 '/'로 끝나게 되어있으나 모든 프레임워크가 이렇게 동작하진 않음
- `foo.com/bar` &rarr; 파일의 내용을 보여준다는 의미
- `foo.com/bar/` &rarr; 폴더를 뜻함
  - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 둘을 서로 다른 페이지로 봄

## Variable routing
- URL 주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지 연결 가능

### Variable routing 작성
![image](https://user-images.githubusercontent.com/108309396/226819530-f0706097-478e-4227-91fb-4e3c121a933c.png)
- 변수는 `<>`에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string으로 5가지 타입으로 명시 가능
  1. `str`
     - '/'를 제외하고 비어 있지 않은 모든 문자열
     - 작성하지 않을 경우 기본값
  2. `int`
     - 0 또는 양의 정수와 매치
  3. `slug`
  4. `uuid`
  5. `path`  

### View 함수 작성
- varialbe routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용 가능  
![image](https://user-images.githubusercontent.com/108309396/225489495-8ac1328f-e361-42ff-bb1f-cc41334b167d.png)  

## App URL mapping
![image](https://user-images.githubusercontent.com/108309396/225490722-895f1bad-104b-46e1-b3b2-1387e19c716a.png)  
- 앱이 많아졌을 떄 urls.py를 각 app에 매핑
- 각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁
![image](https://user-images.githubusercontent.com/108309396/225489840-3a62af7d-b66f-4d16-abc0-f6c93e22d6db.png)  
- Including other URLconfs
  - urlpattern은 언제든지 다른 URLconf 모듈을 include할 수 있음
  - **include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않으면 에러 발생, 빈 리스트라도 작성되어 있어야 함**  

## Naming URL patterns
![image](https://user-images.githubusercontent.com/108309396/225491447-7231007a-ab1d-40c9-8f5d-c656727ed0a4.png)  
- 링크에 URL을 직접 작성X, `path()` 함수의 `name` 인자를 정의해서 사용
- DTL의 Tag 중 **URL 태그**를 사용해서 `name`을 사용 가능
- 이를 통해 URL 설정에 정의된 특정 경로들의 의존성 제거 가능
- view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움
- `{% url '' %}`: 템플릿에서 사용
  - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소 반환

## URL namespace
- URL namespace 사용 시 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 가능
- app_name attribute를 작성해 URL namespace를 설정  
![image](https://user-images.githubusercontent.com/108309396/225491670-d22443b9-b930-457a-8532-8eb5545be63a.png)  
- URL 참조: `:` 연산자를 사용하여 지정    
![image](https://user-images.githubusercontent.com/108309396/225491763-a7b87260-17a1-4514-87fc-96bc462aaf10.png)  