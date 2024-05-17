from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd 

screenshots_dir = "screenshots"
url = "https://www.facebook.com/eunju.seo.739/"

options = Options()
#options.add_argument('__headless')
options.add_experimental_option("detach", True) 
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                         options=options)
#구글접속
browser.get(url)


sleep(1)
browser.quit()

