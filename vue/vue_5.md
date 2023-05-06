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

# Vuex 실습
### Object method shorthand
- 객체 메서드 축약형을 사용할 것
```javascript
// before
const obj1 = {
  addValue: functon(value) {
    return value
  },
}

// after
const obj2 = {
  addValue(value) {
    return value
  }
}
```

## state
- `$store.state`로 접근 가능
- store의 state에 message 데이터 정의  
<img width="229" alt="image" src="https://user-images.githubusercontent.com/108309396/236629025-55839daa-ce1f-4b1b-a31c-10262ad28bb6.png">

- component에 state 사용  
<img width="268" alt="image" src="https://user-images.githubusercontent.com/108309396/236629040-07c478ec-8023-40f4-b488-92e2f6c42c77.png">

- `$store.state`에 바로 접근하기보다 `computed`에 정의 후 접근하는 것을 권장  
<img width="252" alt="image" src="https://user-images.githubusercontent.com/108309396/236629083-68ad2093-b956-465f-8b8a-949a0777fc49.png">

## actions
- `state`를 변경할 수 있는 `mutations` 호출
- component에서 `dispatch()`에 의해 호출됨
- `dispatch(actions-function, payload)` 
  - 호출하고자 하는 actions 함수 & 넘겨주는 데이터(payload)
- actions에 정의된 `changeMessage` 함수에 데이터 전달하기
- component에서 actions는 `dispatch()`에 의해 호출됨  
<img width="469" alt="image" src="https://user-images.githubusercontent.com/108309396/236629268-187ee56d-e5e5-4c0f-8f2c-15495a89d044.png">

### actions의 인자
1. `context`
   - context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
   - `dispatch()`를 사용해 다른 actions도 호출 가능
   - **단, actions에서 state를 직접 조작하지 말 것**
2. `payload`
   - 넘겨준 데이터를 받아서 사용

## `mutations`
- `actions`에서 `commit()`을 통해 mutations 호출
- `commit(mutations-function, payload)`  
<img width="370" alt="image" src="https://user-images.githubusercontent.com/108309396/236629946-2be9909d-0498-4f25-9ec3-1907e00f7cb4.png">

- mutations 함수 작성
- mutations 함수의 첫 번째 인자는 `state`, 두 번째 인자는 `payload`  
<img width="350" alt="image" src="https://user-images.githubusercontent.com/108309396/236630072-9fe29491-e049-4753-a37c-1b74f511215f.png">

## `getters`
- `getters`는 `state`를 활용한 새로운 변수 == `computed`
- getters 함수의 첫 번째 인자는 `state`, 두 번째 인자는 `getters`  
<img width="460" alt="image" src="https://user-images.githubusercontent.com/108309396/236630140-d0c5d198-ab4f-4f18-82ad-76f2ebeb1d33.png">  
<img width="461" alt="image" src="https://user-images.githubusercontent.com/108309396/236630230-4f8ef740-28ec-4c3f-a98d-20d8a544bbec.png">

- `getters`도 `state`와 마찬가지로 `computed`에 정의해서 사용하는 것을 권장  
<img width="353" alt="image" src="https://user-images.githubusercontent.com/108309396/236630869-76f0a606-fae9-4744-ab86-0db062dc932c.png">  
<img width="474" alt="image" src="https://user-images.githubusercontent.com/108309396/236630891-03aeeece-66ca-47f3-b3d7-b943a1167c1e.png">