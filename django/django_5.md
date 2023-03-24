# Django Form
- **유효성 검증**이 반드시 필요
- Form은 Django의 유효성 검사 도구 중 하나로 중요한 방어 수단
- Django Form은 훨씬 쉽게 유효성 검증을 진행할 수 있도록 함

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

## Django Form Class
### 1. Form Class 선언
- Model Class를 선언하는 것과 비슷함
- Model과 마찬가지로 상속을 통해 선언
- 앱 폴더에 `forms.py`를 생성 후 ArticleForm Class 선언  
![image](https://user-images.githubusercontent.com/108309396/226525544-57b7ce0f-85f5-473d-9fb3-4d9ccd1a84b3.png)
- form에는 model field와 달리 TextField가 존재하지 않음
- Form Class를 forms.py에 작성하는 것은 규약이 아님 &rarr; 권장사항

### 2. view 업데이트  
![image](https://user-images.githubusercontent.com/108309396/226525759-8f6bec66-0db1-4f34-8041-cdd3157279c3.png)

### 3. create 템플릿 업데이트
![image](https://user-images.githubusercontent.com/108309396/226525905-82f81fab-c6bf-412a-b311-78771add7f0e.png)  

### +) Form rendering options
- `<label> & <input>` 쌍에 대한 3가지 출력 옵션
1. `as_p()`: 각 필드가 단락(`<p>`태그)으로 감싸져서 렌더링
2. `as_ul()`: 각 필드가 목록 항목(`<li>`태그)으로 감싸져서 렌더링 &rarr; <ul> 태그는 직접 작성해야함
3. `as_table()`: 각 필드가 테이블(`<tr>`태그)으로 감싸져서 렌더링



## Django ModelForm
- Model을 통해 Form Class를 만들 수 있는 helper class
- ModelForm은 Form과 똑같은 방식으로 view 함수에서 사용

### ModelForm 선언
- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정  
![image](https://user-images.githubusercontent.com/108309396/226528031-922e10ed-b955-433f-849e-d90d3e6a3777.png)

### ModelForm에서의 Meta Class
- ModelForm의 정보를 작성하는 곳
- 참조할 모델 &rarr; Meta class의 model 속성
  - 참조하는 모델에 정의된 field 정보를 Form에 적용함
- `fields` 속성에 `'__all__'`를 사용하여 모델의 모든 필드 포함 가능
- 또는 `exclude` 속성을 사용하여 모델에서 포함되지 않을 필드 지정 가능
- `fields`와 `exclude`는 함께 작성해도 되지만 권장X  
![image](https://user-images.githubusercontent.com/108309396/226529114-f8b1f6ff-e3dd-4021-a31e-f8eef551dd3b.png)

# ModelForm with view functions
## CREATE
- 유효성 검사를 통과하면 데이터 저장 후 상세 페이지로 redirect
- 통과하지 못하면 작성 페이지로 redirect   
![image](https://user-images.githubusercontent.com/108309396/226829267-014bb310-40be-4eeb-a491-722b5f0be630.png)

### `is_valid()` method
- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

### `save()` method
- form 인스턴스에 바인딩된 데이터를 통해 DB 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 생성할지, 수정할지를 결정함
  - **instance 없는 경우** save()는 지정된 모델의 새 인스턴스 생성(`CREATE`)
  - **instance 제공되면** save()는 해당 인스턴스를 수정(`UPDATE`)  
![image](https://user-images.githubusercontent.com/108309396/226532368-efe794c0-afbb-4e1b-b452-d8a925f5b681.png)

---
## UPDATE
- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
1. `request.POST`: 사용자가 form을 통해 전송한 데이터(새로운 데이터)
2. `instance`: 수정이 되는 대상

### Update view / template 수정  
![image](https://user-images.githubusercontent.com/108309396/226533077-cbd8ffc1-0de6-4b5b-beff-9dedd7f7bbfb.png)  
![image](https://user-images.githubusercontent.com/108309396/226533119-816cdd81-d115-41c9-8274-5307a0447587.png)  

---
## Form과 ModelForm 비교
- 각자 역할이 다름
1. Form
   - 사용자의 입력을 필요로 하고 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때
2. ModelForm
   - 사용자의 입력을 필요로 하고 입력을 받은 것을 그대로 DB 필드에 맞춰 저장할 때
   - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save() 호출이 가능
---
## Django의 2가지 HTML input 요소 표현
1. Form fields
     - 입력에 대한 유효성 검사 로직 처리
     - 템플릿에서 직접 사용  
![image](https://user-images.githubusercontent.com/108309396/226526341-40ee92ec-7d9e-4ee8-a175-6244e0bce5b3.png)
1. Widgets
     - 웹 페이지의 HTML input element 렌더링을 담당: 단순히 input 요소의 보여지는 부분을 변경
     - 유효성 검증과 아무런 관계가 없음
     - Widgets은 반드시 form fields에 할당됨    
![image](https://user-images.githubusercontent.com/108309396/226526364-9a21c0df-4cba-4a64-8c99-6cb72d2be789.png)

## Widgets을 작성하는 2가지 방법  
- 오른쪽 작성 방식 권장   
![image](https://user-images.githubusercontent.com/108309396/226533838-058c3281-3b00-4146-ba1f-78a741abc7cb.png)   
![image](https://user-images.githubusercontent.com/108309396/226533913-49180bb6-647c-44e7-9adc-67b71b398e2f.png)
# Static files
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- **파일 자체가 고정**되어 있고, 서비스 중에도 추가되거나 **변경되지 않고 고정**되어있음
  - 일반적으로 이미지, 자바 스크립트, CSS와 같이 미리 준비된 추가 파일(움직이지 않는)
- Django는 `staticfiles` 앱을 통해 정적 파일과 관련된 기능 제공
- 사진 파일은 resource이고 해당 사진 파일을 얻기 위한 경로인 웹 주소(URL)가 존재
- 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함

### Django에서 정적파일을 구성하고 사용하기 위한 단계
1. `settings.py`에서 `STATIC_URL`을 정의하기
2. 앱의 static 폴더에 정적 파일을 위치하기 - `my_app/static/sample_img.jpg`
3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기  
![image](https://user-images.githubusercontent.com/108309396/226535276-88c75a01-83be-411b-a475-3289cb267eb6.png)

### Django template tag
- `{% load %}`: load tag, 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
- `{% static '' %}`: static tag, STATIC_ROOT에 저장된 정적 파일에 연결

### Static files 관련 settings
1. `STATIC_ROOT`
2. `STATICFILES_DIRS`
3. `STATIC_URL`  
![image](https://user-images.githubusercontent.com/108309396/226536894-c1e8a0c8-1cc6-4be0-84f1-ca3b7404c67c.png)  
![image](https://user-images.githubusercontent.com/108309396/226536937-5428e459-e9b5-4c0d-bae7-698f376dbafd.png)  
![image](https://user-images.githubusercontent.com/108309396/226536967-b753f4fc-f447-41b4-9844-bbf017470c35.png)  
![image](https://user-images.githubusercontent.com/108309396/226537016-099d55c9-a63e-4373-a4d0-c29cbc0b0056.png)  


### Static file 가져오기
1. 기본 경로에 있는 static file 가져오기  
![image](https://user-images.githubusercontent.com/108309396/226830864-f95d0e33-182a-45bc-b1d9-2a46a60c2e23.png)  
![image](https://user-images.githubusercontent.com/108309396/226830903-a57c93fa-f13d-4631-acbc-20bd1f8d904d.png)  
![image](https://user-images.githubusercontent.com/108309396/226830939-15081c71-969c-4913-84c6-9183a828030c.png)  

2. 추가 경로에 있는 static file 가져오기    
![image](https://user-images.githubusercontent.com/108309396/226830969-d29490cc-8424-45a9-89be-8586b178469f.png)  
![image](https://user-images.githubusercontent.com/108309396/226831008-8c567e40-c601-4347-a203-e7b3ce93e758.png)  
![image](https://user-images.githubusercontent.com/108309396/226831038-4949ea0b-5cc4-493e-8b8a-ce9af3ff16c0.png)  
![image](https://user-images.githubusercontent.com/108309396/226831071-c11c792c-0007-4f8c-97ff-4c30183e8e80.png)  

### Static_URL 확인하기
![image](https://user-images.githubusercontent.com/108309396/226831281-3c060c3d-d6c3-42cc-b73d-2ea30d3a16d7.png)  
![image](https://user-images.githubusercontent.com/108309396/226831318-ae611e1a-e3f4-41f3-a057-a30798d6a828.png)


# Media File
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- 유저가 업로드한 모든 정적 파일

### `ImageField()`
- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스
- 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용해 최대 길이 변경 가능

### `FileField()`
- `FileField(upload_to='', storage=None, max_length=100, **options)`
- 파일 업로드에 사용하는 모델 필드
- 선택인자 `upload_to, storage`

### FileField/ImageField를 사용하기 위한 단계
1. `settings.py`에 `MEDIA_ROOT`, `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 `MEDIA_ROOT`의 하위 경로를 지정(선택사항)

### Media files 관련 settings
1. `MEDIA_ROOT`  
![image](https://user-images.githubusercontent.com/108309396/226832080-27281b8d-f413-4c45-b527-c17418e22b23.png)
2. `MEDIA_URL`  
![image](https://user-images.githubusercontent.com/108309396/226832110-c7874b17-c79c-4c08-be82-d4a34c1990fe.png)

### 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기
![image](https://user-images.githubusercontent.com/108309396/226832538-ccf82b42-661d-4ce6-80ff-07118155a46c.png)  
- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고 나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL 필요
  - 업로드 된 파일의 URL == `setttings.MEDIA_URL`
  - 위 URL을 통해 참조하는 파일의 실제 위치 == `settings.MEDIA_ROOT`

## Media File 사용하기
### CREATE
![image](https://user-images.githubusercontent.com/108309396/226832845-1fa7191e-bf2f-439c-9204-ac9a1281ded8.png)
- Model field option: `blank`, `null`
- `blank` &rarr; "Validation-related"
  - Default: False
  - True인 경우 필드 비워둘 수 있음 &rarr; 이 경우 DB에는 ''(빈 문자열)이 저장됨
  - 유효성 검사에서 사용됨(is_valid)
    - 필드에 `blank=True`가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음
- `null` &rarr; "Database-related"
  - Default: False
  - True인 경우 DB에는 NULL이 저장
  - CharField, TextField와 같은 문자열 기반 필드에서는 null 옵션 사용 지양
- Migrations: ImageField를 사용하려면 반드시 Pillow 라이브러리 필요 `pip install pillow`
- pillow: 광범위한 파일 형식 지원, 효율적이고 강력한 이미지 처리 기능을 제공하는 라이브러리

### ArticleForm에서 image 필드 출력 확인
![image](https://user-images.githubusercontent.com/108309396/226833987-0137a4d2-ed4a-4c8b-932d-bffaa8a8177b.png)  
- 파일 또는 이미지 업로드 시에는 `form` 태그에 `enctype` 속성을 변경해야 함  
![image](https://user-images.githubusercontent.com/108309396/226834028-999f5a5a-5a15-4e0e-bb67-5add3df06a0b.png)
- 파일 및 이미지는 `request`의 `POST` 속성 값으로 넘어가지 않고 `FILES` 속성값에 담겨 넘어감   
![image](https://user-images.githubusercontent.com/108309396/226834206-8eae21f8-ca1b-492b-ac8d-938ab1b16da5.png)

### 이미지 첨부하기
![image](https://user-images.githubusercontent.com/108309396/226834486-e904b6d5-953f-4bcb-9c4b-70658b21909b.png)  
![image](https://user-images.githubusercontent.com/108309396/226834534-c758a8f9-8376-4e42-8d44-3ffd4d3c9cf8.png)

## READ
### 업로드 이미지 출력하기
![image](https://user-images.githubusercontent.com/108309396/226834678-65684587-6504-46e2-9c76-3533c9c97a4e.png)  
![image](https://user-images.githubusercontent.com/108309396/226834836-59b6b9fa-ce84-443b-aa59-dc901b75be3c.png)  
![image](https://user-images.githubusercontent.com/108309396/226834877-e9724034-47bf-41a8-95ee-60a933730131.png)  

## UPDATE
- enctype 속성값 추가  
![image](https://user-images.githubusercontent.com/108309396/226835082-f1ddd739-484a-48aa-8125-3e327d5f26be.png)
- 이미지 파일이 담겨있는 request.FILES 추가 작성  
![image](https://user-images.githubusercontent.com/108309396/226835308-ad0342f2-fd2e-49a9-add0-33eab7a9db15.png)