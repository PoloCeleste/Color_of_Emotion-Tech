from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.safari.options import Options as SOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


options = Options()
# options.add_argument("--headless")  # 129버전에선 --headless=old로 흰창 날릴 순 있으나 다른버전에서 문제 생길 수 있으므로 저 멀리 날려버림
# options.add_argument("--window-position=-15400,-15400")  # 창이 뜨는 위치 변경. 4k나 8k에선 보일수도?
options.add_argument("log-level=3")
# options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36")
options.add_argument("--window-size=1920,1080")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
options.add_experimental_option("useAutomationExtension", False)
service = Service(ChromeDriverManager().install())

url = 'https://pedia.watcha.com/ko-KR'

dr = webdriver.Chrome(service=service, options=options)
# dr = webdriver.Safari(options=options)
dr.get(url)
wait = WebDriverWait(dr, 5)
act = ActionChains(dr)

dr.implicitly_wait(5)

try:
    bt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.hsDVweTz")))
    bt.click()
except:pass

dr.implicitly_wait(5)

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "searchKeyword")))

movie_name = "글래디에이터"
movie_year = '2000'
search_box.send_keys(movie_name)
search_box.send_keys(Keys.ENTER)

dr.implicitly_wait(10)

movie_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v1F9TlrZ")))
movie_list = WebDriverWait(movie_box, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "listWrapper")))

movie = WebDriverWait(movie_list, 5).until(EC.visibility_of_element_located((By.XPATH, f"//a[@title='{movie_name}']//div[contains(text(), {movie_year})]")))
movie.click()

sleep(1)

contents_url = dr.current_url+'/comments'

gal_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='갤러리']/following-sibling")))
gal = WebDriverWait(gal_name, 5).until(EC.visibility_of_element_located((By.XPATH, '..child::section')))
dr.execute_script("arguments[0].scrollIntoView({block : 'center'});", gal)
sleep(0.5)
btn=WebDriverWait(gal, 2).until(EC.element_to_be_clickable((By.XPATH, "./button[@title='right']")))

while True:
    try:
        btn.click()
        sleep(0.1)
        print(1)
    except:
        print('end')
        break

galleries = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'MfhUSmJK')))

for gallery in galleries:
    pic = WebDriverWait(gallery, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "div")))
    pstyle = pic.get_attribute('style')
    print(pstyle)


sleep(1)

try:
    videotag = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "g9zBSzqQ")))
    dr.execute_script("arguments[0].scrollIntoView({block : 'center'});", videotag)
    sleep(0.5)
    video=WebDriverWait(videotag, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "div")))
    vstyle=video.get_attribute('style')
    vid=vstyle.split(';')[-2].split('/')[-2]
    print()
except:print("None video")




sleep(1)

dr.get(contents_url)

sleep(3)
dr.quit()