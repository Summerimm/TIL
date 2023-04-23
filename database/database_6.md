# HTTP
## HTTP Request Methods
1. `GET`
   - 서버에 리소스의 표현을 요청
   - GET을 사용하는 요청은 데이터만 검색해야 함
2. `POST`
   - 데이터를 지정된 리소스에 제출
   - 서버의 상태를 변경
3. `PUT`
   - 요청한 주소의 리소스를 수정
4. `DELETE`
   - 지정된 리소스를 삭제

## HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료되었는지 여부
1. Informational reponses(100-199)
2. Successful responses(200-299)
3. Redirection messages(300-399)
4. Client error responses(400-499)
5. Server error responses(500-599)

## 웹에서의 리소스 식별
- HTTP 요청의 대상을 resource라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든
- 각 리소스는 식별을 위해 `URI`로 식별됨

## URI
- Uniform Resource Identifier(통합 자원 식별자)
- 인터넷에서 리소스를 식별하는 문자열
- 가장 일반적인 URI는 웹 주소로 알려진 **URL**  
![image](https://user-images.githubusercontent.com/108309396/231621624-6f5d2f1b-a0f3-4450-82f7-273e97dc0fee.png)
- 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 **URN**
  - 리소스를 찾아가는 경로를 제공X  
![image](https://user-images.githubusercontent.com/108309396/231621741-cfdeb834-80f3-451c-8d0a-86825531a035.png)

### URL
- Uniform Resource Locator(통합 자원 위치)
- 웹에서 주어진 리소스의 주소  
![image](https://user-images.githubusercontent.com/108309396/231621930-ea0e9a6e-9997-4b13-941d-2e83003b32e5.png)

### URL 구조
- Scheme(or protocol)
  - 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
  - 브라우저가 어떤 규약을 사용하는지
  - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 `mailto:`, 파일을 전송하기 위한 `ftp:` 등 다른 프로토콜도 존재
- Authority
  - domain과 port를 모두 포함하며 둘은 `:`으로 구분됨
  1. Domain Name
    - 요청 중인 웹 서버, 직접 IP주소를 사용하는 것도 가능
  2. Port
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 Gate
    - HTTP 프로토콜의 표준 포트는 (HTTP - 80, HTTPS: 443)이고 생략이 가능(나머지는 생략 불가능)
    - Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음
- Path
  - 웹 서버의 리소스 경로
  - 오늘 날엔 실제 위치가 아닌 추상화된 형태의 구조를 표현
- Parameters
  - 웹 서버에 제공하는 추가적인 데이터
  - `&`기호로 구분되는 key-value 쌍 목록
- Anchor
  - 리소스의 다른 부분에 대한 앵커
  - 리소스 내부 일종의 '북마크'를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시
  - fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송X
  - 하이퍼링크와 비슷한 기능을 하는 인터넷 상의 다른 문서와 연결된 문자 혹은 그림

### URN
- Uniform Resource Name(통합 자원 이름)
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함(독립적 이름)
- URL의 단점을 극복하기 위해 등장
- 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원을 식별
- 하지만 이름만으로 실제 리소스를 찾는 방법은 보편화X 현재는 URL을 대부분 사용


# REST API
## API
- Application Programming Interface
- 애플리케이션과 프로그래밍으로 소통하는 방법
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등 사이의 간단한 계약(인터페이스)이라고 볼 수 있음
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공
- API는 다양한 타입의 데이터를 응답: HTML, XML, JSON 등

## REST
- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- 소프트웨어 아키텍쳐 디자인 제약 모음
- REST의 기본 아이디어는 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술
1. 자원의 식별: URI
2. 자원의 행위: HTTP Method
3. 자원의 표현: JSON, 자원과 행위를 통해 궁극적으로 표현되는 (추상화된)결과물

### JSON
- lightweight data-interchange format
- JavaScript의 표기법을 따른 단순 문자열
- **key-value 형태의 구조** : Python의 Dictionary와는 다름


# Response JSON
### 사전준비
1. json_response 프로젝트 준비
2. 가상 환경 생성, 활성화 및 패키지 설치
3. migrate 진행
4. 준비된 fixtures 파일을 load하여 실습용 초기 데이터 입력
5. urls 작성

### JSON 데이터를 응답하는 다양한 방법
1. HTML 응답
2. JsonResponse()
3. Django Serializer
4. Django REST framework

## 1. HTML 응답  
![image](https://user-images.githubusercontent.com/108309396/231638309-806f67cc-56aa-4929-b130-08dae5694f3e.png)  
![image](https://user-images.githubusercontent.com/108309396/231638514-15a481a7-5ff0-4e60-9306-eab695d872da.png)  

## 2. JsonResponse()
- 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능   
- JsonResponse()
  - `safe` parameter: 기본 값 True, False로 설정 시 모든 타입의 객체를 serialization 가능(하지 않으면 dict 인스턴스만 허용) 
![image](https://user-images.githubusercontent.com/108309396/231638958-3216b1df-1e67-4c59-a262-af1ae56883ba.png)

## 3. Django Serializer를 사용한 JSON 응답
- Django의 내장 HttpResponse()를 활용한 JSON 응답
- JSON의 모든 필드를 일일이 작성할 필요X  
![image](https://user-images.githubusercontent.com/108309396/231640420-edd40fd6-e331-4dd8-9ada-4163e0da9075.png)

### Serialization
- 직렬화
- 여러 시스템에서 활용하기 위해 데이터구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 변환 포맷은 json, xml, yaml이 있으며 json이 가장 보편적  
![image](https://user-images.githubusercontent.com/108309396/231640582-8ef837bf-4fb0-4abb-a6df-70900353b470.png)

## 4. Django REST framework(DRF)를 사용한 JSON 응답
- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 유사하게 작동
- DRF 설치 확인  
![image](https://user-images.githubusercontent.com/108309396/231640963-65ec1739-6a2c-40a5-9b1c-19b570ac8b10.png)
- `ModelSerializer`  
![image](https://user-images.githubusercontent.com/108309396/231641034-89694fdd-f4eb-4a61-9ca8-fd9f0d85488d.png)

### 직접 requests 라이브러리를 사용하여 json 응답 받아보기  
![image](https://user-images.githubusercontent.com/108309396/231641202-4f934901-8700-4806-be58-578a4746e727.png)