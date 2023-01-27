import requests
from pprint import pprint
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ.get('api_key')

def credits(title):
    searchURL = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KO&region=KR&query={title}'
    response1 = requests.get(searchURL).json()
    resultlist = response1['results']

    if resultlist == []: # 검색한 영화 정보가 없을 경우
        return None

    else:
        movie_id = resultlist[0]['id'] # 검색결과의 최상단 영화의 id
        creditURL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-KO'
        response2 = requests.get(creditURL).json()
        castlist = response2['cast'] # 검색 영화의 cast 딕셔너리의 리스트
        crewlist = response2['crew'] # 검색 영화의 crew 딕셔너리의 리스트

        castans = []
        for cast in castlist:
            if cast['cast_id'] < 10:
                castans.append(cast['name'])

        crewans = []
        for crew in crewlist:
            if crew['department'] == 'Directing':
                crewans.append(crew['name'])
        
        ans = {'cast': castans, 'directing': crewans}
        return ans


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
