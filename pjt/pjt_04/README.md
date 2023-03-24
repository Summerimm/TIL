# DB를 활용한 웹 페이지 구현
## 목표
- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 사용한 데이터 처리
- Django Model과 ORM에 대한 이해
- Django ModelForm을 활용한 사용자 요청 데이터 유효성 검증
- Django Static files 관리 및 image file 업로드

## Model
- `class Movie(models.Model)`  
![image](https://user-images.githubusercontent.com/108309396/227415961-16e591e3-92f0-420b-b94d-572e38513e77.png)

## URL
- `mypjt`에는 `include('movies.urls')`사용
![image](https://user-images.githubusercontent.com/108309396/227416038-88c9f097-8c36-41c7-b5dc-2ecb6b6f5a03.png)

## View
![image](https://user-images.githubusercontent.com/108309396/227416137-01ce8fa0-bb4f-4c00-953c-f93cc9e8faac.png)

## Admin
- `admin.site.register(Movie)`
- 추가로 `list_display`를 추가하여 admin 사이트에서도 가독성이 좋게 구성했다.

## Form
- ModelForm 사용
- `genre`의 경우 Charfield를 받아서 RadioSelect라는 widget을 사용했다.
- `CHOICES`도 클래스 앞에서 장르를 나누어 선언
- `score`의 경우 widget으로 NumberInput을 사용하고 attr으로 step은 0.5, min은 0, max는 5로 지정
- `release_date`는 DateField를 사용하고 DateInput widget을 사용했다

## Template
- `base.html`
- `index.html`
- `detail.html`
- `create.html`
- `update.html`

## Study point
- Create 함수 설정 시 form의 유효성 검사를 진행 후 movie = form.save()를 하는 부분
- 이 부분을 통해 movie 인스턴스가 생성되고 pk를 받아서 detail로 redirect할 수 있음
- 다양한 widget의 활용 및 작성방식
- static files와 media files 사용 방법
- `update.html`과 `create.html`의 form 태그에 `enctype="multipart/form-data"` 추가
- views.py의 update, create 함수에서 POST 받아오는 부분에 request.FILES 추가