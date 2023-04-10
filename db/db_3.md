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

### 모델관계 설정
<img width="527" alt="image" src="https://user-images.githubusercontent.com/108309396/230914094-d7a95fad-0abe-446e-b425-1e18942658da.png">  

### Django Relationship fields
1. OneToOneField() - 1:1
2. ForeignKey() - N:1
3. ManyToManyField() - M:N

### ForeignKey(to, on_delete, **options)
- N:1을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 RDB의 FK속성을 담당
- 2개의 필수 위치 인자가 필요
  - 참조하는 `model class`
  - `on_delete` 옵션

### Comment Model
<img width="539" alt="image" src="https://user-images.githubusercontent.com/108309396/230916258-76ac2585-3de6-405a-8b75-817c4a475d3a.png">  
- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

### ForeignKey arguments - `on_delete`
- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지를 정의
- 데이터 무결성을 위해서 매우 중요한 설정
- `on_delete` 옵션 값
  - `CASCADE`: 부모 객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제
  - `PROTECT, SET_NULL, SET_DEFAULT...`

# N:1 (Article - User)