import requests
from pprint import pprint

results=[]

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzdmZmQwODVkMjk5Y2NkOTQ3MmRkOWQ5N2NlZjFiNCIsIm5iZiI6MTczMTkxMDY4My4wMTkwMDk2LCJzdWIiOiI2NzJhMzNhZjE0ZDRhMzk5NzIwMzU2MDgiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.N8hx1t0qh5wZtGn7HktjxlYMbpk_pRso_AH603WrH1k"
}

popular_url = "https://api.themoviedb.org/3/discover/movie"


for i in range(1, 51):
    params = {
        'sort_by':'popularity.desc',
        'include_adult':False,
        'include_video':False,
        'language':'ko-KR',
        'page':i,
        'vote_average.gte':6,
        'vote_count.gte':300,
    }

    responses = requests.get(popular_url, headers=headers, params=params).json()['results']

    for response in responses:
        pass

pprint(results)
