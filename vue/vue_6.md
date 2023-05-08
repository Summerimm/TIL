# Vuex Advanced
- Vuex로 관리 중인 상태(data)를 로컬에 저장하기(관련 plugin 알아보기)
- Vuex Helper method 알아보기

# `Window.localStorage`
- 브라우저의 내장 객체 중 하나
- Key-Value 형태로 데이터를 저장할 수 있는 저장소
- localStorage에 저장된 데이터는 브라우저를 종료해도 계속해서 유지됨
  - 다른 탭에서도 동일한 데이터를 공유할 수 있음
  - but 다른 도메인에서는 접근 불가능
  - 보안과 관련된 중요한 정보를 저장하기엔 적합X

## `localStorage.setItem(key, value)`
- key, value 형태로 저장
- 데이터 저장 시 기본적으로 문자열로 저장됨  
![image](https://user-images.githubusercontent.com/108309396/236718285-7795bd63-9b0d-48d9-bbf8-a8e2f9143c61.png)

## `localStorage.getItem(key, value)`
- key 값으로 저장된 데이터 불러오기
- 데이터를 불러올 때도 문자열로 불러옴
![image](https://user-images.githubusercontent.com/108309396/236718457-56a9fbcd-c2cf-4f84-8e7a-f5059b305823.png)

## `JSON.stringify`
- JSON 객체의 메서드
- 자바스크립트 객체를 JSON 형식의 문자열로 변환하여 반환  
![image](https://user-images.githubusercontent.com/108309396/236718575-d7a0936f-0ffb-4f34-a6a3-9d47dff19ca0.png)

## `JSON.parse`
- JSON 형식의 문자열을 자바스크립트 객체로 변환하여 반환  
![image](https://user-images.githubusercontent.com/108309396/236718688-6f613ccd-187c-494e-9c86-ab7d325ac1f4.png)

### Vuex에 적용
![image](https://user-images.githubusercontent.com/108309396/236720148-48c14e80-abd0-4bb7-83ca-475cd7272463.png)  
![image](https://user-images.githubusercontent.com/108309396/236720186-b44ba82c-9b42-43e1-9e4d-fb9a532acf8b.png)

## plugins
- Vuex store에 추가적인 기능을 제공하는 확장 기능
- 일반적으로 state의 변화를 감지해, 어플리케이션의 성능 최적화를 목적으로 함
- `vuex-persistedstate`
  - Vuex store의 상태를 브라우저 local stoarage에 저장해주는 plugin
  - 이전 상태를 유지할 수 있도록 함
  - `vuex` key에 state의 message가 가진 값들이 value로 할당됨
![image](https://user-images.githubusercontent.com/108309396/236720415-8fcbccec-df47-426f-8fb9-9eb4fbf48629.png)
- 추가 옵션을 사용하여 필요에 따라 저장 방식 변경 가능  
![image](https://user-images.githubusercontent.com/108309396/236720601-f3f4280c-20e2-4c1c-b082-23a60eead6f0.png)

# Vuex Binding Helper
- Vuex store의 state, mutations, actions 등을 간단하게 사용할 수 있도록 만들어진 helper function
- import 필요  
![image](https://user-images.githubusercontent.com/108309396/236720786-ceaeab62-03b3-4b72-8ee5-18bd3569acd8.png)

## `mapState`
- Vuex store의 상태를 컴포넌트의 데이터에 매핑할 때 사용
- 이름 바꿀 땐 객체, 그대로 쓸 땐 배열
1. mapState를 import
2. Spread operator를 사용하여 mapState를 전개  
3. 객체 형태
   - 화살표 함수를 사용하여 mapState 내부에 불러오고자 하는 값을 정의
   - key-value 형태로 할당
   - key 값 변경 가능  
![image](https://user-images.githubusercontent.com/108309396/236727359-46e6d0a2-4f16-41e7-b38f-335ffcfed519.png)
3. 배열 형태
   - vuex store의 상태 중, 불러오고자 하는 대상을 배열의 원소로 정의  
  ![image](https://user-images.githubusercontent.com/108309396/236729558-c02929ab-768e-4f78-966d-5da9a9a975ee.png)

## `mapActions`
- 컴포넌트에서 `this.$store.dispatch()`를 호출하는 대신 액션 메서드를 직접 호출하여 사용할 수 있음
1. 배열 형태로 매핑
   - changeMessage에 넘겨주어야 할 inputData를 changeMessage 호출 시 인자로 직접 값을 넘겨주어야 함
  ![image](https://user-images.githubusercontent.com/108309396/236729819-354b8087-b2cc-44e9-8f9c-849c768e09ab.png)
2. 객체 형태로 매핑
  - Actions의 changeMessage를 actionscChangeMessage에 매핑
  - this.actionsChangeMessage 형식으로 사용
  - payload를 넘겨주거나 추가적인 로직 작성 가능  
  ![image](https://user-images.githubusercontent.com/108309396/236730226-68ad02b4-2f6c-4fea-95dc-46dcee26d83e.png)
3. mapGetters
![image](https://user-images.githubusercontent.com/108309396/236730271-bee1288b-7614-4078-9444-44816a29cf66.png)  
- 상황에 따라서는 배열과 객체 형태로 각각 매핑하여 사용 가능
![image](https://user-images.githubusercontent.com/108309396/236730423-4e3b750e-c7f4-4453-bcde-3ce3d3583ad7.png)


# Modules
- Vuex store를 여러 파일로 나눠서 관리할 수 있게 해주는 기능
- Vuex store와 동일한 구성을 가진 별도의 객체를 정의하여 modules 옵션에 작성한 객체를 추가하여 사용
- 별개의 .js 파일에 정의하고 import 하는 방식으로도 사용 가능
- Store의 가독성 향상 가능
