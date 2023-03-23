# 데일리 과제 3-2에서 작성한 모델 Article 모델을 참고하여 작성하시오.
# 1. 홈워크_django_03_hw02_P를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 두 개의 핵심 명령어를 작성 하시오.
python manage.py makemigrations
python manage.py migrate

# 2. shell_plus를 이용하여 레코드를 생성합니다. 'title'과 	'content'의 내용은 자유롭게 작성합니다.
python manage.py shell_plus
Article.objects.create(title='First', content='Django')