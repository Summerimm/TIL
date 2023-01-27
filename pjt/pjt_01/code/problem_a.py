import json
from pprint import pprint


def movie_info(movie):
    new_data = {}
    requirements = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average']

    for key in requirements:
            new_data[key] = movie.get(key)

    return new_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data\movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
