# UX & UI
## UX(User Experience)
- 유저와 가장 가까이에 있는 분야
- 데이터를 기반으로 유저를 조사하고 분석해 개발자, 디자이너가 이해할 수 있게 소통
- 유저가 느끼는 느낌, 태도, 그리고 행동을 디자인

## 좋은 UX를 설계하기 위해서는
- 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내고 계속 고쳐나가는 것이 중요
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

## UI(User Interface)
- 유저에게 보여지는 화면을 디자인
- UX를 고려한 디자인을 반영
- 기능 개선 혹은 추가가 필요한 경우 Front-end 개발자와 가장 많이 소통

### [참고] Interface
- 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고 받는 경우의 접점
  - 즉, 사용자가 기기를 쉽게 동작시키는 데 도움을 주는 시스템
- CLI(Command-Line Interface), GUI(Graphic User Interface)를 사용해 컴퓨터를 조작

## 좋은 UI를 설계하기 위해서는
- 심미적인 부분만 중요시하기 보다 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하는 부분까지 고려되어야 함
- 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등이 필요


# Vue Router
## Routing
- 네트워크에서 경로를 선택하는 프로세스

## Routing in SSR
- Server가 모든 라우팅을 통제
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공

## Routing in SPA / CSR
- 서버는 하나의 HTML(index.html)만을 제공
- 이후 모든 동작은 하나의 HTML 문서 위에서 JS 코드를 활용
- **하나의 URL만 가질 수 있음**

## Why routing?
- 동작에 따라 URL이 반드시 바뀔 필요는 없지만 유저의 사용성 관점에서는 필요
- Routing이 없다면
  - 유저가 URL을 통한 페이지의 변화 감지 불가능
  - 페이지가 무엇을 렌더링 중인지에 대한 상태 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크를 공유할 시 처음 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
  - SPA의 단점 중 하나이 "URL이 변경되지 않는다."를 해결
- [참고] MPA(Multiple Page Application)
  - 여러 개의 페이지로 구성된 애플리케이션
  - SSR 방식으로 렌더링

## Vue Router 시작하기
![image](https://user-images.githubusercontent.com/108309396/236978894-216038c7-48cd-44c3-8fcf-3cd861b4698c.png)
- history mode 사용 여부 &rarr; Yes

## History mode
- 브라우저의 History API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있음
- [참고] History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨(#을 통해 URL을 구분하는 방식)

## Vue Router 시작하기
- `App.vue`
  - router-link 요소 및 router-view가 추가됨    
  ![image](https://user-images.githubusercontent.com/108309396/236979152-3583e312-3ce1-4ea6-b468-4fd395ff7092.png)
- `router/index.js` 생성
- `views` 폴더 생성  
![image](https://user-images.githubusercontent.com/108309396/236979255-6ab9cadf-5a98-43ca-a5ef-2a424fcccb37.png)

### `router-link`
- a태그와 비슷한 기능 &rarr; URL을 이동시킴
  - routes에 등록된 컴포넌트와 매핑됨
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
- 목표 경로는 `to` 속성으로 지정됨
- 기능에 맞게 HTML에서 a태그로 rendering되지만, 필요에 따라 다른 태그로 변경 가능

### `router-view`
- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- Django에서의 block tag와 비슷함
  - `App.vue`는 base.html
  - `router-view`는 block 태그로 감싼 부분

### `src/router/index.js`
- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py에 해당
- routes에 URL와 컴포넌트를 매핑  
![image](https://user-images.githubusercontent.com/108309396/236979960-30643ecd-8fde-40cd-91b2-0ea6e6c217a2.png)
- Django와의 비교    
![image](https://user-images.githubusercontent.com/108309396/236980044-cb913a01-0c3f-41c8-a775-9125ed47db7c.png)

### `src/Views`
- `router-view`에 들어갈 component 작성
- 기존에 component를 작성던 곳은 components 폴더뿐이었지만 이제 두 폴더로 나뉘어짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
- 폴더 별 컴포넌트 배치
  - `views/`
    - routes에 매핑되는 컴포넌트, 즉 `router-view`의 위치에 렌더링되는 컴포넌트를 모아두는 폴더
    - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
    - ex) AboutView, HomeView 컴포넌트
  - `components`
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
    - ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

# Vue Router 실습
## 주소를 이동하는 2가지 방법
1. 선언적 방식 네비게이션
- router-link의 `to` 속성으로 주소 전달
- routes에 등록된 주소와 매핑된 컴포넌트로 이동  
![image](https://user-images.githubusercontent.com/108309396/236980540-af27b8fb-ea28-4d1f-b99c-8af8e01393e6.png)
- Named Routes(Django에서의 path 함수의 name 인자 활용과 같은 방식)    
![image](https://user-images.githubusercontent.com/108309396/236980634-580fb689-7419-4ae7-b639-e16082d5918f.png)
- 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동  
![image](https://user-images.githubusercontent.com/108309396/236980714-7e2acca9-b419-436c-a4f8-09ca22d5269f.png)

2. 프로그래밍 방식 네비게이션
- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 가능
- 다른 URL로 이동하려면 `this.$router.push`를 사용
  - history stack에 이동할 URL을 넣는(push) 방식
  - history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동 가능
- 결국 `<route-link :to="...">`를 클릭하는 것과 `$router.push(...)`를 호출하는 것은 같은 동작
- 동작 원리는 선언적 방식과 같음    
![image](https://user-images.githubusercontent.com/108309396/236981143-00f01066-9ffb-43cc-9dbe-b448608240a0.png)

### Dynamic Route Matching
- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용 가능(Django에서의 variable routing)
- `HelloView.vue` 작성 및 route 추가
- route를 추가할 때 동적 인자를 명시
![image](https://user-images.githubusercontent.com/108309396/236981305-d5bd5dfd-6b62-447f-bc02-8e347818ff18.png)  
![image](https://user-images.githubusercontent.com/108309396/236981342-25e20337-4e74-40c1-8073-e224544ef066.png)
- `$route.params`로 변수에 접근 가능
- but HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장  
![image](https://user-images.githubusercontent.com/108309396/236981473-edbcd4ac-0cb3-4d48-98f9-b93eac4f3ddc.png)
- 선언적 방식 네비게이션
  - params를 이용하여 동적 인자 전달 가능  
  ![image](https://user-images.githubusercontent.com/108309396/236981592-ff9c70d2-e529-46dd-8831-0ae7d20bdd8c.png)
- 프로그래밍 방식 네비게이션
![image](https://user-images.githubusercontent.com/108309396/236981658-f48ea927-8b0e-4516-b197-dac7819590ad.png)

## router에 컴포넌트를 등록하는 또다른 방법
- `router/index.js`에 `about`추가    
![image](https://user-images.githubusercontent.com/108309396/236981805-2e38b229-d540-475b-ac72-8a56d868767d.png)

### `lazy-loading`
- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식 활용
  - 최초 로드 시간이 빨라짐
  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심