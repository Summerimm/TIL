# Event
- **Event**란 HTML 요소에서 발생하는 모든 상황을 의미
- 클릭 말고도 웹에서는 각양각색의 Event가 존재
  - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

## Event object
- Event가 발생했을 때 생성되는 객체
- Event 발생: 사용자 행동 / 특정 메서드 호출을 통해 프로그래밍적으로 만들 수 있음
- DOM 요소는 Event를 "수신"하고 받은 event를 "처리"할 수 있음
  - Event 처리는 주로 `addEventListener()` 메서드를 통해 Event handler를 다양한 html요소에 "부착"해서 처리

## Event handler
### `addEventListner()`
- **대상**에 **특정 Event**, **할 일**을 등록하자
- `EventTarget.addEventListner(type, handler function[, options])`
- 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
- Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상(EventTarget)으로 지정 가능
- `type`: 반응할 Event 유형을 나타내는 대소문자 구분 문자열
  - `input, click, submit...`
- `handler function`: 지정된 타입의 Event를 수신할 객체
  - JavaScript function 객체(콜백 함수)여야 함
  - 콜백 함수는 발생한 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음

## Event 전파
- DOM 요소에서 발생한 이벤트가 상위 노드에서 하위 노드 혹은, 하위 노드에서 상위 노드로 전파되는 현상을 의미
- `addEventListener` 메서드를 사용하여 전파 방식 제어 가능
- 기본값은 하위 노드에서 상위 노드로 전파되는 방식을 사용 - Event Bubbling

### `event.preventDefault()`
- 현재 Event의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음
- HTML 요소의 기본 동작 예시) a 태그-클릭 시 특정 주소로 이동, form 태그: form 데이터 전송


### [참고] this와 addEventListener
- addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻함
- 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨
- 결론: addEventListener의 콜백 함수는 function 키워드를 사용하기