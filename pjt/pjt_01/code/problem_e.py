import json


def dec_movies(movies):
    date_list = []
    mv_list = []
    idxdict = {}

    for idx, moviesdict in enumerate(movies):
        id = moviesdict.get('id') # extract id of each movie
        detail_json = open('data/movies/'+f'{id}'+'.json', encoding='utf-8') # open detail json file based on movie id
        detail_dict = json.load(detail_json) # load detail json file on detail dict
        release_date = detail_dict.get('release_date')
        if release_date[5:7] == '12': # 12월만 slicing
            mv_list.append(detail_dict.get('title'))
    
    return mv_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
