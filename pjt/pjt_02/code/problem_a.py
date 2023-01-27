import requests
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ.get('api_key')

def popular_count():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KO&region=KR'
    response = requests.get(URL).json()
    return len(response['results'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
