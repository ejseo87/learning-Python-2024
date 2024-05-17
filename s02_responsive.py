from math import ceil
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sizes = [480,960,1366,1920]

class ResponsiveTester:

    def __init__(self, urls):
        options = Options()
        options.add_experimental_option("detach", True) 
        self.browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                         options=options)
        self.browser.maximize_window()
        self.urls = urls

    def screenshot(self, url):
        BROWSER_HEIGHT = 1027
        self.browser.get(url)
        for size in sizes:
            self.browser.set_window_size(size,BROWSER_HEIGHT)
            #윈도우 맨 위로 이동
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(1)
            # 자바스크립 실행결과를 return 을 이용하여 파이썬에 전달
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            total_sections=ceil(scroll_size/BROWSER_HEIGHT)
            for section in range(total_sections+1):
                #print(size,":좌표(0.",(section)*BROWSER_HEIGHT,")")
                self.browser.execute_script(
                    f"window.scrollTo(0, { (section) * BROWSER_HEIGHT})"
                )
                self.browser.save_screenshot(f"screenshots/{size}x{section}.png")
                time.sleep(1)

    def start(self):
        for url in self.urls:
            self.screenshot(url)


tester = ResponsiveTester(["https://nomadcoders.co","http://aladin.co.kr"])
tester.start()




