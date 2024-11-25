import requests, json, os
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
import requests, sys

if len(sys.argv) > 1 and sys.argv[1] in ('movie', 'selenium'):
    options = Options()
    options.add_argument("--headless")  # 129버전에선 --headless=old로 흰창 날릴 순 있으나 다른버전에서 문제 생길 수 있으므로 저 멀리 날려버림
    options.add_argument("--window-position=-15400,-15400")  # 창이 뜨는 위치 변경. 4k나 8k에선 보일수도?
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


def selenium_data(movie_name, movie_year, movie_url=None):
    
    # if '블랙펄' in movie_name:movie_name = movie_name.replace('블랙펄', '블랙 펄')
    # if '크레용' in movie_name:movie_name = movie_name.replace('보라색', '마법')
    # if '번개도둑' in movie_name:movie_name = movie_name.replace('번개도둑', '번개 도둑')
    # if '엔젤 해즈 폴른' == movie_name:movie_name = '앤젤 해즈 폴른'
    # if '블레어 위치' == movie_name:movie_name = '블레어 윗치'
    # if '장난감이 살아있다' == movie_name:movie_year = '2016'
    # if '엠 아이 오케이?' == movie_name:movie_year = '2022'
    # if '킬 빌: 1부' == movie_name:movie_name = '킬 빌'
    # if '밀레니엄: 제1부 여자를 증오한 남자들' == movie_name:movie_name = '밀레니엄 1 : 여자를 증오한 남자들'
    # if '애니 2015' == movie_name:movie_name = '애니'
    
    if movie_url==None:
        search_box = wait.until(EC.visibility_of_element_located((By.NAME, "searchKeyword")))
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        search_box.send_keys(movie_name)
        search_box.send_keys(Keys.ENTER)

        sleep(0.5)

        try:
            movie_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v1F9TlrZ")))
        except: 
            try:
                if ":" in movie_name:
                    elmovie=movie_name.split(":")[0]
                    movie_name=movie_name.split(":")[1]
                elif '2' in movie_name or '3' in movie_name: movie_name=movie_name.replace('2','').replace('3','')
                search_box = wait.until(EC.visibility_of_element_located((By.NAME, "searchKeyword")))
                search_box.send_keys(Keys.CONTROL + "a")
                search_box.send_keys(Keys.DELETE)
                search_box.send_keys(movie_name)
                print(movie_name)
                search_box.send_keys(Keys.ENTER)
                sleep(0.5)
                movie_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v1F9TlrZ")))
            except:
                movie_name=elmovie
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

        
    else:
        dr.get(movie_url)

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
    cannot=[]
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
        for index,response in enumerate(responses):
            # 필요 없는 항목 삭제
            for d in de:
                del response[d]
            
            # 영화 제목이 '한글제목' - 영어제목 인 경우 한글제목만 나오도록 수정
            if "'" in response['title']: response['title']= response['title'].split("'")[1]
            
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
                print("can't get watcha detail ", response['title'], ' | ', movie_id, ' | ', response['release_date'], ' | index: ', index)
                cannot.append({response['title']:{'page':i, 'index':index, 'year':response['release_date'].split('-')[0]}})
            
            # 포스터 색감 추출하기
            try:
                palette = extract_colors(image_url=response['poster_path'])
                poster_palette = list(map(lambda x:[x.rgb[0], x.rgb[1], x.rgb[2], x.freq], palette))
                response['poster_palette']=poster_palette
            except:
                response['poster_palette']=None
                print("\ncolor extract error : \n response['poster_path'] \n ", response['title'], ' | ', movie_id, '\n')
        file_out(f'movies_{str(i).zfill(2)}', responses)
        print()
    file_out(f'movies_cannot_{str(start_page).zfill(2)}_to_{str(end_page).zfill(2)}', cannot)
    print()
    dr.quit()



# 완성된 데이터 json으로 저장
def file_out(dataname, data):
    if not os.path.exists('movies_data'): os.makedirs('movies_data')
    with open(f'movies_data/{dataname}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent="\t", cls=NpEncoder)
    f.close
    print(f'\nmovies_data/{dataname}.json에 {len(data)}개 데이터 저장 완료.\n')



# 저장된 json 합치기
def file_set(start_page = 1, end_page = 50):
    try:
        result=[]
        for i in range(start_page, end_page+1):
            with open(f'movies_data/movies_{str(i).zfill(2)}.json', 'r', encoding='utf-8') as file:
                result += json.load(file)
            file.close
        file_out("movies", result)
    except:
        print('파일 또는 경로 없는듯.')



# selenium 크롤링 재시도
def try_selenium(start_page, end_page):
    cannots=[]
    with open(f'movies_data/movies_cannot_{str(start_page).zfill(2)}_to_{str(end_page).zfill(2)}.json', 'r', encoding='utf-8') as file:
        cannots += json.load(file)
    for cannot in cannots:
        for movie_name, data in cannot.items():
            try:
                result=[]
                with open(f'movies_data/movies_{str(data["page"]).zfill(2)}.json', 'r', encoding='utf-8') as file:
                    result+=json.load(file)
                file.close
                movie_url=None
                
                if 'movie_url' in data:movie_url=data['movie_url']
                
                picture_url, video_url, reviews, content_url=selenium_data(movie_name, data['year'], movie_url)                
                result[data['index']]['title'] = movie_name
                result[data['index']]['picture_url'] = picture_url if picture_url else None
                result[data['index']]['video_url']=video_url if video_url else None
                result[data['index']]['reviews']=reviews if reviews else None
                result[data['index']]['watchapedia'] = content_url
                
                file_out(f'movies_{str(data["page"]).zfill(2)}', result)
            except:print("can't get watcha detail ", movie_name, '|', data['year'])



# 프로그램 사용법 출력
def help():
    print("\n** 주의 : tmdb.py 파일과 같은 경로상에 .env 파일이 필요합니다. **")
    print("** tmdb=<TMDB API Access Token Auth> 형식으로 저장, utf-8로 인코딩. **\n")
    print("\n인자 사용법")
    print("\nmovie <시작페이지> <종료페이지> (구분자 공백)")
    print('\t: TMDB 상 인기 순 <시작페이지>부터 <종료페이지>까지 가져오기')
    print('\t: 한 페이지만 입력할 경우 1페이지부터 입력페이지까지 가져옵니다.')
    print("\nprovider")
    print("\t: 영화 공급자 목록 가져오기")
    print("\ngenre")
    print("\t: 영화 장르 목록 가져오기")
    print('\nfile <시작페이지> <종료페이지> (구분자 공백)')
    print('\t: 만들어진 movie 데이터 <시작페이지>부터 <종료페이지>까지 파일 병합')
    print('\t: 한 페이지만 입력할 경우 1페이지부터 입력페이지까지 가져옵니다.')
    print('\nselenium <시작페이지> <종료페이지> (구분자 공백)')
    print('\t: Watchapedia 추가 크롤링 시도하기')
    print('\t: movie 데이터 생성 시 생성 된 cannot.json 파일 "수정" 후 실행.')
    print('\t: cannot.json 파일 명에 포함된 시작페이지와 종료페이지 필수 입력.')
    print('\t: 숫자로만 입력합니다. (앞에 0이 붙어있는 경우 떼고 작성)')
    print()



if __name__=='__main__':
    print()
    if len(sys.argv)==1:
        help()

    elif sys.argv[1]=='movie':
        if len(sys.argv)==2:
            print("기본 값 1페이지부터 기본 값 50페이지까지 가져옵니다.\n")
            movie_data()
        elif len(sys.argv)==3:
            try: 
                print(f"기본 값 1페이지부터 입력 값 {int(sys.argv[2])}페이지까지 가져옵니다.\n")
                movie_data(end_page=int(sys.argv[2]))
            except: print('페이지는 숫자로만 입력해주세요.')
        else: 
            try:
                if int(sys.argv[2]) > int(sys.argv[3]):
                    print("종료페이지가 시작페이지보다 작습니다.")
                else:
                    print(f"입력 값 {int(sys.argv[2])}페이지부터 입력 값 {int(sys.argv[3])}페이지까지 가져옵니다.\n")
                    movie_data(int(sys.argv[2]), int(sys.argv[3]))
            except: print('페이지는 숫자로만 입력해주세요.')
    
    elif sys.argv[1]=='provider': 
        print("영화 공급자를 가져옵니다.\n")
        provider_data()

    elif sys.argv[1]=='genre':
        print("영화 장르 목록을 가져옵니다.\n")
        genre_data()
        
    elif sys.argv[1]=='file':
        if len(sys.argv)==2:
            print("기본 값 1페이지부터 기본 값 50페이지까지 병합합니다.\n")
            file_set()
        elif len(sys.argv)==3:
            try: 
                print(f"기본 값 1페이지부터 입력 값 {int(sys.argv[2])}페이지까지 병합합니다.\n")
                file_set(end_page=int(sys.argv[2]))
            except: print('페이지는 숫자로만 입력해주세요.')
        else: 
            try:
                if int(sys.argv[2]) > int(sys.argv[3]):
                    print("종료페이지가 시작페이지보다 작습니다.")
                else:
                    print(f"입력 값 {int(sys.argv[2])}페이지부터 입력 값 {int(sys.argv[3])}페이지까지 병합합니다.\n")
                    file_set(int(sys.argv[2]), int(sys.argv[3]))
            except: print('페이지는 숫자로만 입력해주세요.')

    elif sys.argv[1]=='selenium':
        print('크롤링 실패한 영화들을 다시 시도합니다.\n')
        try:try_selenium(int(sys.argv[2]), int(sys.argv[3]))
        except: print('cannot.json 파일 명에 포함된 시작페이지와 종료페이지는 필수 입력입니다.')
        
    elif sys.argv[1]=='help':help()
    else:
        print('사용법을 확인해주세요.')
        help()
