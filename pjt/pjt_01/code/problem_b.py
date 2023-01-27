import json
from pprint import pprint


def movie_info(movie, genres):
    new_data = {}
    idlist = movie.get('genre_ids') # genre_ids 추출 [18, 80]
    genre_names = [] # genre_names: id 추출한 값과 genres에서 같은 id 찾아 name 저장
    requirements = ['id', 'overview', 'poster_path', 'title', 'vote_average']
    
    for genre in genres:
        if genre.get('id') in idlist:
            genre_names.append(genre.get('name'))
    new_data['genre_names'] = genre_names

    for key  in requirements:
        new_data[key] = movie.get(key)
    return new_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
