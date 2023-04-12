# A many-to-one relationship
- 관계형 데이터베이스에서의 외래 키 속성을 사용해 모델간 N:1 관계 설정하기

## RDB에서의 관계
1. 1:1
   - One-to-one relationships
   - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. N:1
   - Many-to-one relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
   - 기준 테이블에 따라(1:N, One-to-many relationships)이라고도 함
   - 주문 테이블과 고객 테이블(고객(1)은 여러 주문(N)을 진행할 수 있음)
3. M:N
   - Many-to-many relationships
   - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
   - 양쪽 모두에서 N:1 관계를 가짐
   - 태그(1개의 태그는 여러 개의 게시물과, 하나의 게시물은 여러 개의 태그를..)

## Forign key
- 키를 사용하여 부모 테이블의 유일한 값을 참조(by 참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

### 참조 무결성
- 데이터베이스 관계 모델에서 관련된 2개의 테이블 간 일관성을 의미
- 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함 

# N:1 (Comment - Article)
- Comment(N) - Article(1)
- Comment 모델과 Article 모델 간 관계 설정
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음

### 모델 관계 설정
![image](https://user-images.githubusercontent.com/108309396/230914094-d7a95fad-0abe-446e-b425-1e18942658da.png)  
![image](https://user-images.githubusercontent.com/108309396/231045496-3d102118-5992-49fa-93f3-75f6a9d6e5c2.png)  

### Django Relationship fields
1. `OneToOneField()` - 1:1
2. `ForeignKey()` - N:1
3. `ManyToManyField()` - M:N

### `ForeignKey(to, on_delete, **options)`
- N:1을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 RDB의 FK속성을 담당
- 2개의 필수 위치 인자가 필요
  - 참조하는 `model class`
  - `on_delete` 옵션

## Comment Model
![image](https://user-images.githubusercontent.com/108309396/231045883-88b253ab-0adb-4913-a714-4c2bafc1a419.png)  
- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨(ex. `article_id`)
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

### ForeignKey arguments - `on_delete`
- 외래 키가 참조하는 객체가 사라졌을 때, **외래 키를 가진 객체를 어떻게 처리할지를 정의**
- 데이터 무결성을 위해서 매우 중요한 설정
- `on_delete` 옵션 값
  - `CASCADE`: 부모 객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제
  - `PROTECT, SET_NULL, SET_DEFAULT...`

## 댓글 생성 연습하기
1. 댓글 생성  
![image](https://user-images.githubusercontent.com/108309396/231046164-3e8bdcec-45a8-4790-8331-e898688ef4f6.png)  
![image](https://user-images.githubusercontent.com/108309396/231046263-587ebbf7-5f73-4ddd-89db-44b025e9adf0.png)  
2. 댓글 속성 값 확인  
![image](https://user-images.githubusercontent.com/108309396/231046359-6b540010-dea0-42c1-8a37-bda986eb0f26.png)  
3. comment 인스턴스를 통한 article 값 접근하기  
![image](https://user-images.githubusercontent.com/108309396/231046437-4034b97b-4f9f-4686-b240-ef2fdce1eba8.png)  
4. 두 번째 댓글 작성해보기  
![image](https://user-images.githubusercontent.com/108309396/231046520-afac0e58-d691-4832-a531-9564d629d7fd.png)  

## 관계 모델 참조
### `Related manager`
- N:1 혹은 M:N 관계에서 사용 가능한 context
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조**할 때에 사용할 수 있는 manager를 생성
  - 역참조란? 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - N:1 관계에서 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조

### `article.comment_set.method()`
- Article 모델이 Comment 모델을 역참조할 때 사용하는 매니저
- article.comment 형식으로는 참조 불가
- 대신 Django가 역참조할 수 있는 comment_set manager를 자동으로 생성해 댓글 객체 참조 가능

## Related manager 연습하기
1. 1번 게시글 조회  
![image](https://user-images.githubusercontent.com/108309396/231047395-81c33427-f4e5-44c1-b21c-ddc27c1fe788.png)  
2. dir() 함수를 사용해 클래스 객체가 사용할 수 있는 메서드를 확인하기  
![image](https://user-images.githubusercontent.com/108309396/231047459-5304aaf8-93f7-4b3b-bb79-68b2540ddae7.png)  
3. 1번 게시글에 작성된 모든 댓글 조회하기(역참조)  
![image](https://user-images.githubusercontent.com/108309396/231047548-20afe78d-6587-4339-86cc-fe3305aa75d5.png)
4. 1번 게시글에 작성된 모든 댓글 출력하기  
![image](https://user-images.githubusercontent.com/108309396/231047596-68ca9d22-96a9-4de3-8c18-7a54ea728cd8.png)

## ForeignKey arguments - `related_name`
![image](https://user-images.githubusercontent.com/108309396/231047808-34d40439-b095-4047-9e42-d24b10d7d532.png)  
- 역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있음
- 위와 같이 변경하면 기존 article.comment_set은 더 이상 사용할 수 없고, article.comments로 대체됨

### admin site 등록
- 새로 작성한 Comment 모델을 admin site에 등록하기  
![image](https://user-images.githubusercontent.com/108309396/231061181-daf8487a-238f-4255-9b2a-db625572f1a5.png)

# Comment 구현
### CREATE
- CommentForm 작성(외래 키 필드를 출력에서 제외)    
![image](https://user-images.githubusercontent.com/108309396/231061908-e9d33650-e98b-40db-841d-efbb222ff40e.png)
- detail페이지에서 CommentForm 출력(view)  
![image](https://user-images.githubusercontent.com/108309396/231061620-f80c6ec9-0e66-43c4-a467-d869086452d6.png)
  - ArticleForm 클래스의 인스턴스명을 form으로 작성했기 때문에 헷갈리지 않도록 comment_form으로 작성
- detail.html  
![image](https://user-images.githubusercontent.com/108309396/231061753-553a5995-4706-4c68-b9f8-d9f183aaa4de.png)
- urls, detail.html  
![image](https://user-images.githubusercontent.com/108309396/231062167-c0db3680-63b9-419d-a8b4-2bb741c81900.png)  
![image](https://user-images.githubusercontent.com/108309396/231062202-2bb70ae7-7c53-4e5b-a29d-e18e4020f7a0.png)
- views, `save()` 메서드의 `commit` 옵션을 사용해 DB에 저장되기 전 article 객체 저장하기  
![image](https://user-images.githubusercontent.com/108309396/231062422-f7a0374c-d881-423e-9675-7a518e90afd4.png)

## READ
- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가  
![image](https://user-images.githubusercontent.com/108309396/231062708-91b63775-fd30-4ce5-a310-e285e5697b20.png)  
- detail 템플릿에서 댓글 목록 출력하기  
![image](https://user-images.githubusercontent.com/108309396/231062790-f544af50-86a8-42c6-a98c-951a0bb9e662.png)

## DELETE
- 댓글 삭제(url, view)  
![image](https://user-images.githubusercontent.com/108309396/231063013-8fbc25e9-81b0-4750-a9ba-87758780be10.png)  
![image](https://user-images.githubusercontent.com/108309396/231063057-8187ccd2-2a55-4846-ac0e-661c3bb5c3cb.png)
- 댓글 삭제 버튼(detail.html)  
![image](https://user-images.githubusercontent.com/108309396/231063160-1596ba78-fe0f-4283-a63c-686aca2b64aa.png)

### Comment 추가 사항
1. 댓글 개수 출력하기
   - DTL filter - `length` 사용  
![image](https://user-images.githubusercontent.com/108309396/231063318-7c2c5d4a-6281-4f13-a773-8aed2e043621.png)
   - Queryset API - `count` 사용  
![image](https://user-images.githubusercontent.com/108309396/231063377-31eccaf5-1db0-4a9f-9afc-2b664d1f5f7a.png)
  - detail 템플릿에 작성  
![image](https://user-images.githubusercontent.com/108309396/231063555-afb7719e-80ab-4d6b-95ce-d408ec46ae5d.png)  
![image](https://user-images.githubusercontent.com/108309396/231063604-962b6187-eb3b-4597-ab33-7be0cc2a6c33.png)  
2. 댓글이 없는 경우 대체 컨텐츠 출력하기
  - DTL `for empty` 활용하기  
![image](https://user-images.githubusercontent.com/108309396/231063711-23ca28ee-7fbb-495b-a549-e7c02ae94fe3.png)


# N:1 (Article - User)
- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

## Referencing the User model
1. `settings.AUTH_USER_MODEL`
   - 반환 값: `accounts.User`(문자열)
   - User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용
   - **models.py의 모델 필드에서 User 모델을 참조할 때 사용**
2. `get_user_model()`
   - 반환 값: `User Object`(객체)
   - 현재 active된 User 모델을 반환
   - 커스터마이징한 User 모델이 있는 경우는 CustomUser 모델, 그렇지 않으면 User를 반환
   - **models.py를 제외한 모든 곳에서 User 모델을 참조할 때 사용**

### 모델 관계 설정
![image](https://user-images.githubusercontent.com/108309396/231065305-346510fe-bfc3-464a-a8cb-a7a7f686232d.png)  
![image](https://user-images.githubusercontent.com/108309396/231065456-0f249e51-8b30-4f03-96a0-7686df4b136f.png)
- Article 모델에 User 모델을 참조하는 외래 키 작성
- `makemigrations` 진행 시 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황
  - 기본값을 어떻게 작성할 것인지 선택해야 함
  - 1 입력 후 article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함

## CREATE
- user 필드에 작성해야 하는 user 객체는 view 함수의 request 객체를 활용해야 함  
- ArticleForm의 출력 필드 수정  
![image](https://user-images.githubusercontent.com/108309396/231065879-4f95d919-335b-4ae7-ab22-925705d21143.png)
- 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 `commit` 옵션을 활용  
![image](https://user-images.githubusercontent.com/108309396/231066024-f6bb0ec5-c7e6-425f-a6ff-f7aed02ada54.png)

## DELETE
- 게시글에 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함  
![image](https://user-images.githubusercontent.com/108309396/231066130-cef71071-b983-4bc3-a79f-b63bf1c721df.png)


## UPDATE
- 수정을 요청하는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함  
![image](https://user-images.githubusercontent.com/108309396/231066945-e4e3ee72-444b-48ad-9cdc-b63c6ccf2d5d.png)
- 추가로 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함  
![image](https://user-images.githubusercontent.com/108309396/231067025-fe2056c9-93c0-40f5-ade2-af62ef762bbf.png)

## READ
- index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력  
![image](https://user-images.githubusercontent.com/108309396/231067186-571f77eb-d859-4853-89a5-5e1cd2f3b33b.png)  
![image](https://user-images.githubusercontent.com/108309396/231067218-38bf8776-6999-4564-83d4-967b9e4ce498.png)
