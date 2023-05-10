# Navigation Guard
- Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 해당 URL로의 접근을 막는 방법
- ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

## 네비게이션 가드의 종류
1. 전역 가드: 애플리케이션 전역에서 동작
2. 라우터 가드: 특정 URL에서만 동작
3. 컴포넌트 가드: 라우터 컴포넌트 안에 정의

## 전역 가드(Global Before Guard)
- 다른 URL 주소로 이동할 때 "항상" 실행
- `router/index.js`에 `router.beforeEach()`를 사용하여 설정
- 콜백 함수의 값으로 3개의 인자를 받음
  - `to`: 이동할 URL 정보가 담긴 Route 객체
  - `from`: 현재 URL 정보가 담긴 Route 객체
  - `next`: 지정한 URL로 이동하기 위해 호출하는 함수
    - 콜백 함수 내부에서 반드시 "한 번만" 호출되어야 함
    - 기본적으로 `to`에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 `router.beforeEach()`가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 `next()`를 호출해줘야 함
  - `next()`가 호출되기 전까지 화면 전환X

### Login 여부에 따른 라우팅 처리
- Login이 되어 있지 않다면 Login 페이지로 이동하는 기능 추가  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/5e3f3b2a-8711-43c2-8f39-3e56cd765376)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/fe8651eb-5f5a-4379-a30a-63add8d8c191)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/8800a031-fb2f-4a95-9e73-dddf17ab3b4f)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/f9056777-82aa-4095-8101-57d71d5f3496)  
- 반대로 Login하지 않아도 되는 페이지들을 모아 둘 수도 있음  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/238a5bc9-fb8c-4bb9-82a6-efd2f8d8a1cb)

## 라우터 가드
- 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
  - route에 진입했을 때 실행
  - 라우터를 등록한 위치에 추가
  - 단, 매개변수, 쿼리, 해시 값이 변경될 때는 실행X
  - 다른 경로에서 탐색할 때만 실행됨
  - 콜백함수는 `to, from, next`를 인자로 받음

### Login 여부에 따른 라우팅 처리
- 이미 로그인 되어 있는 경우 HomeView로 이동하기  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/61c5529e-b7cc-42db-a5db-c5ce24e0e202)  
- `/login`으로 접속 시도 시 Home으로 이동
- Login을 제외한 다른 페이지로 이동하면 라우터 가드가 동작X
- `isLoggedIn = false`로 변경 시 Login 페이지로 정상 이동 가능

## 컴포넌트 가드
- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
  - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
- URL은 변하지만 페이지는 변화하지 않는 이유
  - 컴포넌트가 재사용됨
  - 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
    - 단, lifecycle hook이 호출X
    - 따라서 `$route.params`에 이쓴ㄴ 데이터를 새로 가져오지 않음
- Params 변화 감지
  - `beforeRouteUpdate()`를 사용
  - userName을 이동할 params에 있는 userName으로 재할당
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/6c520a1a-3623-45a7-91d2-939bbdbe142c) 

## 404 Not Found
- 사용자가 요청한 리소스가 존재하지 않을 때 응답  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/c97c219c-79a1-424e-837e-f94ef5fc9b25)
- 기존에 명시한 경로가 아닌 모든 경로에 대해서 404 page로 redirect 시키기
  - **routes에 최하단부에 작성**   
  ![image](https://github.com/Haaarimmm/TIL/assets/108309396/e1f1f601-df0e-4afa-8941-19c191f413df)

### Dog API를 사용한 404 예시
형식은 유효하지만 특정 리소스를 찾을 수 없는 경우
- 데이터가 없음을 명시하고 404 page로 이동해야 함
![image](https://github.com/Haaarimmm/TIL/assets/108309396/6f99c42b-e5ec-417e-9ae1-4f8e22c77769)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/1e91faca-1128-4464-b482-3e5ec3088dfe)  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/b444c332-1953-4a75-87f0-f1eee07f8f79)
- axios 요청이 오는 중 동작하고 있음을 표현하기 위한 로딩 메시지 정의  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/c12e519b-3280-4877-8d52-9545d35b7b6e)
![image](https://github.com/Haaarimmm/TIL/assets/108309396/e0f1f0be-daa6-4771-bcd4-929c8dee761b)
- axios 요청이 실패할 경우 자료가 없음을 표현하기  
![image](https://github.com/Haaarimmm/TIL/assets/108309396/e0659245-5d84-4fae-95ee-21c4c959a22d)
- axios 요청이 실패할 경우 404로 이동시킬 수도 있음   
![image](https://github.com/Haaarimmm/TIL/assets/108309396/eb36a7c7-92fb-4d03-a451-2296661943dc)