# Vue State Management
## State Management
- 상태란? 현재에 대한 정보(data)
- Web application에서의 상태 &rarr; 현재 App이 가지고 있는 data로 표현 가능
- 각 component는 독립적이기 때문에 각각의 상태(data)를 가짐
  - but 하나의 app을 구성해야 하기 때문에 **여러 개의 component가 같은 상태를 유지할 필요**가 있음
  - 상태 관리 필요

## Pass Props & Emit Event
- 같은 데이터를 공유하므로 각 컴포넌트가 동일한 상태를 유지하고 있음
- 데이터의 흐름을 직관적으로 파악 가능
- but component의 중첩이 깊어지면 데이터 전달이 쉽지 않음  
<img width="229" alt="image" src="https://user-images.githubusercontent.com/108309396/236440785-9f511343-a92e-4a4d-b1b9-b8ce8803f762.png">

## Centralized Store
- **중앙 저장소(store)에 데이터를 모아서 상태관리**
- 각 component는 중앙 저장소의 데이터를 사용
- component의 계층에 상관없이 중앙저장소에 접근 및 데이터 변경 가능
- 중앙 저장소의 데이터가 변경되면 component도 실시간 업데이트  
<img width="239" alt="image" src="https://user-images.githubusercontent.com/108309396/236441283-3271d75a-2155-4143-b23f-7caa67e6ba44.png">

## Vuex
- "state management pattern + Library" for vue.js
- 중앙 저장소를 통해 상태관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙 설정
- Vue의 반응성을 효율적으로 사용하는 상태 관리 기능 제공

# Vuex 시작하기
## Project with vuex
<img width="472" alt="image" src="https://user-images.githubusercontent.com/108309396/236447532-696578c0-3515-4d80-9437-d97a01c9f534.png">

- `src/store/index.js`가 생성됨
1. `state`: 중앙에서 관리하는 모든 상태 정보
2. `mutations`: `state`를 변경하기 위한 methods 
3. `actions`: 비동기 작업이 포함될 수 있는(외부API와의 소통) methods, state 변경 외의 모든 비즈니스 로직 수행
4. `getters`: `state`를 활용해 계산한 새로운 변수 값  
<img width="228" alt="image" src="https://user-images.githubusercontent.com/108309396/236447761-723e154c-2b33-4bc1-b8da-51975da42d53.png">

## Vue와 Vuex 인스턴스 비교
<img width="472" alt="image" src="https://user-images.githubusercontent.com/108309396/236447854-67f180fa-29ca-43a5-8c74-98f389efc86a.png">

### 1. `state`
- vue instance의 `data`에 해당
- **중앙에서 관리하는 모든 상태 정보**
- state의 데이터가 변화하면 해당 데이터를 공유하는 component도 자동으로 다시 렌더링
- `$store.state`로 state 데이터에 접근

### 2. `mutations`
- vue instance의 `methods`에 해당
- `mutations`에서 호출되는 핸들러 함수는 반드시 *동기적*이어야 함
  - 비동기 로직으로 state 변경 시, state의 변화 시기를 특정할 수 없기 때문
- **실제로 state를 변경하는 유일한 방법**
- 첫 번째 인자로 `state`를 받으며, component 혹은 actions에서 `commit()` 메서드로 호출됨

### 3. `actions`
- `mutations`와 비슷하지만 *비동기 작업 포함 가능*하다는 차이 존재
- `state`를 직접 변경하지 않고 `commit()`메서드로 `mutations`를 호출해서 `state`를 변경
- context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근 가능
  - 즉 state를 직접 변경할 수 있지만 하지 않아야 함
- component에서 `dispatch()`메서드에 의해 호출

### Mutations & Actions
- Mutations: state를 변경
- Actions: state 변경을 제외한 나머지 로직(비즈니스 로직)
<img width="637" alt="image" src="https://user-images.githubusercontent.com/108309396/236448888-62835b97-633d-48e9-b678-9b575e2db8e3.png">

### 4. `getters`
- vue instance의 `computed`에 해당
- **`state`를 활용하여 계산된 값을 얻고자 할 때 사용**
- `state`의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- `computed`와 마찬가지로 getters의 결과는 캐싱되며 종속된 값이 변경된 경우에마 재계산
- `getters`에서 계산된 값은 `state`에 영향X
- 첫 번째 인자로 `state`, 두 번째 인자로 `getter`를 받음

### 데이터의 흐름
- component에서 데이터를 '조작'하기 위한 데이터의 흐름
  - `component` -`dispatch()`-> `actions` -`commit()`-> `mutations` -> `state`
- component에서 데이터를 '사용'하기 위한 데이터의 흐름
  - `state` -> `getters` -> `component`














# 9시반에 옴 (아마도)