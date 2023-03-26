1.   static 파일 기본 설정  
개발자가 작성한 CSS 파일이나 미리 업로드한 이미지 파일 등을 Django 프로젝트 폴더 (my_pjt) 내부 assets 폴더에 저장해두었다. 이처럼 기존 static 파일 경로 외에 추가 경로를 정의해야 할 경우 settings.py 에 추가해야 하는 설정과 값을 작성하시오
```python
# settings.py

STATICFILES_DIRS = [
    BASE_DIR / 'my_pjt' / 'assets'
]

STATIC_URL = '/static/
```

2.   media 파일 기본 설정   
사용자가 업로드 파일의 저장 위치를 Django 프로젝트 폴더(my_pjt) 내부 uploaded_files 폴더로 지정하고자 한다 . 이 때 settings.py 에 작성해야 하는 설정과 값을 모두 작성하시오

```python
# settings.py

MEDIA_ROOT = BASE_DIR / 'my_pjt' / 'uploaded_files'

MEDIA_URL = '/media/'
```
