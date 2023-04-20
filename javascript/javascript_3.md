# DOM
- 스크립트 언어(Script Language): 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍

## 1. Browser APIs
- 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함
- 종류: DOM, Geolocation API, WebGL 등

### 브라우저가 웹 페이지를 불러오는 과정
- 웹 페이지를 브라우저로 불러오면, 브라우저는 코드(HTML, CSS, JavaScript)를 실행 환경(브라우저 탭)에서 진행
- JavaScript는 `DOM API`를 통해 HTML과 CSS를 동적으로 수정, 사용자 인터페이스를 업데이트 하는 일에 많이 쓰임

## DOM이란?
- 문서 객체 모델(Document Object Model)
- **문서의 구조화된 표현을 제공**하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
- **HTML 문서를 구조화하여 각 요소를 객체(object)로 취급**
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능함
- 웹 페이지는 일종의 문서(document)
- DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정 가능

## DOM 기본 구조
### DOM Tree
- DOM은 문서를 논리 트리로 표현
- DOM에서 모든 것은 **Node**
- 즉, HTML 요소, 속성, 텍스트 모든 것이 노드
- 각 노드는 부모, 자식 관계를 형성하고 이에 따라 상속 개념도 동일하게 적용됨  
- DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음    
![image](https://user-images.githubusercontent.com/108309396/233236900-7e439979-68eb-4c68-b192-b149f861cc89.png)

## Node
- DOM의 구성 요소 중 하나
- HTML 문서의 모든 요소를 나타냄
  - 각각의 HTML 요소는 DOM Node로서 특정한 노드 타입을 가짐
  - Document Node === HTML 문서 전체를 나타내는 노드
  - Element Node === HTML 요소를 나타내는 노드 ex) `<p>`
  - Text Node === HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
  - Attribute Node === HTML 요소의 속성을 나타내는 노드

## DOM의 객체
- `window`
- `document`: DOM의 주요 객체
- `navigator, location, history, screen` 등

### `window` object
- DOM을 표현하는 창
- 가장 최상위 객체(생략 가능)
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄  
![image](https://user-images.githubusercontent.com/108309396/233240581-55a6c50d-231f-4e07-9658-fc1616961bd8.png)
- `window`의 메서드
  - 새 탭 열기  
  ![image](https://user-images.githubusercontent.com/108309396/233240666-270e0610-5488-46e5-9f84-41915c76508d.png)
  - 경고 대화 상자 표시  
  ![image](https://user-images.githubusercontent.com/108309396/233240748-532dd4b2-5d37-4fda-afa3-db09aae5e7ab.png)
  - 인쇄 대화 상자 표시  
  ![image](https://user-images.githubusercontent.com/108309396/233240777-69c43f22-1b16-42ff-8a94-86eded2d0614.png)

### `document` object
- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점 역할을 하며, `<body>`등과 같은 수많은 다른 요소들을 포함하고 있음
- `document`는 `window`의 속성이다.

### [참고] Node vs Element
- 모든 것은 Node
- `<head>, <body>`는 HTML 요소로 element
- `<title>, <p>`는 Text Node이면서 element
- `id="unique"`는 DOM에서는 `Attr Node`이고, HTML 요소인 `<p>`의 속성이므로 elemente는 아님

# DOM 조작
## 선택 관련 메서드
- `document.querySelector(selector)`
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS Selector를 만족하는 첫 번째 element 객체를 반환(없다면 `null` 반환)
- `document.querySelectorAll(selector)`
  - 제공한 선택자와 일치하는 element 여러 개 선택
  - 매칭할 하나 이상의 selector를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 제공한 CSS selector를 만족하는 NodeList를 반환

### [참고] NodeList
- DOM 메서드를 사용해 선택한 노드의 목록
- 배열과 유사한 구조를 가짐
- Index로만 각 항목에 접근 가능
- 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
  - but push(), pop() 등 사용 불가
- `querySelectorAll()`에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

## 조작 관련 메서드
1. 생성
- `document.createElement(tagName)`
  - 작성한 tagName의 HTML 요소를 생성하여 반환

2. 입력
- `HTML.innerText`
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(해당 요소 내부의 raw text)
  - 사람이 읽을 수 있는 요소만 남김
  - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨

3. 추가
- `Node.appendChild()`
  - 한 Node를 특정 부모 Node의 자식 nodeList 중 마지막 자식으로 삽입
  - 한 번에 오직 하나의 Node만 추가 가능
  - 추가된 Node 객체를 반환
- 새롭게 생성한 Node가 아닌 이미 문서에 존재하는 Node를 다른 Node의 자식으로 삽입하는 경우, 위치를 이동 
![image](https://user-images.githubusercontent.com/108309396/233245976-c1df7711-5cae-4bd0-b64b-5486e725af98.png)  

4. 삭제
- `Node.removeChild()`
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환

## 속성 조회 및 설정
- `Element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

### [참고] 그 외 다양한 속성 조작 방법
- 만약 기존 속성은 유지한 채로, 새로운 값을 추가하고자 한다면 `Element.classList, Element.style` 등을 통해 직접적으로 해당 요소의 각 속성들을 제어할 수 있음