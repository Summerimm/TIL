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
1. block tag 영역 base.html에 작성  
  ![image](https://user-images.githubusercontent.com/108309396/235388550-23a04ae8-71ad-4d1e-bd50-56515af9fbc5.png)
2. axios CDN 작성  
  ![image](https://user-images.githubusercontent.com/108309396/235388582-e07ec313-0d74-4a16-aca5-397a2ad75ecf.png)
3. form 요소 선택을 위해 id 속성 지정 및 선택  
  ![image](https://user-images.githubusercontent.com/108309396/235388602-64768d46-b433-456b-8c47-dbeb0965f0c9.png)
   - action과 method 속성은 불필요하므로 삭제(요청은 axios로 대체되기 때문)
4. form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소  
  ![image](https://user-images.githubusercontent.com/108309396/235388656-7b29f888-19a8-40d6-b7e4-84cb8b32f448.png)
5. axios 요청 준비  
  ![image](https://user-images.githubusercontent.com/108309396/235388672-0eb08cb5-fc01-422b-b508-bdb02ceaa0b3.png)
6. url에 작성할 user pk 가져오기(HTML &rarr; JavaScript)  
  ![image](https://user-images.githubusercontent.com/108309396/235388700-1b5bb551-606d-4196-bc6e-fbde3082aedb.png)
7. url 작성 완료  
  ![image](https://user-images.githubusercontent.com/108309396/235388729-621c133d-da95-43ea-ab23-d69c31dae202.png)
8. csrf 값을 가진 input 태그 선택  
  ![image](https://user-images.githubusercontent.com/108309396/235388746-d222ca93-dd04-4d26-916a-7c16dfe1d718.png)
9.  AJAX로 csrftoken을 보내기  
  ![image](https://user-images.githubusercontent.com/108309396/235388762-bb85e31b-d0d1-428e-9acd-82dc043432e0.png)
10. 팔로우 여부를 확인하기 위한 `is_followed` 변수 작성 및 JSON 응답  
  ![image](https://user-images.githubusercontent.com/108309396/235388783-accbadcb-24b4-4a4b-acbb-5b2c4a52b845.png)
11. view 함수에서 응답한 `is_followed`를 사용해 버튼 토글하기  
  ![image](https://user-images.githubusercontent.com/108309396/235388813-5a37c46d-efc5-4a6a-afd7-de9c3f0f2f87.png)


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
1. 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성  
  ![image](https://user-images.githubusercontent.com/108309396/235388845-e3dc0034-db03-4156-a2a5-7978b99f4fc6.png)
2. 직전에 작성한 span 태그 각각 선택    
  ![image](https://user-images.githubusercontent.com/108309396/235388861-4c07c276-6941-43f6-b979-00cfe7845ba7.png)
3. 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달  
  ![image](https://user-images.githubusercontent.com/108309396/235388882-ece8829d-4eb5-4f92-98d8-d6fc2a8f193f.png)
4. view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경  
  ![image](https://user-images.githubusercontent.com/108309396/235388912-6d0b0d10-3b8b-4830-82a8-a0c095b61f5f.png)

### 팔로우 & 팔로잉 최종코드
![image](https://user-images.githubusercontent.com/108309396/235388935-f4e9a672-6bf5-4c01-a200-3de0f5989ac6.png)  
![image](https://user-images.githubusercontent.com/108309396/235388956-b48761ca-fae7-46b5-9ae6-6bd6e37b691b.png)  
![image](https://user-images.githubusercontent.com/108309396/235388962-818b085d-8338-4ae6-b04d-c5c9f16cdb1b.png)


## 좋아요(like)
- 좋아요 비동기 적용은 "팔로우와 동일한 흐름 + `forEach() & querySelectorAll()`
  - index 페이지 각 게시글마다 좋아요 버튼이 있기 때문

### 좋아요 최종코드
![image](https://user-images.githubusercontent.com/108309396/235388983-301f9519-ef9e-44cf-8f69-f27e1232061b.png)  
![image](https://user-images.githubusercontent.com/108309396/235388993-4105fcf4-20be-4c23-a3ba-efc215490eea.png)  
![image](https://user-images.githubusercontent.com/108309396/235389000-10eab446-50b2-4ffc-8346-2ccee68a6d79.png)
