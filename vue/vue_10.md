# DRF Auth System
## Authentication - 인증, 입증
- 사용자가 누구인지 확인하는 행위
- 모든 보안 프로세스의 첫 번째 단계(가장 기본 요소)
- 401 Unauthorized
  - 비록 HTTP 표준에서는 "미승인(unauthorized)"을 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미

## Authorization - 권한 부여, 허가
- 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정(절차)
- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
- 인증이 되었어도 모든 권한을 부여받는 것은 아님
- 403 Forbidden
  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

## 인증 여부 확인 방법
- `settings.py`에 작성
  - 기본적인 인증 절차 방식
- DRF가 기본으로 제공해주는 인증 방식: `TokenAuthentication`
- 모든 상황에 대한 인증 방식을 정의
  - 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식 필요
- view 함수마다 다른 인증 방식을 설정하고자 한다면 decorator 활용  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/f273855b-5401-4c4b-976b-963171e3b88b)
- [참고] `permission_classes`
  - 권한 관련 설정
  - 권한 역시 특정 view 함수마다 다른 접근 권한을 요구할 수 있음

## 다양한 인증 방식
1. `BasicAuthentication`
   -  가장 기본적인 수준의 인증 방식
   -  테스트에 적합
2. `SessionAuthentication`
   - session 기반의 인증 시스템
   - DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이 존재
3. `RemoteUserAuthentication`
   - Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
4. `TokenAuthentication`
   - 매우 간단하게 구현 가능
   - 기본적인 보안 기능 제공
   - 다양한 외부 패키지 존재
- **`settings.py`에서 `DEFAULT_AUTHENTICATION_CLASSES`를 정의**
  - `TokenAuthentication` 인증 방식 명시

## TokenAuthentication 사용 방법
- `INSTALLED_APPS`에 `rest_framework.authtoken` 등록
- 각 User마다 고유 Token 생성  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/e61a5269-0a94-4783-acb3-03333522e6b6)
- 생성한 Token을 각 User에게 발급
  - User는 발급 받은 Token을 요청과 함께 전송
  - Token을 통해 User 인증 및 권한 확인
- Token 발급 방법  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/864f1e9b-c2b1-48cd-b9e2-3ffb31cb5ed5)
- User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
  - 단, 반드시 Token 문자열 함께 삽입
    - 삽입해야 할 문자열은 각 인증 방식마다 다름
  - 주의) Token 문자열과 발급받은 실제 token 사이를 `' '`(공백)으로 구분
- Authorization HTTP headers 작성 방법  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/5993ea99-7545-43a8-bfe6-e64e59b1a1ab)

## dj-rest-auth
- 회원가입, 인증(SNS 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공

### dj-rest-auth 사용 방법
1. 패키지 설치
2. App 등록
3. url 등록  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/4c6e5f1b-6109-4142-a79f-cecf476ee7f1)

### dj-rest-auth 사용하기
![image](https://github.com/Haaarimmm/TIL/assets/108309396/341404d9-0a2c-412d-a405-00e7b5d034e3)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/0caa1426-7591-48a7-8cdb-eccf2d7e4c6b)

### Registration
- `dj-rest-auth`의 회원가입 기능을 사용하기 위해서는 `django-allauth` 필요
- `django-allauth` 설치  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/92f3b3c9-ea86-4312-8b72-ec62475f87f7)
![image](https://github.com/Haaarimmm/TIL/assets/108309396/7295339f-24fb-454d-bd47-e094a2f87684)
- `my_api/settings.py` APP 등록 및 SITE_ID 설정
- `SITE_ID`: 하나의 컨텐츠를 기반으로 여러 도메인에 컨텐츠를 게시 가능
  - 다수의 도메인이 하나의 DB에 등록
  - 현재 프로젝트가 첫 번째 사이트임을 나타냄

## Permission Setting
- 권한 세부 설정
  - 모든 요청에 대해 인증을 요구하는 설정
  - 모든 요청에 대해 인증이 없어도 허용하는 설정
- 설정 위치 == 인증 방법을 설정한 곳과 동일
  - 우선 모든 요청에 대해 허용 설정  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/c8b1c808-fba5-4e19-b79f-c508ae785e3b)

### 정리
1. 인증 방법 설정
   - `DEFAULT_AUTHENTICATION_CLASSES`
2. 권한 설정하기
   - `DEFAULT_PERMISSION_CLASSES`
3. 인증 방법, 권한 세부 설정도 가능
   - `@authentication_classes`
   - `@permission_classes`
4. 인증 방법은 다양한 방법이 있으므로 내 서비스에 적합한 방식을 선택

# DRF Auth with Vue