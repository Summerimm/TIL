# M:N (User-User)
- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현

## Profile 구현
1. url 및 view 함수 작성  
![image](https://user-images.githubusercontent.com/108309396/231400207-eb8eb55e-b6ac-4246-aed3-ddee485ecb91.png)
2. profile 템플릿 작성
![image](https://user-images.githubusercontent.com/108309396/231400314-3b481574-7ce3-4f77-908e-c1f346ebeb96.png)
3. profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성  
![image](https://user-images.githubusercontent.com/108309396/231400464-255438a8-5775-414c-8ee4-64b8c44c64a1.png)

## Follow 구현
- 모델 관계 설정: ManyToManyField 작성 및 Migration 작성  
![image](https://user-images.githubusercontent.com/108309396/231400972-3c00f363-a1c9-461c-874a-a18ac4a297aa.png)
- url 및 view 함수 작성  
![image](https://user-images.githubusercontent.com/108309396/231401116-e80a6d26-a9c1-4571-b130-5ce86015f059.png)
- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성  
![image](https://user-images.githubusercontent.com/108309396/231401275-34e647da-b3e2-437a-a5ed-14e898474f44.png)
- 데코레이터 및 is_authenticated 추가   
![image](https://user-images.githubusercontent.com/108309396/231401481-83d4a61c-fdf0-4577-90c0-228361752451.png)


# Fixtures
- Fixtures를 사용해 모델에 초기 데이터 제공하는 방법
- Django 프로젝트의 앱을 처음 설정할 떄 동일하게 준비된 데이터로 데이터베이스를 미리 채우는 것이 필요한 상황이 있음
- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음

## fixtures 생성 및 로드
- 생성(데이터 추출): `dumpdata`
  - 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력함
  - 여러 모델을 하나의 json 파일로 만들 수 있음  
  ![image](https://user-images.githubusercontent.com/108309396/231402424-60f2382c-f6a9-48b5-b2c1-36ed50bb2012.png)
  - `dumpdata`의 출력 결과물은 `loaddata`의 입력으로 사용됨
  - `--indent 4` &rarr; Prettify
  - [참고] 모든 모델을 한 번에 dump하기
  ![image](https://user-images.githubusercontent.com/108309396/231404263-fec1e4b5-afdf-4a3d-af02-ff5a640d5c15.png)
- 로드(데이터 입력): `loaddata`
  - 

## Fixtures 