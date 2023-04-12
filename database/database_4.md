# N:1 (Comment - User)
- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음

### 모델 관계 설정
![image](https://user-images.githubusercontent.com/108309396/231322556-6f83403b-eeda-4cd0-aa6d-3844450ed02b.png)  
![image](https://user-images.githubusercontent.com/108309396/231322615-83b752c1-b0bb-438c-a49a-fea18124e3f9.png)  
- Comment 모델에 User 모델을 참조하는 FK 작성
- Migration 진행 시 기존에 존재하던 테이블에 새로운 컬럼이 추가되는 상황
- 기본적으로 모든 컬럼은 `NOT NULL` constraints가 있기 때문에 데이터 없이는 새로 추가되는 FK 필드인 user_id가 생성되지 않음
- 기본값을 어떻게 작성할 것인지 선택해야 함 &rarr; 1 입력 후 직접 기본 값 입력

## CREATE
- 인증된 회원의 댓글 작성 구현
1. CommentForm의 출력 필드 수정(User 선택은 안 보이게)  
![image](https://user-images.githubusercontent.com/108309396/231323018-cc5844d3-3395-4911-9bad-76d4ab2f39ec.png)  
2. 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 `commit` 옵션 활용  
![image](https://user-images.githubusercontent.com/108309396/231323105-9c90a556-e428-4f14-b132-820c5e3cf457.png)   

## READ
- detail 템플릿에서 각 게시글의 작성자 출력  
![image](https://user-images.githubusercontent.com/108309396/231323217-5faf217c-6a81-4b74-b94e-19166db8c438.png)  

## DELETE
1. 댓글 삭제 시 작성자 확인
- 현재 삭제를 요청하는 사람과 댓글을 작성한 사람이 일치한 경우만 삭제할 수 있도록 구현  
![image](https://user-images.githubusercontent.com/108309396/231323319-959b9015-2301-4901-9c6c-76ccb2f3649d.png)  
2. 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼이 출력되지 않도록 함  
![image](https://user-images.githubusercontent.com/108309396/231323496-498e52f2-ce2f-4e79-bdd2-8fc3d98a9556.png)  

## 인증된 사용자에 대한 접근 제한하기
- `is_authenticated`와 `View decorator` 사용
1. 인증된 사용자인 경우만 댓글 작성 및 삭제  
![image](https://user-images.githubusercontent.com/108309396/231323641-23f6da8f-bff7-48ca-a48e-bb30d2b80b39.png)   
![image](https://user-images.githubusercontent.com/108309396/231323702-2b81edce-ab38-405b-bd68-662d4670330b.png) 
2. 비인증 사용자는 CommentForm을 볼 수 없도록 하기  
![image](https://user-images.githubusercontent.com/108309396/231323771-ce042e6a-b10f-4e81-b49a-a8afc744e1e4.png)



# Many-to-many-relationship
### [참고] 데이터 모델링
- 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
- 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업
- target model: 관계 필드를 가지지 않은 모델
- source model: 관계 필드를 가진 모델

- 별도의 예약 모델을 새로 작성
## 중개모델
- 예약 모델은 의사와 환자에 **각각 N:1 관계**를 가짐  
![image](https://user-images.githubusercontent.com/108309396/231324193-659a3ca4-3747-44b2-9fdf-1ca3be5dd31d.png)

### 중개모델 확인
1. 의사와 환자 객체 생성 후 예약 만들기  
![image](https://user-images.githubusercontent.com/108309396/231324456-cae5472f-0bbc-4d7c-b50a-7e4b1c6da8a3.png)  
![image](https://user-images.githubusercontent.com/108309396/231324540-7f3e606a-ca14-4dd7-bcd3-c3809a2d199a.png)  
2. 예약 정보 조회(역참조)  
![image](https://user-images.githubusercontent.com/108309396/231324583-197d7426-0e51-4737-8f42-9f5bb9d6d7a8.png)  
3. 1번 의사에게 새로운 환자 예약이 생성된다면  
![image](https://user-images.githubusercontent.com/108309396/231329609-7c0fc137-0309-4daf-b20f-3b1dd32b33b7.png)    
![image](https://user-images.githubusercontent.com/108309396/231324691-93f0f5fb-1fe1-4f5c-831f-3dff6ca92307.png)

### 중개 테이블 필드 생성 규칙
1. source model 및 target model이 다른 경우
   - id
   - <containing_model>_id
   - <other_model>_id
2. ManyToManyField가 동일한 모델을 가리키는 경우
   - id
   - from_<model>_id
   - to_<model>_id

## Django ManyToManyField
- 환자 모델에 Django ManyToManyField 작성  
![image](https://user-images.githubusercontent.com/108309396/231324806-964626ba-d2cb-4e6b-93f5-39a1fb407840.png)
- 생성된 중개 테이블 `hospitals_patient_doctors  
![image](https://user-images.githubusercontent.com/108309396/231324840-6e4950e9-0bbf-4b99-82c1-c27cbce4c61e.png)

### ManyToManyField 확인
- 의사 1명과 환자 2명 생성  
![image](https://user-images.githubusercontent.com/108309396/231324998-0c26b667-f1d5-49c4-b495-4b8b86fe2104.png)
- 예약 생성(환자가 의사에게 예약)  
![image](https://user-images.githubusercontent.com/108309396/231325064-a4a6aa44-a972-4853-8390-36d0b7f76209.png)
- 예약 생성(의사가 환자를 예약)  
![image](https://user-images.githubusercontent.com/108309396/231325144-339d1fbe-409c-4ef3-ad9a-cc698e366edf.png)
- 예약 취소하기(삭제): 기존에는 해당 Reservation을 찾아 지웠다면 이제는 `.remove()` 사용  
![image](https://user-images.githubusercontent.com/108309396/231325217-97de146d-282c-48b2-a145-47e23174071c.png)

### `realated_name` argument
- target model이 source model을 참조할 때 사용할 manager name
- `ForeignKey()`의 `related_name`과 동일  
![image](https://user-images.githubusercontent.com/108309396/231325479-02358d50-33f3-432e-ba6e-56b1b5badd6f.png)  

### `realated_name` argument 확인
- related_name 설정 값 확인  
![image](https://user-images.githubusercontent.com/108309396/231325529-13f842fe-37b2-4845-b1be-8ea47e21ace6.png)  

### `through` argument
- 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용 가능
- 가장 일반적인 용도는 **중개테이블에 추가 데이터를 사용해** 다대다 관계와 연결하려는 경우

### `through` argument 확인
1. through 설정 및 Reservation Class 수정
   - 이제는 예약 정보에 증상과 예약일이라는 추가 데이터가 생김  
![image](https://user-images.githubusercontent.com/108309396/231325827-061fff4e-0f31-44c7-ac08-e5f27caac041.png)
2. 의사 1명과 환자 2명 객체 생성
3. Reservation class를 통한 예약 생성 1  
![image](https://user-images.githubusercontent.com/108309396/231326112-38c07747-20b0-4913-8d0a-4e156eb5a8a0.png)  
4. Patient 객체를 통한 예약 생성: through_defaults 값에 딕셔너리 타입으로 입력  
![image](https://user-images.githubusercontent.com/108309396/231326363-a84df7bf-7526-4c73-8d34-4aab18270f00.png)
5. 예약 삭제  
![image](https://user-images.githubusercontent.com/108309396/231326487-333595e1-caea-4a32-9b69-91c9aecc0078.png)


## `ManyToManyField(to, **options)`
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관없음
- 대신 필드 작성 위치에 따라 참조, 역참조 방향을 주의할 것
- source model이 target model을 참조하는 것은 정참조
- 반대는 역참조
- `to`: 필수 위치인자(M:N 관계로 설정할 모델 클래스)
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
  - `add(), remove(), create(), clear()...`

### 데이터베이스에서의 표현
- 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨
- `db_table` arguments를 사용하여 중개 테이블의 이름 변경 가능

### ManyToManyField's Arguments
1. `related_name`
   - target model이 source model을 참조할 때(역참조) 사용할 manager name
2. `through`
   - 중개 테이블을 직접 작성하는 경우 사용
   - 일반적으로 extra data with a many-to-many relationship에 사용
3. `symmetrical`
   - 기본 값: True
   - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용    
    ![image](https://user-images.githubusercontent.com/108309396/231327397-693529a3-fa3d-4b40-b35b-4502994c25e3.png)
   - True 일 경우
     - _set 매니저 추가X
     - 정참조 시 자동으로 target model 인스턴스도 source model 인스턴스를 역참조 하도록 함(대칭)
   - 대칭을 원하지 않는 경우 False로 설정(ex. Follow)

### ManyToManyField Related manger's methods
1. `add()`
   - 지정된 객체를 관련 객체 집합에 추가
   - 모델 인스턴스, PK를 인자로 허용
2. `remove()`
   - 관련 객체 집합에서 지정된 모델 개체를 제거
   - 내부적으로 `QuerySet.delete()`를 사용하여 관계가 삭제됨
   - 모델 인스턴스, PK를 인자로 허용


# M:N (Article-User)
- Article-User간의 M:N 관계 설정을 통한 **좋아요 기능 구현**

### 모델 관계 설정
- ManyToManyField 작성: like_users 필드 생성 시 자동으로 역참조에 `.article_set` 매니저가 사용됨
- user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 구분 못 함
- 따라서 user와 관계된 ForeignKey 혹은 MTMField에 related_name을 작성해야 함  
![image](https://user-images.githubusercontent.com/108309396/231328706-8f1d4951-0d03-4614-b044-451e0af6db35.png)  
- related manager 정리  
![image](https://user-images.githubusercontent.com/108309396/231329085-90030389-52b9-4501-a925-cb864cbff2b1.png)

## LIKE 구현
1. url, view  
![image](https://user-images.githubusercontent.com/108309396/231329168-328f3f82-fb1a-4c88-aba6-e6c929c8aacb.png)
- `.exists()`: QuerySet에 결과가 포함되어 있으면 True 반환, 아니면 False 반환
2. index 템플릿에서 각 게시글에 좋아요 버튼 출력  
![image](https://user-images.githubusercontent.com/108309396/231329345-ebf58fee-fcdb-41b1-8ab5-bcf2d2bbfca8.png)
3. decorator 및 is_authenticated 추가  
![image](https://user-images.githubusercontent.com/108309396/231329438-9790b26a-1def-42a1-9601-fe6b2eba5ab2.png)