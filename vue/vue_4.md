# Vue Data Management
## Data in components
- 동적 웹페이지를 만들고 있음 &rarr; 웹페이지에서 다뤄야 할 데이터 등장
  - User data, 게시글 data, 등등...
- 한 페이지 내에서 같은 데이터를 공유해야 함
  - 하지만 페이지들은 component로 구분이 되어있음
  - 완전히 동일한 data를 서로 다른 component에서 보여주려면?
- 필요한 컴포넌트들끼리 데이터를 주고받으면?
  - 데이터의 흐름을 파악하기 힘듦
  - 개발 속도 저하
  - 유지 보수 난이도 증가
- 컴포넌트는 부모-자식 관계를 가지고 있으므로, **부모-자식 관계만 데이터를 주고 받게 하자**
  - 데이터의 흐름을 파악하기 용이
  - 유지 보수하기 쉬워짐

## pass props & emit event
- `pass props`: 부모 &rarr; 자식으로 데이터 흐름
- `emit event`: 자식 &rarr; 부모으로 데이터 흐름

# Pass Props
- 부모 &rarr; 자식으로의 data 전달 방식
- 요소의 속성(property)을 사용하여 데이터 전달
- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- **자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함**
- 정적인 데이터를 전달하는 경우 `static props`라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능 &rarr; `prop-data-name="value"`
  - 속성의 키 값은 kebab-case를 사용
- 전달받은 props를 type과 함께 명시
- 잘못된 타입을 전달하는 경우 브라우저의 콘솔에서 사용자에게 경고
![image](https://user-images.githubusercontent.com/108309396/235822266-fc8e493f-34be-4e27-acc2-8a869c879644.png)  
![image](https://user-images.githubusercontent.com/108309396/235822298-8b02faa3-d708-412d-bd34-dafb02c615ef.png)

### Pass Props convention
- 부모에서 넘겨주는 props: `kebab-case`
- 자식에서 받는 props: `camelCase`
- 부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함

## Dynamic props
- 변수를 props로 전달할 수 있음
- v-bind directive를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨  
![image](https://user-images.githubusercontent.com/108309396/235822524-8e595ab0-e977-4c9c-b3c0-4f3f532d3f30.png)  
![image](https://user-images.githubusercontent.com/108309396/235822542-9f7224bd-b443-4b9f-91b6-b7a65b6e72ab.png)
- `:dynamic-props="dynamicProps"는 앞의 key값이란 이름으로 뒤의 " "안의 데이터(dynamicProps)를 전달하겠다는 뜻
- 즉, `:my-props="dynamicProps"`로 데이터를 넘긴다면 자식 컴포넌트에서 myProps로 데이터를 받아야 함
- v-bind로 묶여있는 " "안의 구문은 js의 구문으로, dynamicProps라는 변수에 대한 data를 전달 가능
![image](https://user-images.githubusercontent.com/108309396/235823121-3fafba82-ed80-4bf3-8950-a6088b9bbc15.png)  
![image](https://user-images.githubusercontent.com/108309396/235823131-ed723537-c0a3-4e4e-8b1b-a543a74aa096.png)

### 숫자를 props로 전달
```javascript
// 1 static props로 string "1"을 전달
<SomeComponent num-props="1"/>

//2 dynamic props로 숫자 1을 전달
<SomeComponent :num-props="1"/>
```


## 컴포넌트의 data 함수
- 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 함  
![image](https://user-images.githubusercontent.com/108309396/235823026-14683446-8cf1-4e47-8d4c-5a7c4457427b.png)

### 단방향 데이터 흐름
- 모든 props는 부모에서 자식으로 단방향 바인딩을 형성
- 부모 속성이 업데이트되면 자식도 최신 값으로 새로고침됨
- 목적: 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지


# Emit Event
- `$emit` 메서드를 통해 부모 컴포넌트에 이벤트를 발생
  - `$emit('event-name')` 형식으로 사용하며 부모 컴포넌트에 event-name이라는 이벤트가 발생했다는 것을 알림
1. 자식 컴포넌트에 버튼을 만들고 클릭 이벤트를 추가 
2. `$emit`을 통해 부모 컴포넌트에게 child-to-parent 이벤트를 트리거
![image](https://user-images.githubusercontent.com/108309396/235824442-eeea490b-015c-40f7-9906-cb293429be4f.png)
3. emit된 이벤트를 상위 컴포넌트에서 청취 후 핸들러 함수 실행
![image](https://user-images.githubusercontent.com/108309396/235824600-647426b1-273b-43ef-9de5-14c01dd77765.png)  

### Emit Event 흐름 정리
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출
2. 호출된 함수에서 `$emit`을 통해 상위 컴포넌트에 이벤트(child-to-parent) 발생
3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출

## emit with data
- 이벤트를 발생(emit)시킬 때 인자로 데이터를 전달 가능
- 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능
![image](https://user-images.githubusercontent.com/108309396/235824791-2dca3077-e7ef-48f7-8eee-ac2391e906ac.png)  
![image](https://user-images.githubusercontent.com/108309396/235824835-c203e457-6a5b-40a3-8f9f-4f9b45061c02.png)
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출
2. 호출된 함수에서 `$emit`을 통해 부모 컴포넌트에 이벤트(child-to-parent)를 발생
   - 이벤트에 데이터(child data)를 함께 전달
3. 부모 컴포넌트는 자식 컴포넌트의 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출, 함수의 인자로 전달된 데이터(child data)가 포함되어 있음
4. 호출된 함수에서 console.log(`~child data~`) 실행

## emit with dynamic data
- 동적인 데이터도 전달 가능
![image](https://user-images.githubusercontent.com/108309396/235825575-6198168f-1c2c-424a-be1d-90531ad57c0e.png)  
![image](https://user-images.githubusercontent.com/108309396/235825634-0f6a17d4-b07f-4876-a156-22b853c1f657.png)
1. 자식 컴포넌트에 있는 keyup.enter 이벤트를 청취하여 연결된 핸들러 함수(ChildInput) 호출
2. 호출된 함수에서 `$emit`을 통해 부모 컴포넌트에 이벤트(child-input)를 발생
   - 이벤트에 v-model로 바인딩 된 입력받은 데이터를 전달
3. 상위 컴포넌트는 자식 컴포넌트의 이벤트(child-input)를 청취하여 연결된 핸들러 함수(getDynamicData) 호출, 함수의 인자로 전달된 데이터가 포함되어 있음
4. 호출된 함수에서 console.log(`~입력받은 데이터~`) 실행


# Lifecycle Hooks
- 각 vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
- 각 단계가 트리거가 되어 특정 로직 수행 가능
![image](https://user-images.githubusercontent.com/108309396/235825864-7386d375-4430-41fe-a8e3-d698c7bd140a.png)  
![image](https://user-images.githubusercontent.com/108309396/235825893-b4c6b025-8e37-45fe-ae77-23ce912595c5.png)

### Lifecycle Hooks 실습
![image](https://user-images.githubusercontent.com/108309396/235826089-4f902717-1929-4627-afae-50277b782a63.png)  
![image](https://user-images.githubusercontent.com/108309396/235826117-982f348c-32cd-4793-9e49-c689b5b035f3.png)  
![image](https://user-images.githubusercontent.com/108309396/235826167-fd7cff5d-f55d-41b5-8806-4cd3a117fbcf.png)

### created
- Vue instance가 생성된 후 호출
- data, computed 등의 설정이 완료된 상태
- 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
- 단, mount되지 않아 요소에 접근 불가능

### mounted
- Vue instance가 요소에 mount된 후 호출
- mount된 요소를 조작 가능
- created()의 경우 mount 되기 전이기 때문에 DOM에 접근할 수 없으므로 동작X

### updated
- 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

### Lifecycle Hooks 특징
- instance마다 각각의 lifecycle을 가지고 있음
- Lifecycle Hooks는 컴포넌트 별로 정의 가능
- 부모 컴포넌트의 mounted hook이 실행되었다고 해서 자식이 mount된 것 아님
  - 즉 부착 여부가 부모-자식 관계와 관계X
- instance마다 각각의 Lifecycle을 가지고 있기 떄문