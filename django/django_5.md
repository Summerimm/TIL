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
1. `as_p()`: 각 필드가 단락(<p>태그)으로 감싸져서 렌더링
2. `as_ul()`: 각 필드가 목록 항목(<li>태그)으로 감싸져서 렌더링 &rarr; <ul> 태그는 직접 작성해야함
3. `as_table()`: 각 필드가 테이블(<tr>태그)으로 감싸져서 렌더링

## Django의 2가지 HTML input 요소 표현
1. Form fields
  - 입력에 대한 유효성 검사 로직 처리
  - 템플릿에서 직접 사용  
![image](https://user-images.githubusercontent.com/108309396/226526341-40ee92ec-7d9e-4ee8-a175-6244e0bce5b3.png)
2. Widgets
  - 웹 페이지의 HTML input element 렌더링을 담당: 단순히 input 요소의 보여지는 부분을 변경
  - 유효성 검증과 아무런 관계가 없음
  - Widgets은 반드시 form fields에 할당됨  
![image](https://user-images.githubusercontent.com/108309396/226526364-9a21c0df-4cba-4a64-8c99-6cb72d2be789.png)

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
![image](https://user-images.githubusercontent.com/108309396/226529523-253b26b6-f9bf-4fbc-9234-1f26b3bd0abc.png)

### "is_valid()" method
- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

### "save()" method
- form 인스턴스에 바인딩된 데이터를 통해 DB 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 `instance` 여부를 통해 생성할지, 수정할지를 결정함
  - instance 없는 경우 save()는 지정된 모델의 새 인스턴스 생성(CREATE)
  - instance 제공되면 save()는 해당 인스턴스를 수정(UPDATE)  
![image](https://user-images.githubusercontent.com/108309396/226532368-efe794c0-afbb-4e1b-b452-d8a925f5b681.png)

## UPDATE
- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
1. request.POST: 사용자가 form을 통해 전송한 데이터(새로운 데이터)
2. instance: 수정이 되는 대상

### update view / template 수정  
![image](https://user-images.githubusercontent.com/108309396/226533077-cbd8ffc1-0de6-4b5b-beff-9dedd7f7bbfb.png)  
![image](https://user-images.githubusercontent.com/108309396/226533119-816cdd81-d115-41c9-8274-5307a0447587.png)

## Form과 ModelForm 비교
- 각자 역할이 다름
1. Form
   - 사용자의 입력을 필요로 하고 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때
2. ModelForm
   - 사용자의 입력을 필요로 하고 입력을 받은 것을 그대로 DB 필드에 맞춰 저장할 때
   - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save() 호출이 가능

### Widgets을 작성하는 2가지 방법  
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








### Media File
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- 유저가 업로드한 모든 정적 파일