# Vue with DRF
## 컴포넌트 구조 확인
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/6caa2be5-0a92-45c4-b62e-e44533ce4eef)

## 메인 페이지 구성
- `views/ArticleView.vue` component 확인 및 route 등록  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/fa32e59e-270e-4b24-a97a-b41b529b7dc4)
- `src/App.vue` router-link  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/2a49c2e4-f6b2-45b4-8bd6-442c0a1d6e1b)  
- `components/ArticleList.vue` 확인
  - 전체 게시물을 표현할 컴포넌트  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/8f21573c-db97-4d1d-99ac-852a605a572b)
- `views/ArticleView.vue` 
  - `ArticleList` 하위 컴포넌트 등록(불러오기, 등록하기, 보여주기)  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/114adf39-9ef7-40a2-b5ab-370c707516a2)
- `components/ArticleListItem.vue` 확인
  - 각 게시글들의 정보를 표현할 컴포넌트  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/b10da01f-378d-486b-af01-41793fa7325c)
- `components/ArticleList.vue` 
  - `ArticleListItem` 하위 컴포넌트 등록    
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/f30a9a2b-d4ba-4786-8566-0ad8f219c4df)
- `store/index.js`
  - state에 articles 배열 정의
  - 화면 표현 체크용 더미 데이터 생성  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/0cb417dc-f955-45f9-909a-449c0654cbaa)
- `components/ArticleList.vue` 코드 수정
  - state에서 articles 데이터 가져오기
  - `v-for` 디렉티브를 활용하여 하위 컴포넌트에서 사용할 article 단일 객체 정보를 pass props  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/01ec2601-15c1-41e5-9ae2-1274a49e6434)  
- `components/ArticleListItem.vue` 수정
  - 내려받은 props 데이터로 화면 구성
  - prop 데이터의 타입 표기    
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/df1f420f-f914-44de-80cf-11860baa4d9b)

## AJAX 요청 준비
- `axios` 설정: `npm install axios`
- `store/index.js`에서 불러오기: 요청 보낼 API server 도메인 변수에 담기  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/98ce1175-f8a6-46e2-aa79-acf8414d4e82)
- `store/index.js`에서 `getArticles` 메서드 정의  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/3a81c21f-2c2f-4a52-b4ac-6765b8e2d73d)
- `views/ArticleView.vue`에서 `getArticles` actions 호출
  - 인스턴스가 생성된 직후 요청을 보내기 위해 `created()` hook 사용  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/c04bed9b-a25a-42eb-acae-ac5d40586fba)\


# CORS(Cross-Origin Resource Sharing)
- 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착
- 서버는 200(정상) 반환 &rarr; 서버는 정상적으로 응답 but 브라우저가 막음
- 보안 상의 이유로 브라우저는 **동일 출처 정책(SOP, Same Origin Policy)**에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한

## SOP
- 동일 출처 정책
- 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임

### Origin - 출처
- URL의 Protocol, Host, Port를 모두 포함하여 출처라고 부름
- 아래 세 영역이 일치하는 경우에만 same origin  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/271938e7-ca95-4617-9ba6-818d28e23262)

## CORS - 교차 출처 리소스 공유
- 추가 *HTTP Header*를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
  - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 **서버에 지정**할 수 있는 방법
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
- 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알리는 것

## set CORS
- CORS 표준에 의해 추가된 HTTP Response Header를 통해 통제 가능
- ex) Access-Control-Allow-Origin: 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용

### django-cors-headers library 사용
- 응답에 CORS header를 추가해주는 라이브러리
- 라이브러리 설치 및 `requirements.txt` 업데이트
- `pip install django-cors-headers`, `pip freeze > requirements.txt`
- APP 추가 및 MIDDLEWARE 설정: CorsMiddleware는 가능한 CommonMiddleware보다 먼저 정의  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/f9371939-a86a-47d8-94f4-8d19ae2f2198)
- `CORS_ALLOWED_ORIGINS`에 Domain 등록  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/02eb26b9-86d0-4989-bc3a-3bd2ad23a72f) 
- 만약 모든 Origin을 허용하고자 한다면
```python
# my_api/settings.py

# 모든 Origin 허용
CORS_ALLOW_ALL_ORIGINS = True
```

## Article Read
- `store/index.js` 수정
  - 기존 articles 데이터 삭제
  - Mutations 정의(응답 받아온 데이터를 state에 저장)    
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/0d3e33f3-99f6-483d-9bd3-6a46f8974a82)

## Article Create
- `views/CreateView.vue`
  - `v-model.trim`을 활용해 공백 제거
  - `.prevent`를 활용해 form의 기본 이벤트 동작 막기  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/974e1dd7-b54f-464c-aff3-3aa35a0e48bb)  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/a438c363-1358-434b-9668-26f7ca7255ad)
  - state를 변화시키는 것이 아닌 DB에 게시글 생성 후, ArticleView로 이동할 것이므로 methods에서 직접 처리  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/673a5b55-8284-49a4-ba4b-a0477091902e)

## Article Create
- `router/index.js`  
![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/b5979c82-2a86-44a4-afb4-d42764f5801b)
- `views/ArticleView.vue`
  - router-link를 통해 CreateView로 이동  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/87769c07-e05f-489c-bddc-cfc736d55762)
- `views/CreateView.vue` 코드 수정
  - `createArticle` method 수정  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/cfadd970-e280-4942-b817-592c9dc727eb)

## Article Detail
- `views/DetailView.vue` 
  - 게시글 상세 정보를 표현할 컴포넌트
  - AJAX 요청으로 응답 받아올 article의 상세 정보들을 표현  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/4cf516a2-e72a-4278-b28d-e17b3b925808)
- `router/index.js`
  - id를 동적 인자로 입력 받아 특정 게시글에 대한 요청 처리  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/3ea315e7-bf85-425d-8c55-3e834bc6e2c4)
- `components/ArticleListItem.vue` 
  - router-link를 통해 특정 게시글의 id값을 동적 인자로 전달  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/a883a057-8458-447c-b2d7-49f17f942674)
- `views/DetailView.vue`
  - `this.$route.params`를 활용해 컴포넌트가 create될 때, 넘겨받은 id로 상세 정보 AJAX 요청  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/f9c8e643-2d4e-45cb-a47f-9a39955a2669)  
- `views/DetailView.vue` 수정
  - 응답 받은 정보를 data에 저장
  - data에 담기까지 시간이 걸리므로 optional chaining을 활용해 데이터 표기  
  ![image](https://github.com/Al9-Mor9/Selected-Problems/assets/108309396/8e511be0-decd-4dbd-86a2-97ec43708d39)