from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class GoogleKeywordScreenShooter:
    def __init__(self, keyword, screenshots_dir):
        options = Options()
        options.add_experimental_option("detach", True) 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        #self.browser = webdriver.Chrome(service=Service(),options=options)
        # 여기에 최신 릴리즈 버전의 구글 드라이버 버전이 있음
        release = "https://chromedriver.storage.googleapis.com/LASTEST_RELEASE"
        # 버전명 가져오기
        version = requests.get(release).text
        # ChromeDriverManager에 가져온 버전을 넣어준다
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager(version=version).install()), options=options)
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
    
    def start(self):
        #구글접속
        self.browser.get("https://google.com")
        #검색 입력창 찾기 (검색창 이름 = 'q')
        search_bar=self.browser.find_element(By.CLASS_NAME, "gLFyf")
        #검색어 입력
        search_bar.send_keys(self.keyword)
        #검색실행
        search_bar.send_keys(Keys.ENTER)
        """
        구글에서 검색하고 selenium에서 inspect하는 시간이 너무 짧아서 요소를 읽을수가 없습니다.
        WebDriverWait를 사용하면 페이지 로딩을 기다린 후에 작업을 하게 됩니다.
        .until() 구문과 합쳐서 class_name이 "g"인 것이 나올때까지 일정시간 기다립니다.
        1초나 2초 기다리게 설정하면 다 못읽어와서 5초 정도 설정하니 다 불러옵니다.
        그냥 저는 20초로 설정했는데, 로딩 그 전에 다 끝나면 넘어가기 때문에 적당히 해두세요.
        """
        try:
            useless_element=WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cUnQKe"))) #CDYQAA 관련검색
            useless_element.screenshot("useless_element.png") 
            # jabascript로 관련질문 section을 제거
            self.browser.execute_script(
                """
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty)
                """,
                useless_element,
            )
        except Exception:
            pass
        #검색 결과를 스크린샷으로 저장
        search_results=self.browser.find_elements(By.CLASS_NAME,"g")
        print("###########")
        for index, search_result in enumerate(search_results) :
            class_name=search_result.get_attribute("class")
            print(index, ":", class_name)
            search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")
        print("###########")
    
    def finish(self):
        self.browser.quit()


domain_competitors = GoogleKeywordScreenShooter("buy domain", "screenshots")
python_competitors = GoogleKeywordScreenShooter("bython book", "screenshots2")
domain_competitors.start()
domain_competitors.finish()
python_competitors.start()
python_competitors.finish()

