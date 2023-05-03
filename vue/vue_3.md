# Vue CLI
## Node.js
- JavaScript는 브라우저를 조작하는 유일한 언어
  - But 브라우저 밖에서는 구동X
- Node.js: 자바스크립트를 구동하기 위한 런타임 환경
  - 브라우저가 아닌 환경에서도 구동O
  - Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행 가능
  - Server-Side-Programming도 가능

## NPM(Node Package Manage)
- 자바스크립트 패키지 관리자
- 다양한 의존성 패키지 관리
- Node.js의 기본 패키지 관리자

## Vue CLI
- Vue 개발을 위한 표준 도구
- 프로젝트의 구성을 도와줌
- 확장 플러그인, GUI, Babel 등 tool 제공
- 설치: `npm install -g @vue/cli`
- 프로젝트 생성: `vue create vue-cli`
- Vue 2 선택 후 프로젝트 디렉토리로 이동(`cd vue-cli`)
- 프로젝트 실행: `npm run serve`

## Vue CLI 프로젝트 구조
![image](https://user-images.githubusercontent.com/108309396/235568336-66e9475d-8321-4455-bd32-d338bcf3ff63.png)
1. `node_modules`
   - node.js 환경의 여러 의존성 모듈
   - venv와 비슷한 역할
   - 따라서 .gitignore에 넣어주어야 함
   - **Babel**: JavaScript compiler
     - 자바스크립트의 ES6+ 코드를 구버전으로 변환해주는 도구
   - `Webpack`: static module bundler
     - 모듈 간의 의존성 문제를 해결하기 위한 도구
     - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프 빌드
   - `Module`: js 파일 하나가 하나의 모듈
     - 모듈은 대개 기능 단위로 분리
     - 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성
   - `Bundler`: 모듈 의존성 문제를 해결해주는 도구
     - `Webpack`은 다양한 Bundler 중 하나
     - 모듈들을 하나로 묶어주고 묶인 파일은 하나로 만들어짐
     - Bundling된 결과물은 개별 모듈의 실행 순서에 영향받지 않고 동작
2. `package.json`
   - 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션 포함
3. `package-lock.json`
   - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
   - 협업 및 배포환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
   - 사용할 패키지의 버전 고정
   - 개발 과정 간의 의존성 패키지 충돌 방지
   - python의 requirements.txt 역할
4. `public/index.html`
   - Vue 앱의 뼈대가 되는 html 파일 (base.html)
   - Vue 앱과 연결될 요소가 있음
5. `src/`
   - `src/assets`: 정적 파일을 저장
   - `src/components`: 하위 컴포넌트들이 위치
   - `src/App.vue`: 최상위 컴포넌트, `public/index.html`과 연결
   - `src/main.js`: webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
     - `public/index.html`과 `src/App.vue`를 연결시키는 작업이 이루어지는 곳
     - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일


# Component
- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 기능별로 분화한 코드 조각
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적
  - Vue에서는 `src/App.vue`를 root node로 하는 tree 구조
- 유지보수, 재사용 쉬워짐

## Component based architecture
- 관리가 용이
  - 유지/보수 비용 감소
- 재사용성
- 확장 가능
- 캡슐화
- 독립적

# SFC(Single File Component)
- Vue에서의 component &rarr; 이름이 있는 재사용 가능한 Vue instance(new Vue()로 만든 인스턴스)
- 하나의 `.vue`파일이 하나의 Vue instance이고, 하나의 컴포넌트
- Vue instance에서는 HTML, CSS, JavaScript 코드를 한 번에 관리 &rarr; 기능 단위로

## Vue Component 구조
- 템플릿(HTML)
  - 다른 컴포넌트를 HTML 요소처럼 추가 가능
- 스크립트(JavaScript)
  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
- 스타일(CSS)
  - CSS가 작성되며 컴포넌트의 스타일을 담당  
  ![image](https://user-images.githubusercontent.com/108309396/235570095-bad482f3-6997-41d3-a5a8-a3147ea07426.png)


## MyComponent.vue
![image](https://user-images.githubusercontent.com/108309396/235570489-e7350dca-6fbb-4687-929a-3c0884cf20d1.png)
1. `src/components/` 안에 생성
2. script에 이름 등록
3. template에 요소 추가
   - templates 안에는 반드시 **하나의 요소만** 추가 가능

## Component 등록 3단계
![image](https://user-images.githubusercontent.com/108309396/235570738-91d9462d-7c10-4bf3-a040-34534dda0cde.png)
1. 불러오기
   - `import {instance name} from {위치}`
   - `@`는 src의 shortcut
   - `.vue` 생략 가능
2. 등록하기
3. 보여주기