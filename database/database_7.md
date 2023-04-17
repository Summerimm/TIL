# Django REST framework - Single Model 
- 단일 모델의 data를 Serialization하여 JSON으로 변환하는 방법에 대해 학습
- Postman: API를 구축하고 사용하기 위한 플랫폼, API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공

## ModelSerializer
- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
1. Model 정보에 맞춰 자동으로 필드 생성
2. serializer에 대한 유효성 검사기를 자동으로 생성
3. `.create()` 및 `.update()`의 간단한 기본 구현이 포함됨

### `many` option
- 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize하려면 `many=True` 작성

# Build RESTful API - Article
![image](https://user-images.githubusercontent.com/108309396/231641695-6a75b60a-165e-4125-9d6d-46d1b4e86b9b.png)  

## GET
1. GET - List  
![image](https://user-images.githubusercontent.com/108309396/231641808-abe02150-e99c-4e1f-8791-76ac588174ee.png)

### `@api_view` decorator
- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용, 다른 메서드 요청에 대해서는 405 Method Not Allowed

2. GET - Detail  
![image](https://user-images.githubusercontent.com/108309396/231641965-d1616433-6f6a-4a37-bfd1-b4ab3c7160a9.png)  
![image](https://user-images.githubusercontent.com/108309396/231642036-623b0fe7-70a0-4f0b-aa46-60e6d89b08e8.png)

## POST
1. POST - List
- 요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답  
![image](https://user-images.githubusercontent.com/108309396/232400987-2f5f7599-7b29-4fbd-b375-2835285edd0d.png)
- Raising an exception on invalid data: is_valid()의 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 raise_exception 인자 사용 가능
  - 기본적으로 HTTP 400 응답 반환  
![image](https://user-images.githubusercontent.com/108309396/232401651-fd68e006-8da3-4dde-8865-73ee717c2a26.png)

## DELETE
- 게시글 데이터 삭제
- 요청에 대한 데이터 삭제가 성공했을 경우 `204 No Content` 상태 코드 응답
  - 명령을 수행했고 더 이상 제공할 정보X  
![image](https://user-images.githubusercontent.com/108309396/232401861-a139732b-5cc8-43ca-a6ef-718842c42105.png)

## PUT
- 게시글 데이터 수정
- 요청에 대한 데이터 수정이 성공했을 경우 200 OK 상태코드 응답  
![image](https://user-images.githubusercontent.com/108309396/232402130-d46cc22b-b6a3-49b8-b8f4-b4433ed999e9.png)

# Django REST framework - N:1 Relation
- N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환하는 방법

## GET
1. GET - List
   - 댓글 데이터 목록 조회하기  
  ![image](https://user-images.githubusercontent.com/108309396/232402612-bbe52361-0111-4147-8ade-1550aa42272d.png)  
  ![image](https://user-images.githubusercontent.com/108309396/232402711-429ee608-c759-48b8-ba34-e201f7f33cb5.png)

2. GET - Detail
   - 단일 댓글 데이터 조회하기  
  ![image](https://user-images.githubusercontent.com/108309396/232403613-0ce2327a-aecf-4410-8bf4-e0d35bc4f3fe.png)

## POST
- 단일 댓글 데이터 생성하기  
![image](https://user-images.githubusercontent.com/108309396/232403720-7acb90ef-af5c-4186-b669-505f3e0360a8.png)
- `CommentSerializer`를 통해 Serialize되는 과정에서 Parameter로 넘어온 `article_pk`에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장  
![image](https://user-images.githubusercontent.com/108309396/232404006-f602d0d6-2e9f-4edc-870f-22dd3a637acd.png)
- `read_only_fileds`르 사용해 외래 키 필드를 **읽기 전용 필드** 설정
  - 읽기 전용 필드는 데이터를 전송하는 시점에 **해당 필드는 유효성 검사에서 제외시키고 데이터 조회 시에는 출력**하도록 함  
![image](https://user-images.githubusercontent.com/108309396/232404239-71b79b7b-e756-488a-b0b0-5a4fe6608eb2.png)

## DELETE & PUT
- 댓글 데이터 삭제 및 수정  
![image](https://user-images.githubusercontent.com/108309396/232404366-7e1b7167-c4e1-421e-9fda-22f78521816a.png)

# N:1 - 역참조 데이터 조회
### 1. 특정 게시글에 작성된 댓글 목록 출력하기
- 기존 필드 override - Article Detail
  - 게시글 조회 시 해당 게시글의 **댓글 목록**까지 함께 출력
1. `PrimaryKeyRelatedField()`  
![image](https://user-images.githubusercontent.com/108309396/232405051-999857dd-0906-4d88-beb0-0817f03b4316.png)  
  - models.py에서 `related_name`을 통해 이름 변경 가능
  - 역참조 시 생성되는 `comment_set`을 override할 수 있음  
  ![image](https://user-images.githubusercontent.com/108309396/232405340-259f67da-6325-428f-b06f-101ea1703c3f.png)

2. Nested relationships  
![image](https://user-images.githubusercontent.com/108309396/232405431-baef0135-342b-41b7-bca9-68959af6f169.png)
   - 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
   - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 가능
   - 상하 위치 중요

### 2. 특정 게시글에 작성된 댓글의 개수 출력하기
- 새로운 필드 추가 - Article Detail
  - 게시글 조회 시 해당 게시글의 **댓글 개수**까지 함께 출력  
![image](https://user-images.githubusercontent.com/108309396/232405904-dde535b9-14c7-4f9c-8a3e-5a7f2accdf95.png)
- `source`
  - serializers field's argument
  - 필드를 채우는 데 사용할 속성의 이름
  - dotted notation을 사용하여 속성 탐색 가능
- [주의] 읽기 전용 필드 지정 이슈
  - 특정 필드를 override 혹은 추가한 경우 `read_only_fields`가 동작하지 않으니 주의  
  ![image](https://user-images.githubusercontent.com/108309396/232406277-6ce46287-e14e-4942-9f63-b69ee0760eef.png)

# Django shortcuts functions
- `get_object_or_404()`
  - 모델 manager objects에서 `get()`을 호출하지만, 객체가 없을 시 Http404를 raise  
  ![image](https://user-images.githubusercontent.com/108309396/232406700-3c2115dd-3101-4957-b0dd-48a960b15c6e.png)
- `get_list_or_404()`
  - 모델 manager objects에서 `filter()`의 결과를 반환하고, 해당 객체 목록이 없을 때 Http404를 raise  

### 필요성
- 클라이언트 입장에서 "서버 오류 발생(500)"이라는 원인이 정확하지 않은 에러보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소