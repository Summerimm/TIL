import json
import webbrowser

def best_five(movies):
    bestfive = []
    detail_dict = {}
    title_avgcount_dict = {}

    for idx, movie in enumerate(movies):
        id = movie.get('id') # extract id of each movie
        detail_json = open('data/movies/'+f'{id}'+'.json', encoding='utf-8') # open detail json file based on movie id
        detail_dict = json.load(detail_json) # load detail json file on detail dict
        vote_average = detail_dict.get('vote_average')
        vote_count = detail_dict.get('vote_count')
        title = detail_dict.get('title')
        countavg = [vote_average, vote_count]
        title_avgcount_dict[title] = countavg
    
    #print(title_avgcount_dict)
    sorted_title = sorted(title_avgcount_dict.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_title) # {'쇼생크 탈출': [8.7, 18481], '대부': [8.7, 13938], '쉰들러 리스트': [8.6, 11099], ...}
    for i in range(5):
        bestfive.append(sorted_title[i][0]) # title만 추출
    print(f'평점이 가장 높은 상위 영화 5개는 {bestfive}입니다.')
    return bestfive

def bestoneposter(data, movies):
    bestmovie = data[0] # 쇼생크탈출
    print(f'가장 평점이 높은 영화는 {bestmovie}입니다!')
    for movie in movies:
        if movie.get('title') == bestmovie:
            poster_path = movie.get('poster_path')
    
    return webbrowser.open("https://image.tmdb.org/t/p/w500"+f'{poster_path}') #웹브라우저를 열어 영화 포스터를 보여줌 


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    fivelist = best_five(movies_list) # vote_average + vote_count로 정렬해 상위 5개 영화 출력
    bestoneposter(fivelist, movies_list)