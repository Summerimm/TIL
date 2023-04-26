# AJAX
## AJAX란?
- Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)
- 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
- '비동기 통신 웹 개발 기술' == AJAX
- 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

## AJAX 특징
- 페이지 전체를 reload하지 않고서도 수행되는 "비동기성"
- 서버의 응답에 따라 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
1. 페이지 새로고침 없이 서버에 요청
2. 서버로부터 응답(데이터)을 받아 작업 수행

# 비동기(Async) 적용하기
## Follow
1. block tag 영역 base.html에 작성(p.8)
2. axios CDN 작성(p.9)
3. form 요소 선택을 위해 id 속성 지정 및 선택(10)
   - action과 method 속성은 불필요하므로 삭제(요청은 axios로 대체되기 때문)
4. form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소(11)
5. axios 요청 준비(12)
6. url에 작성할 user pk 가져오기(HTML &rarr; JavaScript) (15)
7. url 작성 완료(18)
8. csrf 값을 가진 input 태그 선택(21)
9. AJAX로 csrftoken을 보내기(22)
10. 팔로우 여부를 확인하기 위한 `is_followed` 변수 작성 및 JSON 응답(24)
11. view 함수에서 응답한 `is_followed`를 사용해 버튼 토글하기(25)


### [참고] `data-* attributes`
- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법
- 사용 예시
- 모든 사용자 지정 데이터는 dataset 속성을 통해 사용할 수 있음
- 속성명 작성 시 주의사항
  - 대소문자 여부에 상관없이 xml로 시작X
  - 세미콜론 포함X
  - 대문자 포함X

### [참고] XHR
- XMLHttpRequest
- AJAX 요청을 생성하는 JavaScript API
- XHR의 메서드로 브라우저와 서버 간 네트워크 요청 전송 가능
- Axios는 손쉽게 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리

## 팔로워 & 팔로잉 수 비동기 적용
1. 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성(28)
2. 직전에 작성한 span 태그 각각 선택(29)
3. 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달(30)
4. view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경

### 팔로우 & 팔로잉 최종코드(32~34)

## 좋아요(like)
- 좋아요 비동기 적용은 "팔로우와 동일한 흐름 + `forEach() & querySelectorAll()`
  - index 페이지 각 게시글마다 좋아요 버튼이 있기 때문

### 좋아요 최종코드(36~38)