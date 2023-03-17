# 반응형 웹 페이지 구현
## 목표
- HTML을 통한 웹 페이지 마크업 이해
- CSS 라이브러리의 이해와 활용
- Bootstrap 컴포넌트 및 Grid system을 활용한 반응형 레이아웃 구성

## 준비사항
![image](https://user-images.githubusercontent.com/108309396/225780923-ee6846a3-3133-4d88-8a62-4b5c46a515df.png)  
- 참고) 시맨틱 태그
  - `<h1>`과 같이 기능(스타일이 변함)과 의미(제목)가 함께 있는 태그도 있는 반면, `<nav>`, `<header>`와 같이 의미(네비게이션바, 머릿말)만 담겨있는 태그도 있음
  - 의미만 있는 태그는 `<div>`와 같은 기능을 함
  - 코드의 가독성을 높이고 유지보수를 쉽게 하기 위해
  - 데이터 공유, 재사용을 위해
  - 검색 엔진 최적화(SEO)를 위해

## `01_nav_footer.html`
1. Navigation Bar
- Bootstrap Navbar Component 사용
- 스크롤을 하더라도 항상 화면 상단에 고정 &rarr; `fixed-top`
- Home, Community를 각각 `02_home.html, 03_community.html`에 연결하기 위해 src위치를 넣는데 해당 경로는 `01_nav_footer.html`이 들어있는 `/code/`부터 시작함 
  - `"/code/03_community.html"`
- modal button과 modal 기능을 조작하는데 있어 어려움을 겪음
  - Modal Component란? &rarr; 팝업창
  - modal button은 navbar 안에 넣어야 함
  - 기능은 navbar 안에 넣을 시 오류 발생 &rarr; navbar 태그 밖에 생성
- Viewpoet의 가로 크기 별 반응형 디자인은 breakpoint 사용(md, lg 등)
2. Footer
   - 스크롤을 하더라도 항상 화면 하단에 고정 &rarr; `fixed-bottom`
   - 수직, 수평 가운데 정렬 &rarr; text-center

##  `02_home.html`  
1. Header
   - Bootstrap Carousel COmponent 사용
   - 자동 전환 포맷 사용  
2. Section
   - 개별 article은 Bootstrap Card Component로 구성

## `03_community.html`
- community 탭 강조는 active 사용
1. Asied(게시판 목록)
   - HTML aside element
   - Bootstrap List Group Component로 구성
   - Viewport의 가로 크기가 lg 미만일 경우 전체 너비 &rarr; `col-10`
   - Viewport의 가로 크기가 lg 이상일 경우 1/6 &rarr; `col-lg-2`
2. Section(게시판)
   - Viewport의 가로 크기가 lg 미만일 경우 게시판은 HTML article 요소의 집합, 전체 너비
   - Viewport의 가로 크기가 lg 이상일 경우 게시판은 Bootstrap Tables Content, 5/6
   - HTML article 요소와 Bootstrap Tables Content는 연관성이 없기 때문에 hiding element 사용해야 함
     - `d-none d-lg-table` &rarr; lg 이상에서 table이 보임
     - `d-block d-lg-none` &rarr; lg 미만에서 article이 보임
   -  HTML article과 Bootstrap Tables Content를 `div wrapper`로 감싸 flexbox를 적용 &rarr; `justify-content-center`를 사용해 중앙 정렬한다.
3. Pagination
   - Bootstrap Pagination Component로 구성
   - 수평 중앙 정렬 &rarr; `justify-content-center`