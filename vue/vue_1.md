# Vue Intro
## Front-end Development
- Front-end 개발은 Web App 또는 Web Site의 UI/UX를 제작하고 관리하는 과정
- Front-end 프레임워크와 라이브러리(React, Angular, Vue.js)를 사용하여 개발 효율성을 높이고, Web App의 복잡성을 관리
- Front-end 개발에 사용되는 주요 기술은 HTML, CSS, JavaScript

### Web App이란?
- 개발자 도구 > 디바이스 모드
- 웹 페이지가 그대로 보이는 것이 아닌 **디바이스에 설치된 App**처럼 보이는 것
- 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

### SPA(Single Page Application) &larr;&rarr; MPA
- SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
- CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문

> [참고] SSR(Server Side Rendering)이란?
> - Sever가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
> - 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

> [참고] CSR(Client Side Rendering)이란?
> - 최초 한 장의 HTML을 받아오는 것은 동일
>   - 단, server로부터 최초로 받아오는 문서는 빈 html 문서
> - 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
> 1. 필요한 페이지를 서버에 `AJAX`로 요청
> 2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
> 3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)

### 왜 CSR 방식을 사용하는 걸까?
1. 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨
   - 클라이언트: 트래픽 감소
   - 트래픽이 감소한다 = 응답 속도가 빨라진다
2. 필요한 부분만 고쳐나가므로 각 요청이 끊김없이 진행 - UX 향상
3. BE와 FE의 작업 영역을 명확히 분리 가능 - 협업 용이

### CSR은 만능일까?
- 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간 소요
- 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움
- 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
- SPA 서비스에서도 SSR을 지원하는 Framework이 발전하고 있음
  - Vue의 Nuxt.js, React의 Next.js...

### CSR과 SSR의 장단점
1. CSR
   - 최초 렌더링
   - UX
   - 서버 cost가 좋음
2. SSR
   - 최종 렌더링
   - 유저 환경에 영향 적게 받음

## Vue로 코드 작성하기
1. Vue CDN 가져오기
2. Vue instance 생성
3. `el, data` 설정
   - `data`에 관리할 속성 정의
4. 선언적 렌더링 `{{ }}`
   - Vue data를 화면에 렌더링  
  ![image](https://user-images.githubusercontent.com/108309396/234774598-0a23cf7f-de44-43cf-8862-403adb517855.png)
1. input tag에 `v-model` 작성
   - input에 값 입력 &rarr; Vue data 반영
   - Vue data &rarr; DOM 반영  
  ![image](https://user-images.githubusercontent.com/108309396/234774808-36e6f5c0-e12a-4e0c-8f7d-89dfe3d1ca98.png)


## MVVM Pattern
- 소프트웨어 아키텍처 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(`view`)의 개발을 Back-end(`model`)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
![image](https://user-images.githubusercontent.com/108309396/234776072-1f551f5a-9ace-49ee-bcb4-797b92bc346b.png)
- `View` - 우리 눈에 보이는 부분 = DOM
- `Model` - 실제 데이터 = JSON
- `View Model`(Vue)
  - View를 위한 Model
  - View와 binding되어 Action을 주고 받음
  - Model이 변경되면 View Model도 변경되고 바인딩 된 View도 변경됨
  - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
  - View는 Model을 모르고, Model도 View를 모른다


## Vue instance
1. Vue CDN 가져오기
2. `new` 연산자를 사용한 생성자 함수 호출
   - Vue instance 생성  
![image](https://user-images.githubusercontent.com/108309396/234776588-bcfb83df-e389-4662-a38f-5f9628afd583.png)
- 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것

## `el` (element)
- Vue instance와 DOM을 Mount하는 옵션
  - View와 Model을 연결하는 역할
  - HTML id 혹은 class와 마운트 가능
- Vue instance와 **연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음**
  - Vue 속성 및 메서드 사용 불가  
![image](https://user-images.githubusercontent.com/108309396/234785326-f0c750bf-522e-46f7-945e-bd5b23c4cb7d.png)
- Vue와 연결되지 않은 채 {{ message }} 선언 시 그대로 출력됨

## `data`
- Vue instance의 **데이터 객체** 혹은 **인스턴스 속성**
- 데이터 객체는 반드시 기본 객체 `{}`(Object)여야 함
- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 `interpolation {{}}`을 통해 view에 렌더링 가능  
![image](https://user-images.githubusercontent.com/108309396/234785759-31d24c07-52a4-46b5-b0c2-f9a5575f6740.png)
- 추가된 객체의 각 값들은 `this.message` 형태로 접근 가능

## `methods`
- Vue instance의 `method`들을 정의하는 곳
- 콘솔창에서 `app.print()` 형식으로 실행 가능  
![image](https://user-images.githubusercontent.com/108309396/234785926-82bce6fd-4ffa-4256-9a0e-79e2f7058f8a.png)
![image](https://user-images.githubusercontent.com/108309396/234786023-b26a1f35-4a67-4e89-96ba-bf8288e1bc6f.png)
- arrow function은 사용X &rarr; arrow function의 `this`는 함수가 선언될 때 상위 스코프(window)를 가리킴
