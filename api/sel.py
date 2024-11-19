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
options.add_argument('--blink-settings=imagesEnabled=false')
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
wait = WebDriverWait(dr, 5)
dr.get(url)
dr.implicitly_wait(5)
act = ActionChains(dr)

try:
    bt = WebDriverWait(dr, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.hsDVweTz")))
    bt.click()
except:pass

sleep(1)

search_box = WebDriverWait(dr, 3).until(EC.visibility_of_element_located((By.NAME, "searchKeyword")))

movie_name = "글래디에이터"
movie_year = '2000'
search_box.send_keys(movie_name)
search_box.send_keys(Keys.ENTER)

sleep(1)

movie_box = WebDriverWait(dr, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "v1F9TlrZ")))
movie_list = WebDriverWait(movie_box, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "listWrapper")))

movie = WebDriverWait(movie_list, 3).until(EC.visibility_of_element_located((By.XPATH, f"//a[@title='{movie_name}']//div[contains(text(), {movie_year})]")))
movie.click()

# sleep(1)

sleep(10)
dr.quit()