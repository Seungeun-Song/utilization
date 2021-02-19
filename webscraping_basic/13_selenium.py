# web driver 설치 - chrome drive.exe

from selenium import webdriver

browser = webdriver.Chrome()  # "C:/Users/SONG/utilization/chromedriver.exe"
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem

elem.click()

browser.back()
browser.forward()
browser.refresh()

elem = browser.find_element_by_id("query")
elem

from selenium.webdriver.common.keys import Keys  # keys.enter을 위해. 즉 엔터를 치기 위해서. 검색버튼을 find할 거면 필요X
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)