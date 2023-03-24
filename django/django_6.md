# 인증과 권한
- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)
- 필수 구성은 `setting.py`에 이미 포함됨. `INSTALLED_APPS`에서 확인 가능 &rarr; django.contrib.auth
- `Authentication`(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- `Authorization`(권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

### 사전 설정
- 두 번째 app accounts 생성 및 등록 &rarr; 되도록 accounts로 지정하는 것을 권장  
![image](https://user-images.githubusercontent.com/108309396/226805103-77112fe9-bbf6-41b4-9969-ab67fabf2c6f.png)
- url 분리 및 매핑  
![image](https://user-images.githubusercontent.com/108309396/226805191-3e1417e7-5756-423d-b90c-0e2e87ee7936.png)

# Custom User Model
- Custom User Model로 **대체하기**
- Django는 `AUTH_USER_MODEL` 설정 값으로 Default User Model을 override할 수 있도록 함

## AUTH_USER_MODEL
- 프로젝트에서 User를 나타낼 때 사용하는 모델
- 프로젝트가 진행되는 동안(모델을 만들고 마이그레이션한 이후) 변경할 수 없음
- 첫 번째 마이그레이션 전에 확정지어야 하는 값
- 기본값  
![image](https://user-images.githubusercontent.com/108309396/226805568-e9d90edb-c277-4b43-8a5e-8707290a4ab0.png)

## How to substituting a custom User model
- `AbstractUser`를 상속받는 커스텀 User 클래스 작성  
![image](https://user-images.githubusercontent.com/108309396/226805740-aacf3197-5072-46e1-a43f-c2c621ca9052.png)
- `AUTH_USER_MODEL = 'accounts.User'`  
![image](https://user-images.githubusercontent.com/108309396/226805858-f39b07e2-5ec9-4aaf-8ffb-3d83383dd4a8.png)
- `admin.py`에 커스텀 User 모델을 등록 &rarr; 등록하지 않으면 admin site에 출력X  
![image](https://user-images.githubusercontent.com/108309396/226805985-b690c590-e213-4f6b-9a85-38bf54f2ce44.png)

### [참고] User 모델 상속 관계  
![image](https://user-images.githubusercontent.com/108309396/226806062-ddda67e0-c0d7-4372-ae7a-4d2bd19cce4a.png)

### [참고] AbstractUser
- 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 Abstract base classes
- Abstract base classes(추상 기본 클래스)
  - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  - DB table을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨

### [주의] 데이터베이스 초기화
1. `migrations` 파일 삭제
   - `migrations` 폴더 및 `__init__.py`는 삭제하지 않음
   - **번호가 붙은 파일만 삭제!!!**
2. `db.sqlite3` 삭제
3. `migrations` 진행 (`makemigrations` &rarr; `migrate`)

# HTTP
- Hyper Text Transfer Protocol
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트-서버 프로토콜이라고도 부름

## 요청과 응답
- 요청(requests): 클라이언트(브라우저)에 의해 전송되는 메시지
- 응답(response): 서버에서 응답으로 전송되는 메시지

## HTTP 특징
1. 비연결 지향(connectionless)
   - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
2. 무상태(stateless)
   - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나고 상태 정보가 유지되지 않음
   - 클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적 

### 어떻게 로그인 상태를 유지할까?
- 우리가 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 **"상태"**가 유지됨
- 서버와 클라이언트 간 지속적인 상태 유지를 위해 **"쿠키와 세션"**이 존재

# 쿠키(Cookie): 데이터 전달 방식
- HTTP 쿠키는 **상태가 있는 세션**을 만들도록 해 줌
- 사용자가 웹 사이트를 방문할 경우 해당 웹 사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 "기록 정보 파일"
  - 클라이언트는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 쿠키를 저장해놓았다가, **동일한 서버에 재요청 시 저장된 쿠키를 함께 전송**
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태 유지 가능
  - stateless HTTP protocol에서 상태 정보를 기억시켜주기 때문
- &rarr; 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 같은 서버에 재요청할 때마다 요청과 함께 저장해두었던 쿠키도 함께 전송  
![image](https://user-images.githubusercontent.com/108309396/226807632-f8312433-5253-4e04-a830-472682663521.png)

## 쿠키 사용 목적
1. Session management: 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
   - 서버는 응답과 함께 Set-Cookie 응답 헤더를 브라우저에게 전송 &rarr; 이 헤더는 클라이언트에게 쿠키를 저장하라고 전달
   - 서버로 전송되는 모든 요청에 브라우저는 Cookie HTTP 헤더를 사용해 서버로 이전에 저장했던 모든 쿠키들을 함께 전송(ex. 장바구니 정보를 매 요청마다 보내는 것) 
2. Personalization: 사용자 선호, 테마 등의 설정
3. Tracking: 사용자 행동을 기록 및 분석


# 세션(Session): 상태를 기록하는 데이터
- 사이트와 특정 브라우저 사이의 **"state(상태)"**를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
- session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장

## 쿠키 Lifetime
1. Session cookie
   - current session이 종료되면 삭제됨
   - 브라우저 종료와 함께 세션이 삭제됨
2. Persistent cookies
   - `Expires` 속성에 지정된 날짜 혹은 `Max-Age`속성에 지정된 기간이 지나면 삭제됨

## Session in Django
- Django는 database-backed sessions 저장 방식을 기본값으로 사용
  - session 정보는 Django DB의 django_session 테이블에 저장
- Django는 특정 session_id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄


# Authentication in Web requests - Login
- 로그인은 **Session을 Create**하는 과정
- `AuthenticationForm`

## Login
- 로그인 페이지 작성  
![image](https://user-images.githubusercontent.com/108309396/226811687-e8400117-0549-4da4-94cd-d4369cff26b5.png)
- `login(request, user, backend=None)`
  - 인증된 사용자를 로그인시키는 로직으로 View 함수에서 사용됨
  - 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용
  - HttpRequest 객체와 User 객체가 필요
- 로그인 로직 작성 &rarr; view 함수 login과의 충돌방지 위해 `import login as auth_login`으로 변경  
![image](https://user-images.githubusercontent.com/108309396/226813024-ed83edc9-a336-489e-86e8-6186d80b6dcb.png)
- `get_user()`: AuthenticationForm의 인스턴스 메서드, 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환
- 로그인 링크 작성: 실습 편의를 위해 base.html에 하이퍼 링크 작성  
![image](https://user-images.githubusercontent.com/108309396/226814188-0f8dbd8b-6ecc-4bda-9202-c33a95574bf0.png)

## Authentication with User
- 현재 로그인 되어 있는 유저 정보 출력 &rarr; template에서 인증 관련 데이터 출력  
![image](https://user-images.githubusercontent.com/108309396/226814526-b1dd7462-330b-4dea-b2e5-eee1c5176c35.png)
- settings.py의 context processors 설정 값 때문에 context 데이터 없이 user 변수 사용 가능  

### context processors
- 템플릿이 렌더링될 때 호출 가능한 context data 목록
- 작성된 context data는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨  
![image](https://user-images.githubusercontent.com/108309396/226814802-49b0bf75-e165-4218-861f-77d9aecad659.png)
- 클라이언트가 로그인하지 않은 경우 `AnonymousUser` 클래스의 인스턴스로 생성  
![image](https://user-images.githubusercontent.com/108309396/226814995-6cefd298-9c84-4518-940e-110cd2814f80.png)

# Authentication in Web requests - Logout
- 로그아웃은 **Session을 Delete**하는 과정

## Logout
- `logout(request)`
- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류 발생X
1. 현재 요청에 대한 session data를 DB에서 삭제
2. 클라이언트의 쿠키에서도 session id를 삭제
   - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함
- 로그아웃 로직 작성  
![image](https://user-images.githubusercontent.com/108309396/226816020-692ba8c1-9c99-4119-a6c2-02d8cf2f55bb.png)  
![image](https://user-images.githubusercontent.com/108309396/226816085-ad62e033-abdb-4934-a94b-0f935e3f09bd.png)