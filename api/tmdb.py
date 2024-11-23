﻿import requests, json, os
from dotenv import load_dotenv, find_dotenv
from Pylette import extract_colors
import numpy as np
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests

options = Options()
# options.add_argument("--headless")  # 129버전에선 --headless=old로 흰창 날릴 순 있으나 다른버전에서 문제 생길 수 있으므로 저 멀리 날려버림
# options.add_argument("--window-position=-15400,-15400")  # 창이 뜨는 위치 변경. 4k나 8k에선 보일수도?
options.add_argument("log-level=3")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36")
options.add_argument("--window-size=1920,1080")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
options.add_experimental_option("useAutomationExtension", False)
service = Service(ChromeDriverManager().install())

url = 'https://pedia.watcha.com/ko-KR'

dr = webdriver.Chrome(service=service, options=options)
dr.get(url)
wait = WebDriverWait(dr, 5)
act = ActionChains(dr)

dr.implicitly_wait(5)

try:
    bt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.hsDVweTz")))
    bt.click()
except:pass

dr.implicitly_wait(5)

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


def selenium_data(movie_name, movie_year):
    
    if "'" in movie_name:movie_name=movie_name.split("'")[1]
    if '블랙펄' in movie_name:movie_name = movie_name.replace('블랙펄', '블랙 펄')
    if '크레용' in movie_name:movie_name = movie_name.replace('보라색', '마법')
    if '번개도둑' in movie_name:movie_name = movie_name.replace('번개도둑', '번개 도둑')
    if '엔젤 해즈 폴른' == movie_name:movie_name = '앤젤 해즈 폴른'
    if '블레어 위치' == movie_name:movie_name = '블레어 윗치'
    if '장난감이 살아있다' == movie_name:movie_year = '2016'
    if '엠 아이 오케이?' == movie_name:movie_year = '2022'
    if '킬 빌: 1부' == movie_name:movie_name = '킬 빌'
    if '밀레니엄: 제1부 여자를 증오한 남자들' == movie_name:movie_name = '밀레니엄 1 : 여자를 증오한 남자들'
    if '애니 2015' == movie_name:movie_name = '애니'
    
    
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "searchKeyword")))
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys(movie_name)
    search_box.send_keys(Keys.ENTER)

    sleep(0.5)

    try:
        movie_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v1F9TlrZ")))
    except: 
        if ":" in movie_name: movie_name=movie_name.split(":")[1]
        elif '2' in movie_name or '3' in movie_name: movie_name=movie_name.replace('2','').replace('3','')
        search_box = wait.until(EC.visibility_of_element_located((By.NAME, "searchKeyword")))
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        search_box.send_keys(movie_name)
        print(movie_name)
        search_box.send_keys(Keys.ENTER)
        sleep(0.5)
        movie_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v1F9TlrZ")))
    
    movie_list = WebDriverWait(movie_box, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "listWrapper")))
    try:
        movie = WebDriverWait(movie_list, 5).until(EC.visibility_of_element_located((By.XPATH, f"//a[@title='{movie_name}']//div[contains(text(), {movie_year}) or contains(text(), {str(int(movie_year)+1)}) or contains(text(), {str(int(movie_year)-1)})]")))
    except:
        movie = WebDriverWait(movie_list, 5).until(EC.visibility_of_element_located((By.XPATH, f"//a//div[contains(text(), {movie_year}) or contains(text(), {str(int(movie_year)+1)}) or contains(text(), {str(int(movie_year)-1)})]")))
    movie.click()

    sleep(1)
    content_url = dr.current_url
    contents_url = content_url+'/comments'
    
    body=dr.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    sleep(0.5)

    picture=[]
    try:
        gal = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='갤러리']//..//..")))
        btn = WebDriverWait(gal, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))

        while True:
            try:
                btn.send_keys(Keys.ENTER)
                sleep(0.2)
            except:break

        galleries = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'MfhUSmJK')))

        for gallery in galleries:
            try:
                pic = WebDriverWait(gallery, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "div")))
                pstyle = pic.get_attribute('style')
                picture.append(pstyle.split('"')[-2])
            except:continue
    except:print(movie_name, "None Picture")
    
    video_url = []
    try:
        videotag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "OEje6csz")))
        for video in videotag:
            try:video_url.append(requests.get(video.get_attribute('href')).url.replace('watch?v=', 'embed/'))
            except:continue
    except:print(movie_name, "None Video")

    dr.get(contents_url)
    sleep(1)
    reviews=[]
    try:
        comments = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'eqSewv3p')))
        for comment in comments:
            try: 
                if comment.text: reviews.append(comment.text)
            except:continue
    except:print(movie_name, "None Reviews")
    
    return picture, video_url, reviews, content_url


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
def movie_data(start_page = 1, end_page = 50):
    # global movie_results
    for i in range(start_page, end_page+1):
        movie_params = {
            'sort_by':'popularity.desc',
            'include_adult':False,
            'include_video':False,
            'language':'ko-KR',
            'page':i,
            'vote_average.gte':6,
            'vote_count.gte':200,
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
            response['movie_id']=movie_id
            
            
            # 와챠피디아 크롤링
            try:
                picture_url, video_url, reviews, content_url=selenium_data(response['title'], response['release_date'].split('-')[0])
                
                response['picture_url'] = picture_url if picture_url else None
                response['video_url']=video_url if video_url else None
                response['reviews']=reviews if reviews else None
                response['watchapedia'] = content_url
            except:
                response['picture_url'] =None
                response['video_url']=None
                response['reviews']=None
                response['watchapedia'] = None
                print("can't get watcha detail ", response['title'], ' | ', movie_id, ' | ', response['release_date'])
            
            
            # 포스터 색감 추출하기
            try:
                palette = extract_colors(image_url=response['poster_path'])
                poster_palette = list(map(lambda x:[x.rgb[0], x.rgb[1], x.rgb[2], x.freq], palette))
                response['poster_palette']=poster_palette
            except:
                response['poster_palette']=None
                print("\ncolor extract error : \n response['poster_path'] \n ", response['title'], ' | ', movie_id, '\n')
        # 처리 완료된 페이지 내용 결과에 추가
        # movie_results+=responses
        file_out(f'movies_{str(i).zfill(2)}', responses)
        print(f'\n\nmovies_{str(i).zfill(2)}\n\n')
        # movie_results=[]
    dr.quit()


# 완성된 데이터 json으로 저장
def file_out(dataname, data):
    with open(f'{dataname}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent="\t", cls=NpEncoder)
    print(len(data))

def file_set():
    result=[]
    for i in range(1,51):
        with open(f'movies/movies_{str(i).zfill(2)}.json', 'r', encoding='utf-8') as file:
            result += json.load(file)
    file_out("movies", result)

if __name__=='__main__':
    # provider_data()
    # genre_data()
    movie_data(51,100)
    # file_set()
    # selenium_data('더그의 일상: 칼의 데이트', '2023')
    # movie=[
        # ('칼의 데이트', '2023'),
        # ('미라큘러스 월드: 파리, 셰이디버그와 블랙클로', '2023'),
        # ('스루 마이 윈도: 너에게 머무는 시선','2024'),
        # ('스타워즈: 라스트 제다이', '2017'),
        # ('존 윅 - 리로드','2017'),
        # ('터미네이터 2', '1991'),
        # ('애니','2014'),
        # ('스타워즈: 라이즈 오브 스카이워커','2019'),
    #     ('터미네이터 3','2003'),
    #     ('패스터','2010'),
    # ]
    # result=[]
    # for name, year in movie:
    #     response={}
    #     try:
    #         picture_url, video_url, reviews, content_url=selenium_data(name, year)
            
    #         response['picture_url'] = picture_url if picture_url else None
    #         response['video_url']=video_url if video_url else None
    #         response['reviews']=reviews if reviews else None
    #         response['watchapedia'] = content_url
    #     except:print("can't get watcha detail ", name, '|', year)
    #     if response:result.append(response)
    
    # file_out('extrasa', result)
    # testdata=[{'name':None, 'test':'hello'}]
    # file_out('test', testdata)