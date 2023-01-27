import json


def max_revenue(movies):
    revenue_list = []
    idxdict = {}

    for idx, moviesdict in enumerate(movies):
        id = moviesdict.get('id') # extract id of each movie
        detail_json = open('data/movies/'+f'{id}'+'.json', encoding='utf-8') # open detail json file based on movie id
        detail_dict = json.load(detail_json) # load detail json file on detail dict
        revenue = detail_dict.get('revenue')
        revenue_list.append(revenue)
        idxdict[idx] = detail_dict.get('title') # index dictionary에 index(key)와 title(vaule) 저장

    i = revenue_list.index(max(revenue_list)) # revenue_list에서 max값의 index를 저장
    return idxdict[i] # 최대 수익의 index에 해당하는 title 추출 
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
