# Python을 활용한 데이터 수집 1
## 목표
- Python 기본 문법 습득
- 파일 입출력에 대한 이해
- 데이터 구조에 대한 분석과 이해
- 데이터를 가공하고 JSON 형태로 구성하기

## 준비사항
- 개발도구
  - Visual Studio Code
  - Python 3.9+
- 필수 라이브러리
  - json

## 요구사항
- 커뮤니티 서비스 개발을 위한 데이터 구성 단계로, 필요한 영화 데이터를 직접 추출 및 구성  
  ### A. 제공되는 영화 데이터의 주요내용 수집
  - id, title, overview 등 movie.json에서 필요한 정보에 해당하는 값을 추출
  - 필요한 정보를 새로운 dictrionary로 반환하는 함수 movie_info를 완성  
  ### B. 제공되는 영화 데이터의 주요내용 수정
  - 이전 단계에서 만들었던 데이터 중 `genre_ids`를 장르 번호가 아닌 장르 이름 리스트 genre_names로 바꿔 반환하는 함수를 완성
  - genres.json을 이용해 genre_ids를 각 장르 번호에 맞는 name값으로 대체한 genre_names 키를 생성
  ### C. 다중 데이터 분석 및 수정
  - movies.json에 있는 평점이 높은 20개의 영화 데이터 중 필요한 정보만 추출해 list를 반환하는 함수 movie_info를 완성
  ### D.알고리즘을 사용한 데이터 출력
  - 영화 세부 정보 중 revenue를 사용하여 모든 영화 중 가장 높은 수익을 낸 영화의 제목(title)을 출력하는 알고리즘을 작성.
  - 반복문을 통해 movies 폴더 내부의 파일들을 오픈
  ### E. 알고리즘을 사용한 데이터 출력
  - 영화 세부 정보 중 release_date를 사용하여 모든 영화 중 12월에 개봉한 영화들의 제목(title) 리스트를 출력하는 알고리즘을 작성.
  - 반복문을 통해 movies 폴더 내부의 파일들을 오픈

## example 분석
### 01 example
- `dict.get(key, default=None)`  
&rarr; 딕셔너리의 key에 해당하는 value를 반환  
&rarr; 해당 ket가 존재하지 않을 경우 두 번째 argument를 반환
### 02 example
  - dict.get을 이용해 dictionary 내에서 원하는 정보만 추출해 재구성
### 03 example
  - `import json`
  - `open('sample.json', encoding='utf-8')`에서 에러 발생  
  &rarr; `FileNotFoundError: [Errno 2] No such file or directory: 'sample.json'`  
  &rarr; open(r"절대경로", ~)로 해결  
  &rarr; `movie = open(r"C:\Users\SSAFY\ssafy9\myssafy\0120\code\examples\sample.json", encoding='utf-8')`
- `json.load(movie)` : JSON 파일을 읽어 딕셔너리로 변환

## Problem 분석
### problem_a.py
- `FileNotFoundError: [Errno 2] No such file or directory: 'data/movie.json'` 문제 발생
- 절대경로로 해결
- 실행 경로의 문제로 code폴더 내에서 실행하면 정상작동하는 걸 확인
- **기존에 일일이 `'genre_ids': movie.get('genre_ids'),` 처리했던 부분을 개선**
  - `requirements = ['genre_ids', 'id', 'overview', ...]` 
  - 반복문을 사용해 key가 requirements에 들어있다면 new_data dicitonary에 추가하는 형식 
  ```python  
    for key, value in movie.items():
        if key in requirements:
            getitem = movie.get(key)
            new_data[key] = getitem
  ```
### problem_b.py
- `new_data`를 초기화 후 genre_names 값을 추출해 new_data에 genre_names을 새로운 key로 넣어준다
  ```python
  for genre in genres:
      if genre.get('id') in idlist:
          genre_names.append(genre.get('name'))
  new_data['genre_names'] = genre_names
  ```
### problem_d.py
- index 반환하는 함수 &rarr; index(), 즉 최댓값의 index값을 반환하려면 index(max(a))

### problem_f.py
> best_five(movies)
- vote_average 순으로 정렬 &rarr; 만약 같다면 vote_count 높은 순으로 정렬 시도
- 전체 영화 데이터를 순회하며 vote_average, vote_count, title 값을 추출
- {title1: [avg, count], title2: [avg, count], ...} 형식으로 저장
- `sorted(title_avgcount_dict.items(), key=lambda x: x[1], reverse=True)`
  - 람다함수를 이용해 value(average와 count)를 기준으로 dictionary가 정렬되게 함
- bestfive list에 상위 다섯 개 title을 append
> bestoneposter(data, movies):
- 가장 평점이 높은 영화를 가져와서 poster_path를 추출
- `webbrowser.open("https://image.tmdb.org/t/p/w500"+f'{poster_path}')`로 웹브라우저 연결해 포스터를 띄움
- `import webbrowser` 필요