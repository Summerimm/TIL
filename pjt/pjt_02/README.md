# Python을 활용한 데이터 수집 2
## 목표
- Python 기본 문법 습득
- 데이터 구조에 대한 분석과 이해
- 요청과 응답에 대한 이해
- API의 활용과 API 문서 숙지

## 준비사항
- 개발도구
  - Visual Studio Code
  - Python 3.9+
- 필수 라이브러리
  - Requests
- API
  - TMDB API: 영화 정보 및 API 서비스

## 요구사항
- 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 필요한 영화 데이터를 수집하는 과정
- API 요청 시 언어 및 지역 설정 데이터는 한국을 기준으로 함
  ### A. 인기 영화 조회
  - 인기 영화 목록을 응답받아 개수 출력
  - requests 라이브러리를 사용하여 TMDB에서 Get Popular 데이터를 요청
  - 응답 받은 데이터의 영화 개수를 반환하는 함수 popular_count 작성
  - `URL = 'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KO&region=KR'`
  - `https`: 규약, `api.themoviedb.org/3`: domain name, `movie/popular`: path, `?`뒤는 `key1=value1&key2=value2`
  ### B. 특정 조건에 맞는 인기 영화 조회1
  - 8점 이상인 영화 목록 출력
  ### C. 특정 조건에 맞는 인기 영화 조회2
  - 평점이 높은 순으로 5개의 영화 데이터 목록 출력
  - `sorted(movielist, key=lambda x:x['vote_average'], reverse=True)`: 람다함수를 이용해 정렬, 여기서 x는 list의 원소
  ### D. 특정 추천 영화 조회
  - 제공된 영화 제목('기생충', '그래비티', '검색할 수 없는 영화')을 검색하여 추천 영화 목록을 출력
  - Search Movies, Get Recommendations
  - `searchURL = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KO&region=KR&query={title}'`
  - `recommendURL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko-KO'`
  ### E. 출연진, 연출진 데이터 조회
  - 제공된 영화 제목('기생충', '검색할 수 없는 영화')을 검색하여 해당 영화의 cast 출력, crew 중 Directing의 이름을 출력
  - Search Movies, Get Credits
  - 출연진은 cast_id 10 미만의 출연진만 추출, 연출진은 스태프 부서(department)가 Directing인 데이터만 추출

## example 분석
### 01 example
- `import requests`
- `response = requests.get(URL).json()`: URL로 요청을 보내 json형식으로 응답받음  
&rarr; `{'status': 'success', 'message': 'https://images.dog.ceo/breeds/papillon/n02086910_2897.jpg'}`

### 02 example
  - params를 미리 directory 형식으로 선언하고 `response = requests.get(URL, params=params).json()`로 응답받음
  - 앞의 params는 parameter, 뒤의 params는 argument

## Optional Project
> 웹 브라우저를 열어 선택한 영화의 예고편을 재생하고자 한다.
1. `nowplaying`
    - 1 클릭 시 실행
    - nowplaying API를 활용
    - 일정 기간동안의 최신 영화의 목록을 보여주고 영화를 선택하게 해 `movie_id`를 반환하는 함수이다.
    - 해당 기한 역시 API를 통해 받아와 출력
    - sorted 함수를 통해 평점을 기준으로 최신영화 타이틀을 정렬했다. &rarr; 람다함수를 이용해 편하게 평점을 기준으로 정렬가능
    - 영화 이름을 직접 입력하는 것보다 숫자를 입력하는 것이 편하므로 index 숫자와 movie id를 다시 연결짓는 dictionary가 필요했다.
    - 예고편을 볼 영화의 번호를 입력받아 dictionary에서 id를 찾아 반환했다.
2. `searching(title)`
    - 2 클릭 시 실행
    - search API를 활용
    - 타이틀과 개봉일자(slicing을 통해 더 보기좋게 출력), index를 동시에 출력
    - 마찬가지로 index와 id를 연결시키는 dictionary가 필요했다.
    - 예고편을 볼 영화의 번호를 입력받아 dictionary에서 id를 찾아 반환했다.
3. `video(movie_id)`
    - video API를 활용
    - 받은 movie_id를 통해 공식 트레일러 영상 목록을 출력한다.
    - 입력할 수 있는 숫자(index)와 video title로 출력했다.
    - index와 video key를 연결시키는 dictionary 생성
    - 영상 번호를 입력받아 dictionary에서 video key를 찾는다.
    - 유튜브 url에 videokey를 넣고 webbrowser 라이브러리를 통해 url을 open했다.

## 새롭게 알게 된 점
- URL의 구성: `URL = 'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KO&region=KR'`
  - `https`: 규약, `api.themoviedb.org/3`: domain name, `movie/popular`: path, `?`뒤는 `key1=value1&key2=value2`
- `import pprint` 후 pprint는 dictionary 형식을 json 형식으로 보기 좋게 출력 **pretty print!**
- `.env`를 통해 api_key 관리 가능 &rarr; GitHub 업로드 시 `.gitignore`에 의해 업로드 되지 않음(하지만 .env파일은 따로 들고다녀야 함)
  - problem_f.py 내부
  ```python
  from dotenv import load_dotenv
  import os 

  load_dotenv()
  api_key = os.environ.get('api_key')
  ```
  - .env
  ```python
  api_key = 123456789
  ```