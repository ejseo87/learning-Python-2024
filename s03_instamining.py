from math import ceil
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 프로그램을 위해서 계정을 새로 만들었음
# 이메일주소기반 계정으로 ejseo69@naver.com
INSTAGRAM_ID = "ejseo69"
INSTAGRAM_PASSWD = "SEO7453!"

options = Options()
options.add_experimental_option("detach", True) 
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                options=options)
browser.get("https://www.instagram.com/accounts/login/")
WebDriverWait(browser, 3).until(
EC.presence_of_element_located((By.CLASS_NAME, "_ab3b")))

insta_id = browser.find_element(By.NAME, "username")
insta_password = browser.find_element(By.NAME,"password")

insta_id.send_keys(INSTAGRAM_ID)
insta_password.send_keys(INSTAGRAM_PASSWD)

insta_password.send_keys(Keys.ENTER)

WebDriverWait(browser, 10).until(
EC.presence_of_element_located((By.CLASS_NAME, "x1n2onr6"))) #class="x1n2onr6"
# 로그인 완료

#https://www.instagram.com/explore/tags/netflix/
main_hashtag ="netflix"

browser.get(f"https://www.instagram.com/explore/tag/{main_hashtag}")
#time.sleep(10)

#browser.quit()
