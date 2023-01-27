# 요즘 상영하고 있는 영화 리스트 출력
import requests
from pprint import pprint
import webbrowser
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ.get('api_key')

def nowplaying():
    URL = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=ko-KO'
    response = requests.get(URL).json()

    # 최신 기간
    datedic = response['dates']
    oldestdate = datedic['minimum']
    latestdate = datedic['maximum']
    print(f'{oldestdate} ~ {latestdate} 기간 동안 상영 중인 영화입니다')
    print('==========================================================')

    # 최신 영화 타이틀+평점 출력
    movies_list = response['results']
    sorted_list = sorted(movies_list, key=lambda x: x['vote_average'], reverse=True)
    index_id = {}
    index = 0
    for movie in sorted_list:
        title = movie['title']
        vote_avg = movie['vote_average']
        index += 1
        index_id[index] = movie['id'] # title과 id 매칭시켜 dictionary 생성
        print(f'{index} <{title}> 평점 {vote_avg}점')
    print('==========================================================')

    # 예고편을 볼 영화를 입력받기
    print('공식 예고편을 볼 영화의 번호를 선택해주세요: ', end='')
    select = int(input()) # 영화 입력받기
    movie_id = index_id[select] # 선택한 번호로 id 찾기

    return movie_id

def searching(title):
    searchURL = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KO&region=KR&query={title}'
    response = requests.get(searchURL).json()
    print('다음은 입력하신 영화와 일치하는 검색 결과입니다')
    print('==========================================================')

    # 검색한 영화 타이틀+개봉일자 출력
    searchlist = response['results']
    index_id = {}
    index = 0
    for movie in searchlist:
        title = movie['title']
        date = movie['release_date']
        index += 1
        index_id[index] = movie['id'] # title과 id 매칭시켜 dictionary 생성
        print(f'{index} <{title}> 개봉일자:{date[0:4]}/{date[5:7]}/{date[8:10]}')
    print('==========================================================')

    # 예고편을 볼 영화를 입력받기
    print('공식 예고편을 볼 영화의 번호를 선택해주세요: ', end='')
    select = int(input()) # 영화 입력받기
    movie_id = index_id[select] # 선택한 번호로 id 찾기

    return movie_id


def video(movie_id):
    if movie_id == None:
        return None
    else:
        URL = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language=ko-KO' # 영화의 트레일러 찾기
        response = requests.get(URL).json()

        # 해당 영화에 대한 공식 트레일러 영상 리스트 출력
        print('==========================================================')
        print('다음은 공식 트레일러 영상입니다')
        print('==========================================================')
        video_list = response['results'] 
        index = 0
        idx_key = {}
        for video in video_list:
            video_title = video['name']
            index += 1
            idx_key[index] = video['key']
            print(f'{index} {video_title}')
        
        # 감상할 예고편의 번호 입력받기
        print('예고편을 볼 영상의 번호를 선택해주세요: ', end='')
        num = int(input())
        videokey = idx_key[num]
        URL = f'https://www.youtube.com/watch?v={videokey}'
        return webbrowser.open(URL)

if __name__ == '__main__':
    """
    - 요즘 상영하고 있는 영화 출력
        - 12월 15일부터 2월 1일까지 상영 중인 영화(기간 출력)

    - 그 영화의 공식 트레일러가 존재할 경우 웹 브라우저에서 트레일러 재생
    - 존재하지 않으면 None
    """
    flag = 1
    while(flag):
        print('최신 영화 중에서 예고편을 감상하시려면 1, 검색 후 해당 영화의 예고편을 감상하시려면 2를 입력해주세요: ', end='')
        recentorsearch = int(input())
        if recentorsearch == 1:
            movieid = nowplaying()
            video(movieid)
            flag = 0
        elif recentorsearch == 2:
            print('감상하고 싶으신 영화의 제목을 입력해주세요: ', end='')
            titleinput = input()
            movieid = searching(titleinput)
            video(movieid)
            flag = 0
        else:
            print('잘못 입력하셨습니다. 다시 입력해주세요')