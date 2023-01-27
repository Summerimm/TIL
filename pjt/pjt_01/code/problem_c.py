import json
from pprint import pprint


def movie_info(movies, genres): 
    all_list = [] 
    requirements = ['id', 'overview', 'poster_path', 'title', 'vote_average']
    genres_dict = {}

    for genre in genres:
        genres_dict[genre.get('id')] = genre.get('name')

    for movie in movies: # 각 movie에 대해서
        new_data = {}
        genre_names = [] # genre_names: id 추출한 값과 genres에서 같은 id 찾아 name 저장
        idlist = movie.get('genre_ids') # genre_ids 추출 [18, 80]

        for id in idlist:
            genre_names.append(genres_dict[id])
        new_data['genre_names'] = genre_names

        for key in requirements:
                new_data[key] = movie.get(key)

        all_list.append(new_data) # all_list에 각 movie에 대한 정보 저장
    return all_list # 한 번에 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
