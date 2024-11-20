import requests, json, os, io
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from Pylette import extract_colors
import numpy as np
load_dotenv(find_dotenv())
TMDB = os.getenv('tmdb')

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):		# np.integer를 python의 int로 변환
            return int(obj)
        if isinstance(obj, np.floating):	# np.floating을 python의 float로 변환
            return float(obj)
        if isinstance(obj, np.ndarray):		# np.ndarray를 python의 list로 변환
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

movie_results=[]
provider_results=[]
genre_results=[]

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB}"
}

popular_url = "https://api.themoviedb.org/3/discover/movie"
image_url = "https://image.tmdb.org/t/p/original"
providers_url = "https://api.themoviedb.org/3/watch/providers/movie?language=ko-KR&watch_region=KR"
genres_url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
de=['adult', 'backdrop_path', 'video', 'popularity', 'vote_count']
set_provider=(8,119,337,356,97,350)


# 공급자 데이터
def provider_data():
    responses = requests.get(providers_url, headers=headers).json()['results']
    
    for response in responses:
        if response['provider_id'] not in set_provider:continue
        p={
            'provider_id':response['provider_id'],
            'provider_name':response['provider_name'],
            'logo_path':image_url+response['logo_path']
        }
        provider_results.append(p)
    file_out('providers', provider_results)


# 장르 데이터
def genre_data():
    genre_results = requests.get(genres_url, headers=headers).json()['genres']
    file_out('genres', genre_results)

# 영화 데이터
def movie_data():
    global movie_results
    for i in range(1, 2):
        movie_params = {
            'sort_by':'popularity.desc',
            'include_adult':False,
            'include_video':False,
            'language':'ko-KR',
            'page':1,
            'vote_average.gte':6,
            'vote_count.gte':150,
            'watch_region':'KR',
            'with_watch_providers':'8|119|337|356|97|350',
            #Netflix | Amazon Prime Video | Disney Plus | wavve | Watcha | Apple TV Plus
            # 'with_watch_monetization_types':'flatrate|free|ads',
        }

        # 1페이지 씩 불러오기
        responses = requests.get(popular_url, headers=headers, params=movie_params).json()['results']

        # 불러온 데이터 커스텀
        for response in responses:
            # 필요 없는 항목 삭제
            for d in de:
                del response[d]
            
            # 포스터 url 채우기
            response['poster_path'] = image_url+response['poster_path']
            
            # TMDB 상 평점 저장
            tmdb_vote_average=response['vote_average']
            del response['vote_average']
            response['tmdb_vote_average']=tmdb_vote_average
            
            # 콘텐츠 제공사업자 목록 가져오기
            movie_id = response['id']
            movie_providers_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
            providers = requests.get(movie_providers_url, headers=headers).json()['results']['KR']
            p=set()
            for key, value in providers.items():
                if key=='link':continue
                for v in value:
                    pid=v['provider_id']
                    if pid in set_provider: p.add(pid)
            if p: response['watch_providers']=list(p)
            del response['id']
            
            # 포스터 색감 추출하기
            palette = extract_colors(image_url=response['poster_path'])
            poster_palette = list(map(lambda x:[x.rgb[0], x.rgb[1], x.rgb[2], x.freq], palette))
            response['poster_palette']=poster_palette
        
        # 처리 완료된 페이지 내용 결과에 추가
        movie_results+=responses
    file_out('movies', movie_results)

# 완성된 데이터 json으로 저장
def file_out(dataname, data):
    with open(f'{dataname}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent="\t", cls=NpEncoder)
    print(len(data))


if __name__=='__main__':
    provider_data()
    genre_data()
    movie_data()