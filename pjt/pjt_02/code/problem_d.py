import requests
from pprint import pprint
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ.get('api_key')

def recommendation(title):
    searchURL = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KO&region=KR&query={title}'
    response1 = requests.get(searchURL).json()
    resultlist = response1['results']

    if resultlist == []: # 검색한 영화 정보가 없을 경우
        return None

    else:
        movie_id = resultlist[0]['id'] # 검색결과의 최상단 영화의 id
        recommendURL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko-KO'
        response2 = requests.get(recommendURL).json()
        recommendlist = response2['results'] # 추천 영화 딕셔너리의 리스트

        titlelist = [] # 추천 영화가 없을 경우 자동으로 [] 반환
        for movie in recommendlist:
            titlelist.append(movie['title']) # 추천 영화 타이틀 추출
        return titlelist

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
