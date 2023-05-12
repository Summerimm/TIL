# Vue를 활용한 SPA 구성
## 목표
- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 플러그인 활용

## 컴포넌트 구조
![image](https://github.com/Haaarimmm/TIL/assets/108309396/bcc3d387-8f0a-4839-a062-35d10c71629f)

## router view
![image](https://github.com/Haaarimmm/TIL/assets/108309396/10a0b7a9-4fc7-4118-b4cd-035c8f41e44e)

## 세부 요구사항
### 사전 설정
- `vue create my-vue-pjt`
- `vue add router`
- `vue add vuex`
- `npm install axios`
- `App.vue`에 router-link 및 router-view 추가
  - 선언적 방식 네비게이션 사용
- `router/index.js`에 View import 및 path, name, component 지정
- 
### A. 최고 평점 영화 출력
- `MovieView`
  - `created()` lifecycle hook을 이용해 메서드 `getMovies()`를 실행함
  - `methods`에서 `getMovies()`를 통해 store actions의 `getMovies`에 `dispatch`를 날림
  - store actions에서는 `getMovies(context)`로 axios 요청으로 보내 commit을 날려 state를 변경한다. 
  - `GET_MOVIES` mutations에서는 응답받은 영화 목록 전체를 movies 배열에 저장
  - `MovieCard`를 v-for directive를 통해 하나씩 불러옴
  - computed에서 `movies()`를 불러 store에 있는 movies를 가져옴
- `MovieCard`
  - `MovieView`에서 props 받은 movie를 명시해주고 computed를 이용해 poster_path로 포스터를 img로 보여준다.

### B. 최고 평점 영화 중 랜덤 영화 한 개 출력
- `RandomView`
  - 새로고침되어도 실행할 수 있도록 `created()` lifecycle hook을 이용해 `getMovies`에 `dispatch`를 날림
  - store actions에서는 `getMovies(context)`로 axios 요청으로 보내 commit을 날려 state를 변경한다. 
  - `GET_RANDOM_MOVIES` mutations에서는 응답받은 영화 중 하나를 랜덤으로 뽑아 randomMovie에 저장
  - button을 누르면 `randomMovie()` 메서드를 실행 &rarr; `getMovies`에 `dispatch`를 날림
  - v-if directive를 이용해 movie가 있을 때만 포스터와 타이틀을 보여준다.
  - `computed`에서는 movie에 state의 randomMovie를 가져온다

### C. 보고 싶은 영화 등록 및 삭제
- `WatchListView`
  - `WatchListForm`과 `WatchListItem`을 불러오고 등록하고 사용했다.
  - `WatchListItem`는 MovieList를 가져와 v-for로 돌리면서 하나씩 넣었다. 
  - `WatchListItem`에 movie를 props로 전달했다.
- `WatchListForm`
  - `createMovie` 메서드를 실행해서 store의 action, mutation을 차례로 실행
  - local storage에 저장
- `WatchListItem`
  - `updateMovie` 메서드를 실행해서 store의 action, mutation을 차례로 실행